import streamlit as st
import yfinance as yf

st.title("Financial Stock Market Dashboard")

ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA):", "AAPL")
stock = yf.Ticker(ticker)
data = stock.history(period="1mo")

st.write("## Stock Price Trend")
st.line_chart(data['Close'])

st.write("## Key Metrics")
st.write(stock.info)
