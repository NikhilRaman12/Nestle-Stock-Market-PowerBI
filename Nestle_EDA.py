import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("nestle.csv")
print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.nunique())
print(df.drop_duplicates())

print(df.isnull().sum())
df["Date"] = pd.to_datetime(df["Date"])
print(df[df["Deliverable Quantity" ].isnull()])
df['Deliverable Quantity'].fillna(df['Deliverable Quantity'].median(), inplace=True)
df['% Deli. Qty to Traded Qty'].fillna(df['% Deli. Qty to Traded Qty'].median(), inplace=True)print(df.isnull().sum)
print(df.columns)
df['Daily Return'] = df['Close Price'].pct_change()
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['DayOfWeek'] = df['Date'].dt.dayofweek

