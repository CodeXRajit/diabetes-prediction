import streamlit as st
import pickle
import numpy as np

with open('diabetes_model_2.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Diabetes Prediction App")

st.write("Enter the following information to check diabetes risk:")

pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, step=1)
glucose = st.number_input("Glucose", min_value=0, max_value=300)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=150)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100)
insulin = st.number_input("Insulin", min_value=0, max_value=900)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, format="%.1f")
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, format="%.3f")
age = st.number_input("Age", min_value=1, max_value=120, step=1)

if st.button("Predict"):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                            insulin, bmi, dpf, age]])
    
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("The model predicts that you may have diabetes.")
    else:
        st.success("The model predicts that you are not diabetic.")
