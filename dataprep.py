# dataprep.py
import pandas as pd

def load_data(path):
    """Load CSV data into a DataFrame"""
    return pd.read_csv(path)

def basic_clean(df):
    """Perform basic cleaning: fill missing values, remove duplicates"""
    df = df.copy()
    df = df.drop_duplicates()
    df = df.fillna(0)
    return df
 
def feature_engineer(df):
    """
    Add feature engineering here if needed.
    Returns df and target column name
    """
    df = df.copy()
    # Ensure target column exists
    target_col = "EnergyConsumption"
    # Example: create features if needed
    # df['feature_x'] = df['some_column'] * 2
    return df, target_col

def get_train_val(df, val_frac=0.2, random_state=42):
    """Split df into train and validation"""
    df = df.sample(frac=1, random_state=random_state).reset_index(drop=True)
    n_val = int(len(df) * val_frac)
    val = df.iloc[:n_val]
    train = df.iloc[n_val:]
    return train, val