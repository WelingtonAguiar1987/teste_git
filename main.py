import yfinance as yf
import pandas as pd
import streamlit as st
import numpy as np

def dados_historicos(ticker, start_date, end_date, interval):
    df = yf.download(tickers=ticker, start=start_date, end=end_date, interval=interval)
    df.columns = df.columns.droplevel(1)
    df['Return'] = df['Close'].pct_change()
    df['Volatility'] = df['High'] - df['Low']
    
    return df


ticker = "MNQ=F"
start_date = "2024-03-15"
end_date = "2025-06-20"
interval = "1d"

st.dataframe(dados_historicos(ticker, start_date, end_date, interval))