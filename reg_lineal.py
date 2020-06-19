import pandas as pd
from sklearn import linear_model
from sklearn import metrics
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
import numpy as np

def corr_filter(df,y, val=0.0001):
 x = df.drop(y, axis = 1)
 lista = []
 for i in x.columns:
  corr = df[[y,i]].corr()
  if corr.iloc[0][i] > abs(val):
   lista.append(i)
 return lista
"""SELECCIONO CAMPOS Y APLICAMOS DUMMIES"""
df = pd.read_csv('../desafio_ds/df_clean.csv')
df = df[df['lat'].notnull()]
col = ['property_type', 'place_name',  'state_name','lat','lon',\
 'surface_total_in_m2', 'price_usd_per_m2', 'floor', 'rooms', 'expenses', \
 'pileta|piscina', 'terraza|solarium', 'cochera|garage', 'patio|jardin', 'laundry|lavadero', \
 'parrilla|churrasquera|asadera', 'amenities']
#'lat','lon',
df = df[col]
df = pd.get_dummies(df, drop_first=True)
lista = corr_filter(df,'price_usd_per_m2')
print(lista)
"""MODELO REG LINEAL"""

lm_ridge = linear_model.RidgeCV(alphas=[0.1, 1, 10], normalize=True)
#rfe = RFE(lm_ridge, 20)
y = df['price_usd_per_m2']
X = df[lista]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=179798700)

lm_ridge.fit(X_train, y_train)

y_predicted = lm_ridge.predict(X_test)

print(metrics.r2_score(y_test, y_predicted))

