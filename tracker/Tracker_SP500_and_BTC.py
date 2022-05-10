#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf


# Import and save data

# SP500
sp500 = yf.Ticker('^GSPC')
sp500_hist = sp500.history(period='5y')
sp500_hist.to_csv('sp500.csv')

# BTC
btc = yf.Ticker('BTC-USD')
btc_hist = btc.history(period='5y')
btc_hist.to_csv('btc.csv')


# In[15]:


# Load data

data_sp500 = pd.read_csv('sp500.csv')
data_btc = pd.read_csv('btc.csv')

data_sp500['Date'] = pd.to_datetime(data_sp500['Date'])
data_btc['Date'] = pd.to_datetime(data_btc['Date'])


# In[24]:


# Plot data

fig = plt.gcf()
plt.plot(data_sp500['Date'], data_sp500['Close'], label='SP500')
plt.plot(data_btc['Date'], data_btc['Close'], label='BTC')
plt.ylabel('Value [USD]')
plt.xlabel('Date [Year]')
plt.title('Price of SP500 and Bitcoin in the last 5 years')
plt.legend()
plt.show()

fig.savefig('sp500_BTC_5years.png')


# In[ ]:




