# Round 12 - Exact BLU3797 mapping to the published WO2025003330A1 claims

**Evidence cut: 4 November 2026. Baseline: `823c2be978b2eaa89c0f4796342f949589d5814f`, main. Public-document research only.** This audit maps the published S-BLU3797 structure to one selected patent publication. It adds no biological measurement, synthesis, simulation, procurement or outreach. The companion JSON preserves the atom correspondence, claim branches, source locations and unresolved interpretation.

## Decision

**The explicit variables in the published drawings do not provide a complete mapping of exact BLU3797: its 7-cyclopropylmethoxy substituent occupies the position labeled R8 when the fused lactam is aligned correctly. R8 is defined as a ring atom, C or N, with no drawn external substituent variable.** Reflecting the benzene mapping relocates the actual fused bond to an edge for which Formula 1 provides no ring-closing option. This is a specific drawing-level mismatch, replacing the earlier uncharted-genus statement. [B12-CS01, printed pp.293-294; physical pp.294-295]

**Legal coverage remains unresolved.** The specification's general definition of aryl permits substituted aryl, including alkoxy substitution. Whether that definition supplies additional substitution at the fixed R8 position is a material claim-construction question that this chemistry audit cannot settle. The report therefore does not conclude that BLU is legally excluded, patent-free, noninfringing, patentable or available to commercialize. [B12-CS01, printed pp.116-117; physical pp.117-118]

Retain BLU's existing **55 planning-effort points** and affirmative bounded qualification recommendation. The finding changes the independent-asset record: this family should not be described as an established blanket claim to all C2beta inhibitors, nor as a verified exact-BLU obstacle or clearance. A differentiated data contribution remains plausible; exclusive rights to an exact molecule or successor remain unestablished. Other patent families, prosecution, jurisdiction-specific claims, validity, equivalents and ownership are outside this structural mapping.

## 1. Exact article and source discipline

The article is **(S)-N-(5-(2-(1-cyclopropylethyl)-7-(cyclopropylmethoxy)-1-oxoisoindolin-5-yl)-4-methylthiazol-2-yl)acetamide**, the BLU3797 structure in JCI Figure 1A. The same name is given in the primary Methods. The figure and name were independently checked against the cached publisher v2 PDF, physical/printed pp.3 and 13. BLU2720, comparator47 and a precursor sharing the isoindolinone core are different articles. [B12-CS02]

The original WO PDF, rather than the title or text-only rendering, governs the depicted attachment positions in this audit. All 16 claim texts were reviewed; original drawings for the genus, fused-ring alternatives and linked claim branches were visually inspected. OCR helped navigate the scanned document. For this patent, **physical PDF page = printed page + 1** at the cited locations. The title's tetrahydroquinoline wording is narrower than the disclosed claimed alternatives: claims 4 and 10 explicitly draw an **isoindolinone** option. Rejecting BLU merely because it is an isoindolinone would be an error. [B12-CS01, printed pp.297 and 304; physical pp.298 and 305]

The earlier Round 5 work identified the family and inspected broad claim drawings but did not chart exact BLU inclusion/exclusion. Round 8 and Round 10 qualified comparator47's identity/pharmacology evidence, without resolving this claim topology. This sprint supplies that missing mapping; it does not relabel old comparator data as new activity evidence.

## 2. Fix the attachment graph before choosing substituents

Use the benzene atom attached to thiazole as the anchor, **b0**. Following the direction that encounters the patent's R7 first, Formula 1 has the six-atom cycle:

**b0, b1 = R7 with R10, b2 = carbon bearing R11, b3 = carbon bearing R14, b4 = R8, b5 = R9, returning to b0.**

These are audit labels, not additional patent variables. The two disclosed fusion alternatives are **D across b1-b2** through R10/R11, or **C across b2-b3** through R11/R14. Broad ring sizes and heteroatom choices change the added ring; they do not move its shared bond around B. [B12-CS01, printed pp.293-294; physical pp.294-295]

