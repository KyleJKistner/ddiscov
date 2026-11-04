# Independent review — BLU3797 qualification package, article/exposure scope

Reviewed `ddiscov_round8/research/rounds/round8/blu3797-qualification-package.md` during Round8 against the article/exposure dossier, original JCI v2 PDF page14, official Thermo construct/protocol records and proposed lot criteria.

## Verdict

**No major contradiction in the material, catalytic-assay, target-engagement or comparator decisions.** The controlling package correctly separates prospective criteria from observations, does not infer the journal's actual reagent from the catalog mismatch, does not import28nM as a freeKi, and permits a useful functional positive below80% occupancy. It also correctly withholds a qualified target-negative conclusion when native engagement remains unresolved.

## Two recommended wording corrections

1. **Q0 bioanalysis: separate accuracy from extraction recovery.** The sentence “LC–MS accuracy/recovery80–120%” conflates two attributes. Absolute extraction recovery need not be80–120% for an analytically useful method if it is reproducible, characterized and appropriately corrected with the internal standard. Recommended: “Initial research LC–MS accuracy80–120% and precisionCV≤20%; extraction recovery, matrix effects and nonspecific binding are measured and sufficiently reproducible for the intended inference.” Material-dissolution recovery and free-fraction mass balance are separate measurements. Do not reject an otherwise sound assay merely because absolute extraction recovery is consistently60%.

2. **F1 exposure timing: use sampled pre-change concentration rather than unverified trough.** “Initial,predose/trough and endpoint” can imply that the sampled pre-refresh concentration is a validated minimum. Recommended: “After initial dosing, immediately before a specified medium change, after the final refresh and at the endpoint; record elapsed times. A sampled pre-change value is not asserted to be the true minimum without a suitable time course.” This mirrors the caution correctly applied to terminal mousePK.

## Nonblocking implementation details to carry into the release record

- qNMR95–105% is relative to the declared content/material basis, not a demand that every valid salt or hydrate contain≥95% neutralBLU by mass. The present wording is defensible; retain measured neutral-BLU mass fraction explicitly.
- HRMS426.1845894 is a calculated [M+H]+ target, not a recovered high-resolution journal result. Use concordant structure/stereochemistry, not mass alone.
- The primary JCI catalog text is **PV3574l** on v2 PDFpage14. ThermoPV5374 is GST155–1383. The hypothesis thatPV5374 was intended remains an inference; investigators are not accused of using buffer instead of enzyme.
- PRM peptide detection alone is not engagement. The NCI assets are a native-protein detection starting point; a dose-dependent, protein-specific CETSA response still requires qualification and does not become occupancy by normalization.
- The full article dossier includes chemical-source and assay-development stop/redirect rules. Avoid increasing the initial force block simply because a private NanoBRET tracer is unresolved.
- Exact47 remains the correct first comparator;91 is a conditional fallback after its own broader functional-panel liabilities are evaluated. The package preserves this.

## Numerical utility review

`round8_work/blu_identity_numeric_audit.py` is deterministic and standard-library only. It requires no downloads, credentials, source workbooks or third-party packages. An `--out` / `--output` argument now allows it to live at `methods/blu3797_identity_audit.py` while writing its JSON elsewhere. A rerun with `--out round8_work/blu_identity_numeric_audit_check.json` reproduced the existing audit byte-for-byte. Formulas, atomic masses and assumptions are embedded and visible; the output is arithmetic, not empirical chemical validation.

Example integration command:

```sh
python methods/blu3797_identity_audit.py --out research/rounds/round8/blu_identity_numeric_audit.json
```

No repository files were changed by this independent review.
