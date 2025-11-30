# src/features.py
import pandas as pd
from pathlib import Path
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def load_reaction_data(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)

def encode_features(df: pd.DataFrame):
    y = df["yield_percent"].values

    numeric_cols = ["temperature_C", "time_h"]  # adjust to match cols you actually have
    cat_cols = [c for c in df.columns if c not in numeric_cols + ["yield_percent"]]

    X_numeric = df[numeric_cols]
    X_cat = df[cat_cols]

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", "passthrough", numeric_cols),
            ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
        ]
    )

    # Return transformed X and the fitted preprocessor so we can reuse
    X = preprocessor.fit_transform(df)
    return X, y, preprocessor
