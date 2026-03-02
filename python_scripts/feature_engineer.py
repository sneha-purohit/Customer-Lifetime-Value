import pandas as pd

def preprocess_features(df, features):
    """
    Fill missing values and select relevant features.
    """
    df = df.copy()
    df[features] = df[features].fillna(0)
    return df