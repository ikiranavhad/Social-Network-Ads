import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open("Model (1).pkl", "rb"))

# App title
st.title("🚀 ML Model Deployment App")
st.write("Enter input values to get prediction")

# Example: 3 input features (change as per your model)
feature1 = st.number_input("Enter Feature 1")
feature2 = st.number_input("Enter Feature 2")
feature3 = st.number_input("Enter Feature 3")

# Predict button
if st.button("Predict"):
    input_data = np.array([[feature1, feature2, feature3]])
    prediction = model.predict(input_data)

    st.success(f"Prediction: {prediction[0]}")
