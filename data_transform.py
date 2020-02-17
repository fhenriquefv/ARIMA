# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Time series analysis with ARIMA
# Some time ago I had a discussion about time series analysis and ARIMA models, which found me quite unprepared!
# So I decided to look a bit closer to this neat piece of classical time series analysis. I found out that there are several excellent tutorials on how to use ARIMA, which I link below. Still, I found it useful to compile my own example to summarize my understanding of the problem and to collect links to useful resources.
# %% [markdown]
# ## Import libraries and get sample data

# %%
# Import libraries
import warnings
import itertools
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Defaults
plt.rcParams['figure.figsize'] = (20.0, 10.0)
plt.rcParams.update({'font.size': 12})
plt.style.use('ggplot')

# %% [markdown]
# Get the classic international airline passengers data, downloadable from the DataMarket webpage (https://datamarket.com/data/set/22u3/international-airline-passengers-monthly-totals-in-thousands-jan-49-dec-60#!ds=22u3&display=line) as a CSV with filename "international-airline-passengers.csv".

# %%
# Load the data
data = pd.read_csv('processamento-petroleo-m3-1990-2018.csv',  sep=';', encoding = "ISO-8859-1", engine='python', skipfooter=3)
# A bit of pre-processing to make it nicer
def mask(df, key, value):
        return df[df[key] == value]

pd.DataFrame.mask = mask
#dataFiltered = data.mask('REFINARIA','REDUC')

for row in dataFiltered.itertuples():
     print(row)

# %%
