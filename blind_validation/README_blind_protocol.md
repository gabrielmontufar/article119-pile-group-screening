# External blind validation protocol

Created UTC: 2026-05-15T18:29:40.385815+00:00

This folder implements a non-GEOLAB procedural blind-validation check using three third-party published lateral pile-group load-displacement curves:

1. Rollins et al. 2005 9-pile group, via PileGroups validation example 4.
2. Christensen 2006 9-pile group, via PileGroups validation example 5.
3. Walsh 2005 3x5 pile group, via PileGroups validation example 6.

## Blind sequence

1. `blind_inputs.csv` records only source, geometry/topology class, soil description and applied load points. It does not contain measured displacements.
2. `blind_predictions_frozen.csv` is generated from the disclosed inputs using the frozen normalized screening prior:
   `u_max = 1.8 sqrt(Hmax_kN)` and `u = u_max h/(1.25 - 0.25h)`, where `h = H/Hmax`.
3. The SHA-256 hash of `blind_predictions_frozen.csv` is written in `hash_manifest.json`.
4. `blind_outputs_revealed.csv` then reveals the digitized measured displacements from the third-party figures.
5. `error_metrics.csv` compares prediction and measurement using MAE, RMSE, normalized RMSE and secant stiffness at approximately 50% load.

## Claim boundary

This is a complete external blind curve-scale check relative to the information flow in this folder: outputs are absent from the input file and predictions are frozen before outputs are revealed. It is not a site-specific calibration of the ERIES-aligned selected case, not a laboratory validation of the proposed cyclic degradation law, and not a final-design verification. Its defensible claim is that the screening workflow can be tested against independent published pile-group curves under a documented blind protocol.

## Hashes

```json
{
  "created_utc": "2026-05-15T18:29:40.385815+00:00",
  "protocol": "external non-GEOLAB procedural blind validation",
  "blind_inputs_sha256": "d394fe1925609f7110dcb759abd3a00a0716d5c25374eb6962a621f3d829a729",
  "blind_predictions_frozen_sha256": "4a5570c281daf73ed449160a4994eaa38f17c66bc66e7634e33a30a8dc8f535b",
  "blind_outputs_revealed_sha256": "a548a1ca4dc83e633533f9ee654556ebd2a93fc7dc8e693bddba8c6b3fbab5c8",
  "error_metrics_sha256": "178578fe87c2fc8763d4669ce5159504ba2e003d65b325eb246ac0ea267d0bce",
  "source_manifest_sha256": "87d937345af8c482c5838201a08a938c796b0e9b94d446aa726fcfb5b94a0181",
  "cases": [
    "BV-Rollins2005-9pile-sand",
    "BV-Christensen2006-9pile-sand",
    "BV-Walsh2005-3x5-sand"
  ]
}
```
