
import streamlit as st
import pandas as pd
import pickle

# Laad het model
with open('titanic_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Titanic Overlevingsvoorspeller")

pclass = st.selectbox('Klasse', [1, 2, 3])
sex = st.selectbox('Geslacht', ['male', 'female'])
age = st.number_input('Leeftijd', min_value=0.0, max_value=100.0, value=30.0)
fare = st.number_input('Fare', min_value=0.0, value=7.25)

# Input voorbereiden
input_data = pd.DataFrame([{
    'pclass': pclass,
    'sex': 0 if sex == 'male' else 1,
    'age': age,
    'fare': fare
}])

if st.button("Voorspel"):
    prediction = model.predict(input_data)
    st.write("Voorspelling (0 = overleden, 1 = overleefd):", prediction[0])
