# BIBLIOTECAS NECESSÁRIAS:
import yfinance as yf
import pandas as pd
import streamlit as st
import numpy as np

# FUNÇÃO PARA DADOS HISTÓRICOS:
def historical_data(ticker, start_date, end_date, interval):
    df = yf.download(tickers=ticker, start=start_date, end=end_date, interval=interval)
    df.columns = df.columns.droplevel(1) # Tratando erro no dataframe:
    df['Return'] = df['Close'].pct_change() # Adicionando coluna de Retornos:
    df['Volatility'] = df['High'] - df['Low'] # Adicionando coluna de Volatilidade:
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
list_ticker = ['MNQM25.CME', 'MESM25.CME', 'MYMM25.CME', 'M2KM25.CME', 'MNQ=F', 'MES=F', 'MYM=F', 'M2K=F'] # Sigla dos Ativos:
list_interval = ['5m', '15m', '30m', '60m', '1d'] # Lista dos Intervalos dos timeframes:


# CRIANDO SIDEBAR:
st.sidebar.subheader('Selecione os Filtros')
st.sidebar.header("", divider='rainbow')
ticker = st.sidebar.selectbox('Selecione o Ativo: ', list(list_ticker)) # Ticker do Ativo:
start_date = st.sidebar.date_input('Selecione a Data Inicial: ', format='DD-MM-YYYY') # Data Inicial:
end_date = st.sidebar.date_input('Selecione a Data Final: ', format='DD-MM-YYYY') # Data Final:
interval = st.sidebar.selectbox('Selecione o Intervalo: ', list(list_interval)) # Intervalo:
st.sidebar.header("", divider='rainbow')
last_adjusted_closing = st.sidebar.number_input('Digite o fechamento Ajustado: ') # Último Fechamento Ajustado:
st.header("", divider='rainbow')
annual_effective_rate = st.sidebar.number_input(label='Digite a Taxa Efetiva: ') # Taxa Efetiva Anual:
days_to_maturity = st.sidebar.number_input(label='Digite a Qtde Dias até o Vencimento: ', step=0) # Dias para o Vencimento:

# Cálculo Taxa:
daily_effective_rate = annual_effective_rate / 365 # Taxa Efetiva Dia:
effective_rate_maturity = daily_effective_rate * days_to_maturity # Taxa Efetiva Vencimento:
volatility_rate = last_adjusted_closing * effective_rate_maturity / 100 # Taxa Volatilidade:
first_maximum_volatility = last_adjusted_closing + volatility_rate # Primeira Volatilidade Máxima:
second_maximum_volatility = last_adjusted_closing + (volatility_rate * 2) # Segunda Volatilidade Máxima:
third_maximum_volatility = last_adjusted_closing + (volatility_rate * 3) # Terceira Volatilidade Máxima:
first_minimum_volatility = last_adjusted_closing - volatility_rate # Primeira Volatilidade Mínima:
second_minimum_volatility = last_adjusted_closing - (volatility_rate * 2) # Segunda Volatilidade Mínima:
third_minimum_volatility = last_adjusted_closing - (volatility_rate * 3) # Terceira Volatilidade Mínima:

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
st.write(f'Taxa Efetiva Anual: {annual_effective_rate:.2f}.')
st.write(f'Taxa Efetiva P/ Dia: {daily_effective_rate:.4f}.')
st.write(f'Taxa Efetiva Até o Vencimento: {effective_rate_maturity:.4f}.')
st.write(f'Dias até o Vencimento: {days_to_maturity:.2f}.')
st.write(f'Volatilidade Taxa (Pontos): {volatility_rate:.2f}.')
st.header("", divider='rainbow')

# Print dos Níveis das Taxas:
st.subheader(':orange[Níveis das Taxas]')
st.write(f'3ª Vol Positiva: :red[{third_maximum_volatility:.2f}].')
st.write(f'2ª Vol Positiva: :red[{second_maximum_volatility:.2f}].')
st.write(f'1ª Vol Positiva: :red[{first_maximum_volatility:.2f}].')
st.write(f'Último Fechamento Ajustado: {last_adjusted_closing:.2f}.')
st.write(f'-1ª Vol Negativa: :green[{first_minimum_volatility:.2f}].')
st.write(f'-2ª Vol Negativa: :green[{second_minimum_volatility:.2f}].')
st.write(f'-3ª Vol Negativa: :green[{third_minimum_volatility:.2f}].')

st.header("", divider='rainbow')
st.subheader(':orange[Gráfico]')
fig =  st.line_chart(historical_data(ticker, start_date, end_date, interval)['Close']) # Gráfico:
st.header("", divider='rainbow')



