#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pycoingecko')
get_ipython().system('pip install plotly')
get_ipython().system('pip install mplfinance')


# In[2]:


import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc


# In[3]:


# Data needed to get the information of coin , vs currency and days
cg = CoinGeckoAPI()

bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)


# In[4]:


# Getting the price of the bitcoin
bitcoin_price_data = bitcoin_data['prices']

bitcoin_price_data[0:5]


# In[6]:


#Convert the data into panda frame
data = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp', 'Price'])
print(data)


# In[7]:


#convert the timestamp to date and time
data['date'] = data['TimeStamp'].apply(lambda d: datetime.date.fromtimestamp(d/1000.0))


# In[8]:


#Find the min, max, open and close for candlestick
candlestick_data = data.groupby(data.date, as_index=False).agg({"Price": ['min', 'max', 'first', 'last']})


# In[9]:


#Plot candle stick chart
fig = go.Figure(data=[go.Candlestick(x=candlestick_data['date'],
                open=candlestick_data['Price']['first'], 
                high=candlestick_data['Price']['max'],
                low=candlestick_data['Price']['min'], 
                close=candlestick_data['Price']['last'])
                ])

fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()


# In[ ]:




