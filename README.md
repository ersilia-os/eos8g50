# FASTSOLV solubility prediction

Prediction of organic solubility using deep learning on fixed Mordred-based representations. The authors test the models under rigorous solute extrapolation conditions, outperforming existing methods and demonstrating prediction accuracy near the intrinsic aleatoric limit of experimental data.

This model was incorporated on 2025-08-27.Last packaged on 2025-09-02.

## Information
### Identifiers
- **Ersilia Identifier:** `eos8g50`
- **Slug:** `fastsolv`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Solubility`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `15`
- **Output Consistency:** `Fixed`
- **Interpretation:** Array of predicted log-scale solubility values in 15 organic solvents (all ASKOS organic solvents) for each input compound.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| solubility_methanol | float | high | Predicted solubility (log mol/L) in Methanol at 298 K |
| solubility_ethanol | float | high | Predicted solubility (log mol/L) in Ethanol at 298 K |
| solubility_isopropanol | float | high | Predicted solubility (log mol/L) in Isopropanol at 298 K |
| solubility_acetic_acid | float | high | Predicted solubility (log mol/L) in Acetic acid at 298 K |
| solubility_acetonitrile | float | high | Predicted solubility (log mol/L) in Acetonitrile at 298 K |
| solubility_acetone | float | high | Predicted solubility (log mol/L) in Acetone at 298 K |
| solubility_isobutyl_methyl_ketone | float | high | Predicted solubility (log mol/L) in Isobutyl methyl ketone at 298 K |
| solubility_isopropyl_acetate | float | high | Predicted solubility (log mol/L) in Isopropyl acetate at 298 K |
| solubility_tetrahydrofuran | float | high | Predicted solubility (log mol/L) in Tetrahydrofuran at 298 K |
| solubility_tert_butyl_methyl_ether | float | high | Predicted solubility (log mol/L) in tert-Butyl methyl ether at 298 K |

_10 of 15 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos8g50](https://hub.docker.com/r/ersiliaos/eos8g50)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8g50.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8g50.zip)

### Resource Consumption
- **Model Size (Mb):** `878`
- **Environment Size (Mb):** `1850`
- **Image Size (Mb):** `4342.76`

**Computational Performance (seconds):**
- 10 inputs: `34.02`
- 100 inputs: `259.06`
- 10000 inputs: `-1`

### References
- **Source Code**: [https://github.com/JacksonBurns/fastsolv](https://github.com/JacksonBurns/fastsolv)
- **Publication**: [https://www.nature.com/articles/s41467-025-62717-7](https://www.nature.com/articles/s41467-025-62717-7)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2025`
- **Ersilia Contributor:** [arnaucoma24](https://github.com/arnaucoma24)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos8g50
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos8g50
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
