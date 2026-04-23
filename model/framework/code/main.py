# imports
import os
import sys
import csv
import pandas as pd


# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, root)
from fastsolv.fastsolv.fastsolv import fastsolv

# Load solvents
SOLVENTS = pd.read_csv(os.path.join(root, "..", "..", "checkpoints", 'solvents.csv'))
solvent_names = ["solubility_" + i.lower().replace(" ", "_").replace("-", "_") for i in SOLVENTS['name'].tolist()]
solvent_smiles = SOLVENTS['smiles'].tolist()
TEMPERATURE = 298

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

n_solvents = len(solvent_smiles)

# Build a single DataFrame with all solute-solvent combinations and run the
# model once. This avoids recreating the Trainer and recomputing solvent
# descriptors for every compound, which was the main performance bottleneck.
df_all = pd.DataFrame({
    'solute_smiles': [s for s in smiles_list for _ in solvent_smiles],
    'solvent_smiles': solvent_smiles * len(smiles_list),
    'temperature': [TEMPERATURE] * (len(smiles_list) * n_solvents),
})
results = fastsolv(df_all).reset_index()

# Slice results back into per-compound rows (order is preserved by the DataLoader)
predicted = results["predicted_logS"].tolist()
output = [predicted[i * n_solvents:(i + 1) * n_solvents] for i in range(len(smiles_list))]

# To pandas and write file
outputs = pd.DataFrame(output, columns=solvent_names)
outputs.to_csv(output_file, index=False)
