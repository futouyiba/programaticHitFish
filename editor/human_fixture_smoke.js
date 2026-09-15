const { chromium } = require('playwright');
const assert = (condition, message) => { if (!condition) throw new Error(message); };
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const browser = await chromium.launch({headless: true});
  const page = await browser.newPage();
  await page.goto('http://127.0.0.1:8765');
  await page.locator('#status').filter({hasText: 'Saved Source loaded'}).waitFor();

  // T1 Species Shared edit -> inherited resolved value changes, ProgramRef unchanged.
  await page.getByRole('button', {name: 'Species Shared'}).click();
  const structure = page.getByLabel('structure_affinity');
  await structure.fill('0.70');
  await structure.press('Tab');
  await sleep(100);
  let preview = await page.locator('#preview').innerText();
  assert(preview.includes('structure_affinity = 0.7'), 'T1 resolved Species Shared value did not update');
  assert(preview.includes('INHERITED ← SPECIES_SHARED'), 'T1 provenance is not Species Shared');
  assert(preview.includes('BakeProgramRef = BAKE_NORMAL'), 'T1 unexpectedly changed ProgramRef');

  // T2 Provenance readback across current owners.
  assert(preview.includes('OVERRIDE ← FISH_QUALITY'), 'T2 FishQuality provenance missing');
  assert(preview.includes('OVERRIDE ← ENGAGEMENT_MODE'), 'T2 Engagement Mode provenance missing');
  assert(preview.includes('INHERITED ← SHARED_PROFILE / BASS_BASE_PROFILE'), 'T2 Shared Profile provenance missing');
  assert(preview.includes('FACT ← ENVIRONMENT_FACT'), 'T2 Environment Fact provenance missing');
  assert(preview.includes('Program-owned logic'), 'T2 Program-owned logic missing');

  // T3 Program switch -> inherited + missing + orphaned -> repair -> VALID.
  await page.getByRole('button', {name: 'Reset Saved Baseline'}).click();
  await sleep(100);
  await page.getByRole('button', {name: 'Engagement Mode', exact: true}).click();
  await page.getByLabel('BakeProgramRef').selectOption('BAKE_ALT');
  await sleep(100);
  const missingRow = page.locator('tr').filter({hasText: 'ambush_threshold'});
  assert((await missingRow.innerText()).includes('MISSING'), 'T3 missing required param not visible');
  assert((await page.locator('#workspace').innerText()).includes('ORPHANED: normal_bias'), 'T3 orphaned param not visible');
  await missingRow.locator('input').fill('0.4');
  await missingRow.locator('input').press('Tab');
  await sleep(100);
  await page.locator('#workspace').getByRole('button', {name: 'Remove'}).click();
  await sleep(100);
  await page.getByRole('button', {name: 'Validate / Compile'}).click();
  await page.locator('#status').filter({hasText: 'VALID'}).waitFor();

  // T4 Program logic edit -> localized error -> repair.
  await page.getByRole('button', {name: 'Reset Saved Baseline'}).click();
  await sleep(100);
  await page.getByRole('button', {name: 'Bake Program Editor'}).click();
  await page.locator('#dslSource').fill('let weight = 1.0\nreturn ???');
  await page.getByRole('button', {name: 'Apply DSL Draft'}).click();
  await sleep(100);
  await page.getByRole('button', {name: 'Validate / Compile'}).click();
  await page.locator('#status').filter({hasText: 'Bake DSL line 2'}).waitFor();
  await page.locator('#dslSource').fill('let weight = 1.0\nreturn weight');
  await page.getByRole('button', {name: 'Apply DSL Draft'}).click();
  await sleep(100);
  await page.getByRole('button', {name: 'Validate / Compile'}).click();
  await page.locator('#status').filter({hasText: 'VALID'}).waitFor();

  // T5 OVERALLOCATED -> diagnostics -> repair without normalization/priority escape.
  await page.getByRole('button', {name: 'Reset Saved Baseline'}).click();
  await sleep(100);
  await page.getByRole('button', {name: 'Load T5 OVERALLOCATED'}).click();
  await page.locator('#routingDiagnostics').filter({hasText: 'OVERALLOCATED: Q3'}).waitFor();
  const q3Active = page.locator('tr').filter({hasText: 'Q3'}).filter({hasText: 'ACTIVE_SPAWNING'});
  await q3Active.locator('input').fill('0.20');
  await q3Active.locator('input').press('Tab');
  await sleep(100);
  await page.getByRole('button', {name: 'Validate / Compile'}).click();
  await page.locator('#status').filter({hasText: 'VALID'}).waitFor();

  // Deterministic reset restores baseline.
  await page.getByRole('button', {name: 'Reset Saved Baseline'}).click();
  await sleep(100);
  await page.getByRole('button', {name: 'Species Shared'}).click();
  assert(await page.getByLabel('structure_affinity').inputValue() === '0.8', 'Reset did not restore baseline');

  console.log('HUMAN_FIXTURE_SMOKE_PASS: T1 T2 T3 T4 T5 RESET');
  await browser.close();
})().catch(async error => {
  console.error(error);
  process.exit(1);
});
