import streamlit as st
import pickle
import numpy as np

# Load saved model and scaler
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

st.title("Customer Churn Prediction (Full Features)")

# 1. Get inputs for all features
gender = st.selectbox("Gender", ["Female", "Male"])
senior = st.selectbox("Senior Citizen", ["No", "Yes"])
partner = st.selectbox("Partner", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["No", "Yes"])
tenure = st.slider("Tenure (Months)", 0, 72, 12)

phoneservice = st.selectbox("Phone Service", ["No", "Yes"])
multiplelines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
internetservice = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
onlinesecurity = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
onlinebackup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])
deviceprotection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
techsupport = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
streamingtv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
streamingmovies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
paperlessbilling = st.selectbox("Paperless Billing", ["No", "Yes"])
paymentmethod = st.selectbox("Payment Method", [
    "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
])
monthlycharges = st.number_input("Monthly Charges", min_value=0.0, format="%.2f")
totalcharges = st.number_input("Total Charges", min_value=0.0, format="%.2f")

# 2. Encode input same way as training (label encoding)
def encode_input():
    return [
        1 if gender == "Male" else 0,
        1 if senior == "Yes" else 0,
        1 if partner == "Yes" else 0,
        1 if dependents == "Yes" else 0,
        tenure,
        1 if phoneservice == "Yes" else 0,
        {"No": 0, "Yes": 1, "No phone service": 2}[multiplelines],
        {"DSL": 0, "Fiber optic": 1, "No": 2}[internetservice],
        {"No": 0, "Yes": 1, "No internet service": 2}[onlinesecurity],
        {"No": 0, "Yes": 1, "No internet service": 2}[onlinebackup],
        {"No": 0, "Yes": 1, "No internet service": 2}[deviceprotection],
        {"No": 0, "Yes": 1, "No internet service": 2}[techsupport],
        {"No": 0, "Yes": 1, "No internet service": 2}[streamingtv],
        {"No": 0, "Yes": 1, "No internet service": 2}[streamingmovies],
        {"Month-to-month": 0, "One year": 1, "Two year": 2}[contract],
        1 if paperlessbilling == "Yes" else 0,
        {
            "Electronic check": 0,
            "Mailed check": 1,
            "Bank transfer (automatic)": 2,
            "Credit card (automatic)": 3
        }[paymentmethod],
        monthlycharges,
        totalcharges
    ]

# 3. Predict
if st.button("Predict"):
    input_data = np.array([encode_input()])
    input_scaled = scaler.transform(input_data)
    pred = model.predict(input_scaled)[0]
    result = "Churn" if pred == 1 else "No Churn"
    st.success(f"Prediction: {result}")
