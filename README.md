# reaction-yield-ml

Tiny playground for predicting reaction yields with machine learning.

## What this repo does

- Loads a CSV of reaction conditions (`data/reactions_small.csv`)
- Encodes simple descriptors like temperature, time, and reaction type
- Trains a baseline random forest regressor to predict `yield_percent`
- Evaluates the model with MAE and R²
- Explores the data and model behavior in `notebooks/01_eda_and_baseline.ipynb`

## Getting started

```bash
git clone git@github.com:TonyOdhiambo-47/reaction-yield-ml.git
cd reaction-yield-ml
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python -m src.train_baseline
