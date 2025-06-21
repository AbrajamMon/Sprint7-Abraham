import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header("Vehiculos en venta")

# Convertir la columa 'date_posted' al formato de fecha
car_data['date_posted'] = pd.to_datetime(
    car_data['date_posted'], format='%Y-%m-%d').dt.date

# Agregar la columna 'brand' extrayendo al primer palabra de 'model'
car_data['brand'] = car_data['model'].str.split().str[0]

# Mostrar el Dataframe
st.dataframe(car_data, hide_index=True, column_config={
             "price": st.column_config.NumberColumn(format="$%d"),
             "odometer": st.column_config.NumberColumn(format="%dkm")})

# Checkbox, muestra diagrama de dispersion model_year vs price, color por brand
scatter_checkbox = st.checkbox("Ver diagrama de dispersión")

if scatter_checkbox:
    st.write("Diagrama de dispersión")
    fig = px.scatter(car_data, x='model_year', y='price', color='brand')
    st.plotly_chart(fig, use_container_width=True)

# Checkbox, muestra histograma de precio, color por type
hist_checkbox = st.checkbox("Ver histograma")

if hist_checkbox:
    st.write("Histograma de precios")
    fig = px.histogram(car_data, x='price', color='type')
    st.plotly_chart(fig, use_container_width=True)

# Checkbox, muestra grafico de barras por type, coloreado por brand
bar_checkbox = st.checkbox("Tipo de vehiculo por marca")

if bar_checkbox:
    st.write("Tipo de vehiculo por marca")
    fig = px.bar(car_data, x='type', color='brand')
    st.plotly_chart(fig, use_container_width=True)

# Boton, muestra histograma de days_listed, coloreado por condition
days_listed_button = st.button("Precio vs Dias publicado")

if days_listed_button:
    st.write("Grafico de linea")
    fig = px.histogram(car_data, x='days_listed', color='condition')
    st.plotly_chart(fig, use_container_width=True)
