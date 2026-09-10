const { chromium } = require('/Users/stephen-us/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const path = require('path');
const { pathToFileURL } = require('url');
(async () => {
  const browser = await chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
  const page = await browser.newPage({viewport:{width:1440,height:1000},deviceScaleFactor:1});
  const errors=[];
  page.on('pageerror', e=>errors.push(String(e)));
  await page.goto(pathToFileURL(path.join(__dirname,'index.html')).href);
  await page.screenshot({path:path.join(__dirname,'desktop.png')});
  await page.locator('#search').fill('C08');
  if (await page.locator('.case[data-search]:not(.hide)').count() !== 1) throw Error('search failed');
  await page.locator('.case[data-search]:not(.hide)').scrollIntoViewIfNeeded();
  await page.locator('#expand').click();
  await page.screenshot({path:path.join(__dirname,'c08.png')});
  await page.locator('#mode').click();
  if (!await page.locator('body').evaluate(e=>e.classList.contains('single'))) throw Error('toggle failed');
  await page.locator('#search').fill('');
  await page.locator('#group').selectOption('BASS');
  if (await page.locator('.case[data-search]:not(.hide)').count() !== 6) throw Error('Bass filter failed');
  await page.setViewportSize({width:390,height:844});
  await page.locator('#group').selectOption('C');
  await page.locator('#search').fill('C08');
  await page.locator('.case[data-search]:not(.hide)').scrollIntoViewIfNeeded();
  await page.screenshot({path:path.join(__dirname,'mobile.png')});
  const width=await page.evaluate(()=>({scroll:document.documentElement.scrollWidth,viewport:innerWidth}));
  if (width.scroll>width.viewport) {
    console.log(await page.evaluate(()=>[...document.querySelectorAll('body *')].filter(e=>e.getBoundingClientRect().right>innerWidth&&getComputedStyle(e).display!=='none').slice(0,20).map(e=>({tag:e.tagName,cls:e.className,text:e.textContent.slice(0,80),right:e.getBoundingClientRect().right}))));
    await browser.close();throw Error('mobile horizontal overflow '+JSON.stringify(width));
  }
  if(errors.length)throw Error(errors.join('\n'));
  console.log(JSON.stringify({search:'PASS',filter:'PASS',mode:'PASS',mobileWidth:width,consoleErrors:errors}));
  await browser.close();
})();