| Fixed Formula 1 position | Direct BLU correspondence | Reflected BLU correspondence |
|---|---|---|
| b0, attachment to thiazole | Isoindolinone position 5 | Position 5 |
| b1, R7 with R10 | Position 4, bearing H | Position 6, bearing H |
| b2, carbon bearing R11 | Fusion atom 3a | Position 7, bearing O-CH2-cyclopropyl |
| b3, carbon bearing R14 | Fusion atom 7a | Fusion atom 7a |
| b4, R8 | Position 7, bearing O-CH2-cyclopropyl | Fusion atom 3a |
| b5, R9 | Position 6, bearing H | Position 4, bearing H |
| Actual BLU fusion edge | b2-b3, the permitted C edge | b3-b4, not a permitted C or D edge |
| Specific obstruction under the explicit variables | No drawn substituent handle at b4/R8 for the 7-ether | The fusion would require joining the R14-bearing carbon to R8 |

The direct correspondence supports the fused lactam but leaves the ether unmatched. Reflection can put the ether at R11, where alkoxy is available, but then loses the correct fusion geometry. The D branch does not repair this: its fused atoms are one and two ring bonds from b0 along the relevant direction, while BLU's fusion atoms are two and three bonds from its thiazole-bearing position. Rotations of a drawing preserve those distances and do not create a third anchored mapping.

Changing the assignment of the entire rings also fails to create a new correspondence. BLU's thiazole is the ring with the required ring N and adjacent carbon carrying the external acetamide N; the lactam has no analogous external amino group at that position. Its benzene is the six-membered aromatic ring linked to that thiazole. The mapping therefore cannot silently move the anchor to a different aromatic carbon or interchange the lactam with ring A. These are direct connectivity comparisons, not computational modeling.

## 3. Element-by-element mapping

**Supported match** means that the identified local fragment is compatible with an explicit option. It does not mean the whole compound satisfies a claim. **Specific mismatch** is restricted to the explicit drawing and enumerated variables. **Interpretation unresolved** marks the specification-based alternative discussed below.

| Claim element | Exact BLU feature and assignment | Audit result | Primary location, printed / physical |
|---|---|---|---|
| A and n | Five-membered thiazole, n = 1 | Supported match | 293 / 294 |
| R1 and R6 | Thiazole sulfur; R1 = S, R6 absent | Supported match; no sulfur oxidation required | 293 / 294 |
| Ring N, R2 and R3 | Thiazole N at position 3; R2 = C at position 4; R3 = methyl | Supported match | 293 / 294 |
| Exocyclic N(R4R5) | Acetamide N attached at thiazole position 2, adjacent to the ring N; one substituent H and the other acetyl | Supported match to H and the permitted carbonyl-containing substituent; R4/R5 order is interchangeable | 293 / 294 |
| Bond from A to B | Thiazole position 5 linked to isoindolinone benzene position 5 | Supported match and fixed mapping anchor | 293 / 294; JCI 3 / 3 |
| R7, R8 and R9 atom identities | All three corresponding B-ring atoms are carbon | Supported atom-identity match; does not resolve R8's extra substituent | 293 / 294; 304 / 305 |
| R10 in the direct mapping | H at isoindolinone position 4 | Supported match | 294 / 295 |
| R11/R14 ring C | Five-membered N-containing fused ring across isoindolinone 3a-7a | Supported ring-size and connectivity match | 294 / 295 |
| Lactam carbonyl and ring-N location | Isoindolin-1-one, with N between carbonyl C1 and methylene C3 | Explicitly supported fused-ring alternative, third drawing in the first row of claims 4 and 10 | 297 / 298; 304 / 305 |
| Lactam N side chain | N-CH(CH3)-cyclopropyl; compatible candidate assignment R15 = the two-carbon alkyl segment, R16 = cyclopropyl | Compatible with the alkyl/cycloalkyl options and broad substituted-alkyl definition; not a separate exclusion asserted by this audit | 294 / 295; 305 / 306; definitions 115 / 116 |
| R12/R13 in that candidate assignment | Absent when ring C uses the R15/R16 side chain | Expressly permitted absence branch | 294 / 295; 305 / 306 |
| BLU's 7-cyclopropylmethoxy group | O-CH2-cyclopropyl attached to b4/R8 in the fusion-compatible mapping | **Specific mismatch under the explicit variables:** no external substituent variable drawn at R8; **interpretation unresolved** under the broad aryl definition | 293-294 / 294-295; 116-117 / 117-118 |
| S configuration | Defined S stereocenter in the lactam N side chain | No stereo-based exclusion established: specification allows pure enantiomers and mixtures | 119 / 120; JCI name 13 / 13 |
| Intended medical use | C2beta inhibition in XLMTM | Relevant use overlap, conditional on satisfying the chemical claim; not evidence of clinical efficacy | 307-308 / 308-309; disease description 115 / 116 |

