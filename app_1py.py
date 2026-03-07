import streamlit as st
import seaborn as sns
import yfinance as yf
import plotly.express as px
df=sns.load_dataset('iris')
st.title('app version _2')
st.write('hola mundo')
name=st.text_input('ingresa tu nombre')
if name:
    st.write(f'hola {name}')
st.dataframe(df)
nombre_archivo=st.text_input("ingresa el symbol (e.g., NVDA, BTC-USD)", "NVDA")
stock = yf.Ticker(nombre_archivo)
df_stock = stock.history(period="1y")
fig = px.line(df_stock)
st.plotly_chart(fig)