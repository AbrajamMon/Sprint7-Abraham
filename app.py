import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
st.header("Venta de vehiculos")

car_data['date_posted'] = pd.to_datetime(
    car_data['date_posted'], format='%Y-%m-%d')
