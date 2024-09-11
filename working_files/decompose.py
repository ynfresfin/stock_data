import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# FUNCTION:
def convert_to_float(column):
    return [float(i.replace("$","").replace(",","")) for i in column]

df = pd.read_csv("https://github.com/ynfresfin/stock_data/raw/main/V_HistoricalData_1726077072765.csv",
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

