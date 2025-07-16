import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos (asumiendo que ya está en app.py)
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header("Análisis de Datos de Vehículos")

# Botón para histograma
if st.button("Mostrar Histograma"):
    fig_hist = px.histogram(car_data, x="odometer")
    st.write("Histograma de Odometer")
    st.plotly_chart(fig_hist)

# Botón para gráfico de dispersión
if st.button("Mostrar Gráfico de Dispersión"):
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Odometer vs Price")
    st.write("Gráfico de Dispersión: Odometer vs Price")
    st.plotly_chart(fig_scatter)

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