The ether is a compatible **chemical class** under the patent's broad alkoxy definition. Its attachment **position** is the issue. Similarly, cyclopropyl-substituted alkyl and a pure S stereoisomer are not reliable escape arguments. No negative conclusion here depends on treating the genus as exclusively six-membered tetrahydroquinolines, exclusively sulfonamides, racemic-only or restricted to the numbered examples.

## 4. Complete claim-branch check

The substantive structure starting points are **claim 1, Formula 1 for medical use**, and **claim 10, Formula 2 as a compound**. Claim 11 expressly depends on claim 10; it is not an independent route around claim 10's chemical requirements. Claims 15 and 16 introduce composition/method categories but expressly incorporate earlier claimed compounds. [B12-CS01]

| Claims | Published branch and dependencies | Consequence for exact BLU | Printed / physical pages |
|---|---|---|---|
| **1** | Formula 1 medical-use genus; broad A, B-variable, side-chain and C/D ring options | Primary explicit-variable mapping has the R8 ether mismatch; broad-aryl interpretation remains unresolved | 293-294 / 294-295 |
| **2** | Claim 1 with narrower variable selections | Does not create a new B-ring position or fusion edge | 295-296 / 296-297 |
| **3** | Earlier medical-use claims, Formula 2; R1-R16 referenced back to claim 1 | Fixing the smaller ring does not repair the B mapping | 296-297 / 297-298 |
| **4** | Earlier claims with specified fused C options | Includes the relevant isoindolinone core, but retains the unsupplemented R8 atom in its drawing | 297-298 / 298-299 |
| **5** | Earlier claims with specified fused D option | Wrong fusion-edge relationship to the thiazole anchor for BLU | 298 / 299 |
| **6** | Earlier claims with selected R16 groups | Includes cyclopropyl as an option; side-chain choice does not repair the B-ring ether position | 298-299 / 299-300 |
| **7** | Earlier claims, Formula 5 | More specific fused six-membered framework; does not broaden the parent B topology | 299-300 / 300-301 |
| **8** | Earlier claims, Formula 6 | More specific fused/sulfonyl framework; does not broaden the parent B topology | 300 / 301 |
| **9** | Earlier claims, enumerated named compounds | No exact BLU3797 structure/name identified in the enumerated list; the list is not the sole basis for the genus analysis | 300-303 / 301-304 |
| **10** | Independent compound genus, Formula 2, with additional selections and specified B/C alternatives | Thiazole, methyl, acetamide and isoindolinone can match locally. The B-ring R8 ether issue persists in the original drawing; no blanket exclusion based on the title | 303-306 / 304-307 |
| **11** | Claim 10 with specified D ring | Dependent branch; D geometry does not repair BLU's mapping | 306 / 307 |
| **12** | Claims 10 or 11 with selected R16 groups | Includes cyclopropyl, without adding a new R8 substituent variable | 306-307 / 307-308 |
| **13** | Earlier compounds for medicament use in a C2beta-related condition | Incorporates compound requirements; not a claim to every C2beta inhibitor | 307 / 308 |
| **14** | Earlier compounds for specified disease classes, including myopathy, preferably myotubular myopathy | Disease overlap does not remove structural conditions | 307-308 / 308-309 |
| **15** | Pharmaceutical composition containing an earlier claimed compound and acceptable carrier, for the stated medical use | Composition category remains linked to the chemical definitions | 308 / 309 |
| **16** | In vitro modulation method administering an earlier claimed compound or its composition to a cell | The method also remains chemically bounded; no research-use clearance is inferred | 308 / 309 |

