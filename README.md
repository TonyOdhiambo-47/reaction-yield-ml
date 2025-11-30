# Reaction Yield Prediction – Buchwald–Hartwig Baseline

This repository implements a **clean baseline machine learning workflow** for predicting chemical reaction yields, using the well-known **Buchwald–Hartwig amination** dataset from Dreher & Doyle (*Science, 2018*).

The focus is on building a **fully reproducible ML pipeline** combining:

- RDKit for chemical featurization  
- Morgan fingerprints for reaction descriptors  
- Random Forest regression as the baseline model  
- The official `rxn_yields` open dataset package  

---

## What this project does

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