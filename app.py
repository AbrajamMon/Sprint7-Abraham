import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
st.header("Venta de vehiculos")  # encabezado

car_data['date_posted'] = pd.to_datetime(
    # convertir a fecha 'date_posted'
    car_data['date_posted'], format='%Y-%m-%d').dt.date

car_data['brand'] = car_data['model'].str.split().str[0]  # agregar 'brand'

st.subheader("Vehiculos recien agregados")  # subencabezado

st.write(car_data.sort_values(by='date_posted',
         # mostrar los ultimos vehiculos agregados
                              ascending=False).reset_index(drop=True))

# checkbox para diagrama de dispersion
scatter_checkbox = st.checkbox("Diagrama de dispersión")

if scatter_checkbox:  # mostrar diagrama de dispersion
    st.write("Diagrama de dispersión")
    fig = px.scatter(car_data, x='odometer', y='price', color='brand')
    st.plotly_chart(fig, use_container_width=True)
