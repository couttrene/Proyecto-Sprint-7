import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Título y encabezado principal de la aplicación web
st.header('Cuadro de Mandos: Análisis de Anuncios de Venta de Coches')

# Leer el conjunto de datos
car_data = pd.read_csv('vehicles_us.csv')

# --- SECCIÓN 1: HISTOGRAMA ---
# Crear un botón para el histograma
hist_button = st.button('Construir histograma')

if hist_button:
    # Mensaje informativo
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear histograma con Plotly
    fig_hist = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Personalizar diseño
    fig_hist.update_layout(
        title_text='Distribución del Odómetro',
        xaxis_title='Kilometraje (Odómetro)',
        yaxis_title='Cantidad de Vehículos'
    )

    # Mostrar el gráfico interactivo en Streamlit
    st.plotly_chart(fig_hist, use_container_width=True)

# --- SECCIÓN 2: GRÁFICO DE DISPERSIÓN ---
# Crear un botón para el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    # Mensaje informativo
    st.write('Creación de un gráfico de dispersión: Precio vs. Odómetro')

    # Crear gráfico de dispersión con Plotly
    fig_scatter = go.Figure(data=[go.Scatter(
        x=car_data['odometer'],
        y=car_data['price'],
        mode='markers',
        marker=dict(opacity=0.5)
    )])

    # Personalizar diseño
    fig_scatter.update_layout(
        title_text='Relación entre Precio y Odómetro',
        xaxis_title='Kilometraje (Odómetro)',
        yaxis_title='Precio (USD)'
    )

    # Mostrar el gráfico interactivo en Streamlit
    st.plotly_chart(fig_scatter, use_container_width=True)
