"""Fish-Centric Conditional Funnel V1 reference implementation."""

from .model import (
    Candidate,
    ContactIntent,
    ContactType,
    EntryGrade,
    EntryMotive,
    EntryOpportunity,
    LifecycleSlice,
    PopulationSource,
    SettlementKind,
    SpeciesCapability,
    WorldFacts,
    ActualPresentation,
    FishVariant,
)
from .engine import FCFEngine
from .dsl import DSLCompileError, Diagnostic, compile_artifact
from .lifecycle import LifecycleCommitment, SliceAllocator, SliceKey
from .resolution import (
    EncounterState,
    allocate_occupancy,
    encounter_step,
    hook_compatibility,
    resolve_entry_offer,
    resolve_motive,
    validate_arrival_placement,
)
from .trace import ExplainTrace, StageTrace, entry_trace
from .editor import ArtifactStore, ArtifactVersion
from .journal import DurableJournal, JournalConflict, JournalAdapter, SQLiteJournal
from .conformance import ConformanceCheck, ConformanceReport, run_core_conformance
from .temperature_profile import compile_temperature_profile
from .pre_generation import (
    ResolveSnapshotBundle, RootSemanticOccurrence, OpportunityBasis,
    OpportunityId, SemanticSupportRef, CandidateContribution, CandidateBasisKey,
    CandidateEntry, MeaningResponse, ResolveResult, MaterializationPlan,
    ConcreteFishResult, PreGenerationHarness,
)
from .authoring import CompiledContentBundle, AuthoringError, lint_authoring, compile_authoring

__all__ = [
    "Candidate",
    "ContactIntent",
    "ContactType",
    "EntryGrade",
    "EntryMotive",
    "EntryOpportunity",
    "FCFEngine",
    "LifecycleSlice",
    "PopulationSource",
    "SettlementKind",
    "SpeciesCapability",
    "WorldFacts",
    "ActualPresentation",
    "FishVariant",
    "DSLCompileError",
    "Diagnostic",
    "compile_artifact",
    "LifecycleCommitment",
    "SliceAllocator",
    "SliceKey",
    "EncounterState",
    "allocate_occupancy",
    "encounter_step",
    "hook_compatibility",
    "resolve_entry_offer",
    "resolve_motive",
    "validate_arrival_placement",
    "ExplainTrace",
    "StageTrace",
    "entry_trace",
    "ArtifactStore",
    "ArtifactVersion",
    "DurableJournal",
    "SQLiteJournal",
    "JournalAdapter",
    "ConformanceCheck",
    "ConformanceReport",
    "run_core_conformance",
    "JournalConflict",
    "compile_temperature_profile",
    "ResolveSnapshotBundle", "RootSemanticOccurrence", "OpportunityBasis", "OpportunityId",
    "SemanticSupportRef", "CandidateContribution", "CandidateBasisKey", "CandidateEntry",
    "MeaningResponse", "ResolveResult", "MaterializationPlan", "ConcreteFishResult",
    "PreGenerationHarness",
    "CompiledContentBundle", "AuthoringError", "lint_authoring", "compile_authoring",
]