Preferred substituent ranges, specific examples and compound47's cleaner single-point panel do not narrow claim 1 by themselves. Conversely, a broad disease description or a functional statement about C2beta inhibition does not, in the published claims read here, replace the required compound definition. Formula 1a and other descriptive embodiments do not appear as an additional standalone claim among the 16 published claims.

## 5. Strongest counterargument and the precise unresolved question

The specification defines aryl to include benzene and allows substituents including alkoxy, at **printed p.116 / physical p.117, first paragraph**. On that broader reading, one could argue that B's carbon-based aromatic ring admits the extra ether even though R8 has no separate substituent label. That is a real primary-text argument and must accompany any report of the drawing mismatch.

The counterweight is the formula's explicit positional drafting. R7 carries a separate R10 variable; R11 and R14 have declared attachment sites and prescribed closure alternatives; R8 and R9 are specified only as C or N. The optional-substitution passage at **printed p.117 / physical p.118, lines 24-33** applies its listed options where an optional substituent is recited. Claim 10 and the explicit isoindolinone drawings preserve the same R8 representation. A permissive chemical definition is therefore not automatically an instruction to add a new substituent position to every drawn atom.

**The unresolved question is whether the general aryl definition is incorporated so as to authorize alkoxy at R8 in these formula claims, despite the explicit positional variables.** The audit records the structural facts and both readings. It does not adjudicate legal construction, prosecution effects or equivalents. An amendment, authoritative examination/prosecution interpretation, or jurisdiction-specific claim text/drawing explicitly addressing that position could change the conclusion. Merely re-reading the patent title, finding an isoindolinone example, or showing that cyclopropylmethoxy is an alkoxy group would not resolve it.

## 6. Decision use and stopping rule

The completed output is a finite structure-to-claim comparison for the selected WO publication. It supports three practical corrections:

1. Keep exact-BLU qualification scientifically actionable under the existing recommendation, without calling a research plan legal clearance.
2. Describe this family's exact-BLU relationship as **an explicit-position mismatch with unresolved broader-definition construction**, rather than unqualified inclusion or exclusion.
3. Preserve independent data value, exact-molecule ownership and successor rights as separate questions. A useful assay or function/exposure result does not become an owned compound through this mapping.

Reopen this selected mapping only for changed or newly recovered claim text/drawings, a material construction/prosecution source, an identified alternative full atom correspondence, or a different exact article. National-branch status and publication comparison are handled separately in Round 12; no national drawing identity or enforceable-claim status is certified by this file. No origin-family search was conducted in this workstream. The precursor families, other target-use families and rights to any future analogue remain outside the chart. No new scientific gate, score increase, human dose or clinical benefit claim follows.

## Sources and provenance

- **B12-CS01 - WO2025003330A1, PCT/EP2024/068134, published 2 January 2025.** [Published patent text](https://patents.google.com/patent/WO2025003330A1/en) and [original PDF](https://patentimages.storage.googleapis.com/0c/02/82/d70291e8e8f99d/WO2025003330A1.pdf). Original PDF SHA-256: `4862b6b3d24e135e200ef57c23276c68c9b38ee6f1fb0d8041150f60b316fe23`; 319 physical pages. Primary drawings and definition pages cited above were inspected locally; the HTML claim text was reopened to cross-check navigation. The original document was already available from prior rounds; the new contribution is this exact-structure mapping. No full patent copy is added to the repository.
- **B12-CS02 - Shearer et al., JCI Insight, DOI 10.1172/jci.insight.198568.** [Primary article](https://insight.jci.org/articles/view/198568) and [publisher v2 PDF](https://df6sxcketz7bb.cloudfront.net/manuscripts/198000/198568/jci.insight.198568.v2.pdf), Figure 1A on p.3 and exact compound name on p.13. Cached publisher PDF SHA-256: `b4fc9d50ec0b383bfd97f5e19247b9a67a5ecad0d7595cf626944181be781566`. Exact identity is carried forward and visually reconfirmed; no synthetic procedure or experiment is proposed here.

The companion JSON separates observed claim text/drawings, analyst atom correspondence, alternative interpretation and decision boundaries. It makes no finding of freedom to operate.
