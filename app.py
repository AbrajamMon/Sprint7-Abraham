import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header("Vehiculos en venta")

# Convertir la columa 'date_posted' al formato de fecha
car_data['date_posted'] = pd.to_datetime(car_data['date_posted'],
                                         format='%Y-%m-%d').dt.date

# Agregar la columna 'brand' extrayendo al primer palabra de 'model'
car_data['brand'] = car_data['model'].str.split().str[0]

# Multiselect, filtro para el dataframe por marca
marcas = st.multiselect("Filtrar por marca", car_data['brand'].unique(),
                        default=car_data['brand'].unique())

# Multiselect, filtra el dataframe por type
tipo = st.multiselect("Filtrar por tipo", car_data['type'].unique(),
                      default=car_data['type'].unique())

# Slider, filtrar por precio
precio_min, precio_max = st.slider("Rango de precio", int(car_data['price']. min()),
                                   int(car_data['price'].max()), (25, 40))
# filtrar el dataframe original
car_data_filtrado = car_data[(car_data['brand'].isin(marcas)) &
                             (car_data['type'].isin(tipo)) &
                             (car_data['price'] >= precio_min) &
                             (car_data['price'] <= precio_max)]

# Mostrar el Dataframe filtrado
st.dataframe(car_data_filtrado, hide_index=True, column_config={
             "price": st.column_config.NumberColumn(format="$%d"),
             "odometer": st.column_config.NumberColumn(format="%dkm")})

# Checkbox, muestra diagrama de dispersion model_year vs price, color por brand
scatter_checkbox = st.checkbox(
    "Ver diagrama de dispersión 'Año del modelo vs precio' ")

if scatter_checkbox:
    st.write("Año del modelo vs precio:")
    fig = px.scatter(car_data, x='model_year', y='price', color='brand')
    st.plotly_chart(fig, use_container_width=True)

# Checkbox, muestra histograma de precio, color por type
hist_checkbox = st.checkbox("Ver histograma de precios")

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

# Checkbox, muestra histograma de days_listed, coloreado por condition
days_listed_checkbox = st.checkbox(
    "Ver histograma 'Dias publicado y su condicion'")

if days_listed_checkbox:
    st.write("Numero de dias publicado")
    fig = px.histogram(car_data, x='days_listed', color='condition')
    st.plotly_chart(fig, use_container_width=True)
