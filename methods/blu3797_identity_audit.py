#!/usr/bin/env python3
"""Round8 arithmetic-only BLU audit. No empirical chemistry or exposure results."""
import json
import argparse
from pathlib import Path
avg={'C':12.011,'H':1.008,'N':14.007,'O':15.999,'S':32.06,'F':18.998403163,'Br':79.904,'Cl':35.45}
mono={'C':12.,'H':1.00782503223,'N':14.00307400443,'O':15.99491461957,'S':31.9720711744,'F':18.99840316273,'Br':78.9183376,'Cl':34.968852682}
proton=1.007276466621
def mass(f,w):return sum(w[k]*v for k,v in f.items())
formulas={
 'BLU3797_neutral':{'C':23,'H':27,'N':3,'O':3,'S':1},
 'fluoro_isoindolinone_junction':{'C':13,'H':13,'Br':1,'F':1,'N':1,'O':1},
 'cyclopropylmethoxy_bromo_intermediate':{'C':17,'H':20,'Br':1,'N':1,'O':2},
 'US_4_bromo_2_fluorobenzoic_acid':{'C':7,'H':4,'Br':1,'F':1,'O':2},
 'US_S_cyclopropylethyl_fluorobenzamide':{'C':12,'H':13,'Br':1,'F':1,'N':1,'O':1},
 'CN_4_bromo_2_fluoro_6_methylbenzoic_acid':{'C':8,'H':6,'Br':1,'F':1,'O':2},
 'CN_A_1_1a_methyl_ester':{'C':9,'H':8,'Br':1,'F':1,'O':2},
 'CN_A_1_1b_bromomethyl_ester':{'C':9,'H':7,'Br':2,'F':1,'O':2},
 'S_cyclopropylethylamine_hydrochloride':{'C':5,'H':12,'Cl':1,'N':1}}
rows={k:{'formula_counts':v,'average_mw_g_mol':mass(v,avg),'monoisotopic_neutral_da':mass(v,mono),'calculated_M_plus_H_mz':None if 'hydrochloride' in k else mass(v,mono)+proton,'status':'formula-derived, not measured'}for k,v in formulas.items()}
blu=425.55
j=mass(formulas['fluoro_isoindolinone_junction'],avg)
calc={
 'JCI_final_isolated_mass_mg':21.7,'JCI_stated_start_mmol':0.114,'JCI_stated_yield_pct':38,
 'JCI_mass_based_yield_pct':21.7/(0.114*blu)*100,
 'JCI_mass_predicted_if_38pct_mg':.114*blu*.38,
 'JCI_implied_mass_fraction_if_38pct_and_no_form_change':(.114*blu*.38)/21.7,
 'JCI_listed_nonexchangeable_proton_integration':sum([1,1,2,2,1,3,3,4,1,3,1,3,1]),
 'US_acid_reported_mmol':18.4,'US_6g_acid_formula_mmol':6000/mass(formulas['US_4_bromo_2_fluorobenzoic_acid'],avg),
 'US_6g_amide_formula_mmol':6000/mass(formulas['US_S_cyclopropylethyl_fluorobenzamide'],avg),
 'CN_10g_starting_acid_formula_mmol':10000/mass(formulas['CN_4_bromo_2_fluoro_6_methylbenzoic_acid'],avg),
 'CN_13_05g_A1_1b_formula_mmol':13050/mass(formulas['CN_A_1_1b_bromomethyl_ester'],avg),
 'CN_4_87g_S_amine_HCl_formula_mmol':4870/mass(formulas['S_cyclopropylethylamine_hydrochloride'],avg),
 'CN_3_17g_junction_formula_mmol':3170/j,
 'CN_final_over_42_91mmol_start_nominal_pct':(3170/j)/42.91*100,
 'CN_final_over_40_04mmol_last_step_nominal_pct':(3170/j)/40.04*100,
 'CN_final_over_start_corrected_only_for_13_05_of_13_5g_aliquot_pct':(3170/j)/(42.91*13.05/13.5)*100,
 'JCI_nominal_enzyme_nM':60,'JCI_nominal_half_enzyme_nM':30,'JCI_nominal_lipid_nM':150,
 'JCI_nominal_substrate_per_enzyme':150/60,
 'JCI_max_productive_ADP_as_fraction_of_1mM_ATP_pct':150/1000000*100,
 'JCI_reported_cell_IC50_nM':68.2,
 'JCI_reported_cell_IC50_as_neutral_ng_mL':68.2*blu/1000,
 'JCI_myotube_nuclear_peak_nominal_nM':188,
 'JCI_myotube_nuclear_peak_as_neutral_ng_mL':188*blu/1000
}
out={'version':'round8','classification':'arithmetic audit only; no experimental data','assumptions':['Formulas are neutral named structures, unless explicitly hydrochloride.','Average masses use stated rounded standard atomic weights.','HRMS target is calculated, not journal-observed.','Yield calculations assume named neutral material, stated precursor amounts, no purity correction and no unexplained form.','CN crude carryforward and aliquot prevent definitive mass-balance/yield reconstruction.','150 nM lipid is retained exactly as journal printed, not corrected to micromolar.','68.2nM and188nM remain nominal published cell concentrations; conversions do not establish free exposure.'], 'atomic_weights_used':avg,'monoisotopic_masses_used':mono,'proton_mass_used':proton,'identity_references':rows,'calculations':calc}
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--out','--output',type=Path,default=Path(__file__).with_name('blu_identity_numeric_audit.json'),help='Destination for the deterministic audit JSON.')
args=parser.parse_args()
args.out.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
