import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and scaler
model = joblib.load('knn_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("🍷 Wine Quality Prediction App")

st.markdown("Enter the chemical properties of the wine below:")

# Input fields
fixed_acidity = st.number_input('Fixed Acidity', 0.0, 20.0, 7.4)
volatile_acidity = st.number_input('Volatile Acidity', 0.0, 2.0, 0.7)
citric_acid = st.number_input('Citric Acid', 0.0, 1.0, 0.0)
residual_sugar = st.number_input('Residual Sugar', 0.0, 15.0, 1.9)
chlorides = st.number_input('Chlorides', 0.0, 1.0, 0.076)
free_sulfur_dioxide = st.number_input('Free Sulfur Dioxide', 0.0, 100.0, 11.0)
total_sulfur_dioxide = st.number_input('Total Sulfur Dioxide', 0.0, 300.0, 34.0)
density = st.number_input('Density', 0.9900, 1.0050, 0.9978)
pH = st.number_input('pH', 2.5, 4.5, 3.51)
sulphates = st.number_input('Sulphates', 0.0, 2.0, 0.56)
alcohol = st.number_input('Alcohol', 8.0, 15.0, 9.4)

# Predict button
if st.button('Predict Wine Quality'):
    input_data = np.array([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                            chlorides, free_sulfur_dioxide, total_sulfur_dioxide,
                            density, pH, sulphates, alcohol]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]
    st.success(f"The predicted wine quality is: **{prediction}**")
