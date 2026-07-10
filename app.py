import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/employee_income_model.pkl")

st.set_page_config(page_title="Employee Income Predictor", page_icon="💼")

st.title("💼 Employee Income Predictor")
st.write("Predict whether a person's annual income is <=50K or >50K.")

st.info("In the next step, we'll connect this interface to your model with the correct input fields.")
