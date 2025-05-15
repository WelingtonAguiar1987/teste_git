# BIBLIOTECAS NECESSÁRIAS:
import yfinance as yf
import pandas as pd
import streamlit as st
import numpy as np
import datetime

# FUNÇÃO PARA DADOS HISTÓRICOS:
def historical_data(ticker, start_date, end_date, interval):
    df = yf.download(tickers=ticker, start=start_date, end=end_date, interval=interval)
    df.columns = df.columns.droplevel(1)
    df['Return'] = df['Close'].pct_change()
    df['Volatility'] = df['High'] - df['Low']
    return df

# FUNÇÃO PARA DESVIO PADRÃO:
def standard_deviation():
    dp = np.std(historical_data(ticker, start_date, end_date, interval)['Return'] * 100)
    return dp

# FUNÇÃO PARA MÉDIA:
def mean():
    mean = np.mean(historical_data(ticker, start_date, end_date, interval)['Close'])
    return mean

# FUNÇÃO PARA VOLATILIDADE MÉDIA:
def volatility_mean():
    volatility_mean = np.mean(historical_data(ticker, start_date, end_date, interval)['Volatility'])
    return volatility_mean

# FUNÇÃO PARA MEDIANA:
def median():
    median = np.median(historical_data(ticker, start_date, end_date, interval)['Close'])
    return median

# LISTAS:
list_ticker = ['MNQM25.CME', 'MESM25.CME', 'MYMM25.CME', 'M2KM25.CME', 'MNQ=F', 'MES=F', 'MYM=F', 'M2K=F']
list_interval = ['5m', '15m', '30m', '60m', '1d']

# CRIANDO SIDEBAR:
st.sidebar.subheader('Selecione os Filtros')
st.sidebar.header("", divider='rainbow')
ticker = st.sidebar.selectbox('Selecione o Ativo: ', list(list_ticker))
start_date = st.sidebar.date_input('Selecione a Data Inicial: ', format='DD-MM-YYYY')
end_date = st.sidebar.date_input('Selecione a Data Final: ', format='DD-MM-YYYY')
interval = st.sidebar.selectbox('Selecione o Intervalo: ', list(list_interval))
st.sidebar.header("", divider='rainbow')

# CRIANDO PRINTS DOS DADOS DE ESTATÍSTICAS:
st.header(f':green[NASDAQ FUTUROS {ticker}]')
st.header("", divider='rainbow')
st.subheader(':orange[Tabela Dados Históricos]')
st.dataframe(historical_data(ticker, start_date, end_date, interval))
st.header("", divider='rainbow')
st.subheader(':orange[Dados Estatísticos]')
st.write(f'Desvio Padrão: {standard_deviation():.2f}%.')
st.write(f'Média: {mean():.2f}.')
st.write(f'Mediana: {median():.2f}.')
st.write(f'Volatilidade Média: {volatility_mean():.2f}.')
st.header("", divider='rainbow')
st.subheader(':orange[Gráfico]')
fig =  st.line_chart(historical_data(ticker, start_date, end_date, interval)['Close'])
st.header("", divider='rainbow')
