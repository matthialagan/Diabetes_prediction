import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
with open('model_3.pkl', 'rb') as f:
    model = pickle.load(f)

# Title of the app
st.title("Diabetes Prediction App")

# Getting user input
st.header("Enter your details")
gender = st.selectbox("Gender", options=["Male", "Female"], index=0)
age = st.number_input("Age", min_value=1, max_value=100, value=25)
hypertension = st.selectbox("Hypertension", options=["Yes", "No"], index=1)
heart_disease = st.selectbox("Heart Disease", options=["Yes", "No"], index=1)
smoking_history = st.selectbox("Smoking History", options=["Non-Smoker", "Former Smoker", "Current Smoker", "Chain Smoker"], index=0)
bmi = st.number_input("Body Mass Index (BMI)", min_value=0.0, max_value=70.0, value=20.0)
hba1c_level = st.number_input("HbA1c Level", min_value=0.0, max_value=20.0, value=5.0)
blood_glucose_level = st.number_input("Blood Glucose Level", min_value=0, max_value=200, value=120)

# Convert categorical inputs to numerical values
gender = 1 if gender == "Male" else 0
hypertension = 1 if hypertension == "Yes" else 0
heart_disease = 1 if heart_disease == "Yes" else 0
smoking_history_mapping = {"Non-Smoker": 0, "Former Smoker": 1, "Current Smoker": 2, "Chain Smoker": 3}
smoking_history = smoking_history_mapping[smoking_history]

# Collect user input into a dataframe with correct feature names and order
input_data = pd.DataFrame({
    'gender': [gender],
    'age': [age],
    'hypertension': [hypertension],
    'heart_disease': [heart_disease],
    'smoking_history': [smoking_history],
    'bmi': [bmi],
    'HbA1c_level': [hba1c_level],
    'blood_glucose_level': [blood_glucose_level]
})

# Predict diabetes
if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.subheader("Result: The person is likely to have diabetes.")
    else:
        st.subheader("Result: The person is unlikely to have diabetes.")
