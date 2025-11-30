# Reaction Yield Prediction – Buchwald–Hartwig Baseline

This repository implements a **clean baseline machine learning workflow** for predicting chemical reaction yields, using the well-known **Buchwald–Hartwig amination** dataset from Dreher & Doyle (*Science, 2018*).

The focus is on building a **fully reproducible ML pipeline** combining:

- RDKit for chemical featurization  
- Morgan fingerprints for reaction descriptors  
- Random Forest regression as the baseline model  
- The official `rxn_yields` open dataset package  

---

## 📁 Repository structure

reaction-yield-ml/
│
├── data/
│ ├── Dreher_and_Doyle_input_data.xlsx ← real BH dataset
│ └── reactions_small.csv ← tiny toy dataset (optional)
│
├── notebooks/
│ └── 01_eda_and_baseline.ipynb ← main notebook
│
├── rxn_yields/ ← cloned external dataset repo
│ └── rxn_yields/data.py ← generate_buchwald_hartwig_rxns()
│
├── src/ ← (optional) custom utilities
│
├── requirements.txt
└── README.md

yaml
Copy code

---

## 🚀 What this project does

### 1. **Loads the Dreher & Doyle Buchwald–Hartwig dataset**  
The raw Excel data contains “Ligand / Additive / Base / Aryl halide / Output (%)”.

### 2. **Converts reaction components → reaction SMILES**  
Using `generate_buchwald_hartwig_rxns()` from the official `rxn_yields` library.

This produces canonical reaction SMILES such as:

[Reactants]>>[Products]

markdown
Copy code

### 3. **Featurizes reactions using Morgan fingerprints (RDKit)**  
Circular fingerprints encode substructures in the reactants:

- radius = 2  
- size = 2048 bits  

These act as the ML model’s input features.

### 4. **Trains a Random Forest regressor (baseline)**

The baseline pipeline:

- 80/20 train/test split  
- 300 trees  
- R² and MAE evaluation  

Typical results on the BH dataset:

MAE: ~4–6
R²: 0.85–0.95 (depending on split and sheet)

yaml
Copy code

### 5. **Computes feature importance**  
We inspect which fingerprint bits matter the most.

---

## 🔧 Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
Ensure RDKit is installed (the notebook already handles errors):

bash
Copy code
pip install rdkit
📓 Running the notebook
The main workflow is in:

Copy code
notebooks/01_eda_and_baseline.ipynb
Run all cells.
You’ll see:

Reaction SMILES generation

Fingerprint construction

Model training

MAE / R² metrics

Feature importance plot

📈 Future extensions
This repo can easily be extended to include:

RXNBERT reaction fingerprints

Graph neural networks (D-MPNN)

Hyperparameter optimization

Multi-task learning

Uncertainty estimation

Custom ML pipelines for other reaction types