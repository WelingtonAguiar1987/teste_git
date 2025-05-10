import yfinance as yf
import pandas as pd
import streamlit as st
import numpy as np

def historical_data(ticker, start_date, end_date, interval):
    df = yf.download(tickers=ticker, start=start_date, end=end_date, interval=interval)
    df.columns = df.columns.droplevel(1)
    df['Return'] = df['Close'].pct_change()
    df['Volatility'] = df['High'] - df['Low']
    return df

def standard_deviation():
    dp = np.std(historical_data(ticker, start_date, end_date, interval)['Return'] * 100)
    return dp

ticker = "MNQM25.CME"
start_date = "2024-03-15"
end_date = "2025-06-20"
interval = "1d"

st.dataframe(historical_data(ticker, start_date, end_date, interval))
st.write(f'Desvio Padrão: {standard_deviation():.2f}%')