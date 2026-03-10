import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')
st.header('Análisis de anuncios de vehículos')
hist_button = st.button('Crear histograma')
if hist_button:
    st.write('Creación de un histograma para el kilometraje de los vehículos')

    fig = px.histogram(df, x="odometer")

    st.plotly_chart(fig)