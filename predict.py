# predict.py
import joblib
import pandas as pd

# Load artifact
ARTIFACT = "artifact.pkl"
art = joblib.load(ARTIFACT)
 
model = art['model']
FEATURES = art['features']
TARGET = art['target']

def predict_from_df(df):
    """
    df: pandas DataFrame with all FEATURES columns
    Returns predictions
    """
    X = df[FEATURES]  # select only training columns
    preds = model.predict(X)
    return preds

# Optional debug
if __name__ == "__main__":
    sample_df = pd.DataFrame([dict(zip(FEATURES, [0]*len(FEATURES)))])
    print("Sample prediction:", predict_from_df(sample_df))