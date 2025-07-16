import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración inicial
st.set_page_config(page_title="Análisis de Vehículos", layout="wide")

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header("Data viewer")

# Filtro
include_less_than_1000 = st.checkbox("Include manufacturers with less than 1000 ads")
if include_less_than_1000:
    filtered_data = car_data.groupby('manufacturer').filter(lambda x: len(x) < 1000)
else:
    filtered_data = car_data

# Mostrar tabla
st.dataframe(filtered_data.head(10))

# Gráfico apilado
st.subheader("Vehicle types by manufacturer")
fig = px.histogram(filtered_data, x="manufacturer", color="type", barmode="stack", title="Vehicle types by manufacturer")
st.plotly_chart(fig)

# Opcional: Casillas de verificación como desafío extra
st.subheader("Opciones con Casillas de Verificación")
if st.checkbox("Generar Histograma"):
    fig_hist = px.histogram(car_data, x="odometer")
    st.write("Histograma de Odometer")
    st.plotly_chart(fig_hist)

if st.checkbox("Generar Gráfico de Dispersión"):
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Odometer vs Price")
    st.write("Gráfico de Dispersión: Odometer vs Price")
    st.plotly_chart(fig_scatter)