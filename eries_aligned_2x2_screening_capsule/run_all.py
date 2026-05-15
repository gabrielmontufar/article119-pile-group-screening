from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT.parent / "06 Journal instructions and audit"
TESTS = [
    "qa_decision_validation_passport_check.py",
    "qa_eries_claims_check.py",
    "qa_reproducible_2x2_enumeration_check.py",
    "qa_claim_governance_novelty_check.py",
    "qa_csi_formula_check.py",
    "qa_forbidden_claims_gate.py",
    "qa_journal_fit_check.py",
    "qa_theoretical_math_consistency.py",
    "qa_secondary_evidence_focus_and_refs_check.py",
    "qa_external_blind_validation_protocol_check.py",
    "qa_open_source_e4_validation_strategy_check.py",
    "qa_interface_layer_e4_benchmark_check.py",
    "qa_v4s_validation_check.py",
    "qa_displacement_reconciliation_check.py",
    "qa_text_table_figure_consistency_check.py",
    "qa_consistency_check.py",
]

for test in TESTS:
    path = AUDIT / test
    if not path.exists():
        raise SystemExit(f"Missing QA gate: {path}")
    print(f"RUN {test}")
    subprocess.check_call([sys.executable, str(path)])
print("ERIES_ALIGNED_2X2_SCREENING_CAPSULE_QA_PASSED")
