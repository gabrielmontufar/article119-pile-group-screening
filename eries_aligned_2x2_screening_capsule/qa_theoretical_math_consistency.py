from pathlib import Path
from docx import Document

ROOT = Path(r"C:\Users\gjm31\OneDrive\Escritorio\articulos up\119 avo art\Entrega International Journal of Geotechnical Engineering 20260515")
DOC = ROOT / "01 Manuscript" / "Cyclic Lateral Pile Group - IJGE manuscript.docx"
AUDIT = ROOT / "06 Journal instructions and audit" / "theoretical_mathematical_solidity_upgrade.md"
text = "\n".join(p.text for p in Document(DOC).paragraphs)
required = [
    "Mathematical formulation of the finite screening problem",
    "x = (D, L, rho)",
    "D_set = {0.60, 0.75, 0.90, 1.05, 1.20}",
    "min C_norm(x) subject to g_j(x) <= 1",
    "Table 2a. Dimensional consistency audit",
    "gamma_FEM is a deterministic anchoring operator",
    "Table 24r. Mathematical propositions",
    "Physically parameterized 3D interface-compliance benchmark",
    "Omega_s",
    "Omega_p",
    "Omega_i",
    "Table 24s. Separation of prediction",
    "not a confidence interval",
]
for item in required:
    assert item in text, item
for bad in [
    "gamma_FEM is a statistical",
    "field-calibrated prediction",
    "ERIES calibration of cyclic degradation",
    "universal p-y law",
]:
    assert bad.lower() not in text.lower(), bad
assert AUDIT.exists() and "Executive diagnosis" in AUDIT.read_text(encoding="utf-8")
print("THEORETICAL_MATH_CONSISTENCY_QA_PASSED")
