
from pypmml import Model
import streamlit as st
import pandas as pd

# Laad het PMML-model
model = Model.load('Titanic_test.pmml')

st.title("Titanic Overlevingsvoorspeller")

# Invoervelden (pas aan op je PMML features)
pclass = st.selectbox('Klasse', [1, 2, 3])
sex = st.selectbox('Geslacht', ['male', 'female'])
age = st.number_input('Leeftijd', min_value=0.0, max_value=100.0, value=30.0)
fare = st.number_input('Fare', min_value=0.0, value=7.25)

input_df = pd.DataFrame([{
    'pclass': pclass,
    'sex': sex,
    'age': age,
    'fare': fare
}])

if st.button("Voorspel"):
    prediction = model.predict(input_df)
    st.write("Voorspelling:", prediction)
