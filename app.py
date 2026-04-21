import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("Model (1).pkl", "rb"))

st.set_page_config(page_title="ML App")

st.title("🚀 Prediction App")

st.write("Enter valid details below:")

# Example Inputs (modify as per your model)

# Age (only positive)
age = st.number_input("Enter Age", min_value=0, max_value=120, step=1)

# Salary (only positive)
salary = st.number_input("Enter Salary", min_value=0.0)

# Gender (categorical - no negative issue)
gender = st.selectbox("Select Gender", ["Male", "Female"])

# Convert Gender to numeric (important!)
if gender == "Male":
    gender_val = 1
else:
    gender_val = 0

# Predict
if st.button("Predict"):
    input_data = np.array([[age, salary, gender_val]])
    prediction = model.predict(input_data)

    st.success(f"Prediction: {prediction[0]}")
