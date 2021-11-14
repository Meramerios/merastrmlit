import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
### Shown are the stock closing price and volume of Google,KING and TESLA!
meramerios
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = st.selectbox('company',['ATVI','GOOGL','TSLA'])
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2019-5-31', end='2021-09-30')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
