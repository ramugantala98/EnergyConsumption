# train.py
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from dataprep import load_data, basic_clean, feature_engineer, get_train_val
import pandas as pd
 
DATA_PATH = "Energy_consumption.csv"
print("test   ")
def main():
    # Load and prepare data
    df = load_data(DATA_PATH)
    df = basic_clean(df)
    df, target_col = feature_engineer(df)  # target_col will be 'EnergyConsumption'

    # Train/val split
    train, val = get_train_val(df)
    # Keep only numeric columns
    FEATURES = [c for c in train.columns if c != target_col and pd.api.types.is_numeric_dtype(train[c])] 
    X_train, y_train = train[FEATURES], train[target_col]
    X_val, y_val = val[FEATURES], val[target_col]

    # Model
    model = RandomForestRegressor(
        n_estimators=200,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    )

    # Train
    model.fit(X_train, y_train)

    # Evaluate
    preds = model.predict(X_val)
    mae = mean_absolute_error(y_val, preds)
    print(f"✅ Validation MAE: {mae:.4f}")

    # Save model artifact
    artifact = {'model': model, 'features': FEATURES, 'target': target_col}
    joblib.dump(artifact, "artifact.pkl")
    print("💾 Saved trained model to artifact.pkl")

if __name__ == "__main__":
    main()