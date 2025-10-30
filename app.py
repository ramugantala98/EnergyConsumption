# app.py
import streamlit as st
import pandas as pd
import joblib
from predict import predict_from_df, TARGET, FEATURES

st.title("Citizen Energy — Energy Consumption Predictor")
st.markdown("Predict next-hour energy consumption (one-step ahead).")
 
# Load artifact
artifact = joblib.load("artifact.pkl")
features = artifact['features']

# --- File upload ---
uploaded = st.file_uploader("Upload recent data (CSV) with feature columns only", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)

    # Drop target column if present
    if TARGET in df.columns:
        df = df.drop(columns=[TARGET])

    # Convert categorical columns to numeric
    for col in ['HVACUsage', 'LightingUsage', 'Holiday']:
        if col in df.columns:
            df[col] = df[col].map({'yes': 1, 'no': 0})

    # Convert DayOfWeek to numeric (0=Sunday, 6=Saturday)
    if 'DayOfWeek' in df.columns:
        day_map = {'Sunday': 0, 'Monday': 1, 'Tuesday': 2, 'Wednesday': 3,
                   'Thursday': 4, 'Friday': 5, 'Saturday': 6}
        df['DayOfWeek'] = df['DayOfWeek'].map(day_map)

    # Ensure all features are present
    missing = [f for f in features if f not in df.columns]
    if missing:
        st.error(f"Missing feature columns: {missing}")
        st.stop()

    df = df[features]  # reorder features
    st.write("Preview of input data:", df.head())

    try:
        preds = predict_from_df(df)
        df['predicted_'+TARGET] = preds
        st.write("Predictions:", df[['predicted_'+TARGET]])
        st.line_chart(df[['predicted_'+TARGET]])
    except Exception as e:
        st.error(f"Prediction error: {e}")

# --- Manual input ---
else:
    st.info("Or enter features manually for a single prediction.")
    manual = {}

    # Categorical inputs
    manual['HVACUsage'] = 1 if st.selectbox("HVAC Usage", ["Yes", "No"]) == "Yes" else 0
    manual['LightingUsage'] = 1 if st.selectbox("Lighting Usage", ["Yes", "No"]) == "Yes" else 0
    manual['Holiday'] = 1 if st.selectbox("Holiday", ["Yes", "No"]) == "Yes" else 0
    manual['DayOfWeek'] = st.selectbox("Day of Week", ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"])
    # Convert DayOfWeek to numeric
    day_map = {'Sunday':0,'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6}
    manual['DayOfWeek'] = day_map[manual['DayOfWeek']]

    # Numeric inputs for any remaining features
    for f in features:
        if f not in manual:
            manual[f] = st.number_input(f, value=0.0, format="%.3f")

    if st.button("Predict"):
        dfm = pd.DataFrame([manual])
        try:
            preds = predict_from_df(dfm)
            st.success(f"Predicted {TARGET}: {preds[0]:.3f}")
        except Exception as e:
            st.error(f"Prediction failed: {e}")