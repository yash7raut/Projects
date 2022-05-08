from tracemalloc import start
import pandas as pd
import yfinance as yf
import streamlit as st

st.write("""
### Simple stock Price App

Shown is the **closing price** and ***volume*** of TCS!

""")

tickersymbol = "TCS.NS"

tickerData = yf.Ticker(tickersymbol)

tickerdf = tickerData.history(period='1d', start='2010-01-01', end='2022-04-19')

st.write("""
### Stock price
""")

st.line_chart(tickerdf.Close)

st.write("""
### Volume price
""")

st.line_chart(tickerdf.Volume)
