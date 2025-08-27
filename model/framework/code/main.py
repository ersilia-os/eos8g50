# imports
import os
import sys
import csv
import pandas as pd
from fastsolv.fastsolv.fastsolv import fastsolv

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# Load solvents
SOLVENTS = pd.read_csv(os.path.join(root, "..", "..", "checkpoints", 'solvents.csv'))
solvent_names = ["solubility_" + i.lower().replace(" ", "_") for i in SOLVENTS['name'].tolist()]
solvent_smiles = SOLVENTS['smiles'].tolist()
TEMPERATURE = 298

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

output = []
for smiles in smiles_list:

    # Calculate solubility for all solvents
    data = dict(solvent_smiles=solvent_smiles, solute_smiles=[smiles] * len(solvent_smiles), temperature=[TEMPERATURE] * len(solvent_smiles))
    df = fastsolv(pd.DataFrame(data)).reset_index()

    # Assert solvent order is the same
    assert solvent_smiles == df['solvent_smiles'].tolist()
    output.append(df["predicted_logS"].tolist())

# To pandas and write file
outputs = pd.DataFrame(output, columns=solvent_names)
outputs.to_csv(output_file, index=False)
