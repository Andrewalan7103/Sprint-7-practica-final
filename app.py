import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración inicial
st.set_page_config(page_title="Análisis de Vehículos", layout="wide")

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Extraer fabricantes de la columna 'model' (primera palabra)
car_data['manufacturer'] = car_data['model'].str.split().str[0]

# Primera sección: Data viewer
st.header("Data viewer")

# Filtro
include_less_than_1000 = st.checkbox("Include models with less than 1000 ads")
if include_less_than_1000:
    filtered_data = car_data.groupby('model').filter(lambda x: len(x) < 1000)
else:
    filtered_data = car_data

# Mostrar tabla
st.dataframe(filtered_data.head(10))

# Gráfico apilado
st.subheader("Vehicle types by model")
fig1 = px.histogram(filtered_data, x="model", color="type", barmode="stack", title="Vehicle types by model")
st.plotly_chart(fig1)

# Segunda sección: Comparación de precios
st.header("Compare price distribution between manufacturers")

# Selectores para elegir dos fabricantes
manufacturer1 = st.selectbox("Select manufacturer 1", options=filtered_data['manufacturer'].unique(), index=0)
manufacturer2 = st.selectbox("Select manufacturer 2", options=filtered_data['manufacturer'].unique(), index=1)

# Filtro por fabricantes seleccionados
data_compare = filtered_data[filtered_data['manufacturer'].isin([manufacturer1, manufacturer2])]

# Opción de normalizar histograma
normalize = st.checkbox("Normalize histogram")

# Gráfico de comparación de precios
if normalize:
    fig2 = px.histogram(data_compare, x="price", color="manufacturer", barmode="overlay", histnorm="probability density", title=f"Price distribution: {manufacturer1} vs {manufacturer2}")
else:
    fig2 = px.histogram(data_compare, x="price", color="manufacturer", barmode="overlay", title=f"Price distribution: {manufacturer1} vs {manufacturer2}")

st.plotly_chart(fig2)