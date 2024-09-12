import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
# FOR MAC
import requests
from io import StringIO

# FUNCTION:
def convert_to_float(column):
    return [float(i.replace("$","").replace(",","")) for i in column]

# FOR MAC
url='https://raw.githubusercontent.com/ynfresfin/stock_data/main/PG_HistoricalData_1726077114896.csv'
s=requests.get(url).text #turns data from github into String Data
df=pd.read_csv(StringIO(s),
    parse_dates=["Date"],
    index_col=['Date'])

df["Close/Last"] = convert_to_float(df["Close/Last"])

#Simple Moving Average
sma_window = 7  # 7-day moving average
sma = df["Close/Last"].rolling(window=sma_window).mean()

#Exponential Moving Average
ema_window = 30  # 30-day moving average
ema = df["Close/Last"].ewm(span=ema_window, adjust=False).mean()

# START BELOW:

