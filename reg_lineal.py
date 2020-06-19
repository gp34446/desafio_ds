import pandas as pd
from sklearn import linear_model
from sklearn import metrics
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np

def corr_filter(df,y, val):
 x = df.drop(y, axis = 1)
 for i in x.columns:
  corr = df[[y,i]]

"""SELECCIONO CAMPOS Y APLICAMOS DUMMIES"""
df = pd.read_csv('../desafio_ds/df_clean.csv')
pd.set_option('display.max_columns', None)
col = ['property_type', 'place_name',  'state_name','lat','lon',\
 'surface_total_in_m2', 'price_usd_per_m2', 'floor', 'rooms', 'expenses', \
 'pileta|piscina', 'terraza|solarium', 'cochera|garage', 'patio|jardin', 'laundry|lavadero', \
 'parrilla|churrasquera|asadera', 'amenities']
df = df[col]
df = df[df['lat'].notnull()]
df = pd.get_dummies(df, drop_first=True)

"""MODELO REG LINEAL"""

lm_ridge = linear_model.RidgeCV(alphas=[0.1, 1, 10], normalize=True)

y = df['price_usd_per_m2']
X = df.drop('price_usd_per_m2', axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=100)

lm_ridge.fit(X_train, y_train)

y_predicted = lm_ridge.predict(X_test)

print(metrics.r2_score(y_test, y_predicted))

