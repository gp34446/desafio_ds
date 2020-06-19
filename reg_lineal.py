import pandas as pd
from sklearn import linear_model
from sklearn import metrics
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
import numpy as np

def corr_filter(df,y= 'price_usd_per_m2', val=0.001):
 x = df.drop(y, axis = 1)
 lista = []
 for i in x.columns:
  corr = df[[y,i]].corr()
  if corr.iloc[0][i] > abs(val):
   lista.append(i)
 return lista
"""SELECCIONO CAMPOS Y APLICAMOS DUMMIES"""
df = pd.read_csv('../desafio_ds/df_clean.csv')


def ridge(data,state_name, target='price_usd_per_m2', val_corr=0.001):
 df = pd.get_dummies(data, drop_first=True)
 lista = corr_filter(df, target, val_corr)
 lm_ridge = linear_model.RidgeCV(alphas=[0.00001, 0.00005, 0.0001, 0.0005, 0.001, 0.005, 0.01,\
                                        0.05, 0.1, 1, 5, 10], normalize=True, cv=5)
 y = df[target]
 X = df[lista]
 X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=100)
 lm_ridge.fit(X_train, y_train)
 y_predicted = lm_ridge.predict(X_test)
 dicc = {'state_name':st,'r2':metrics.r2_score(y_test, y_predicted),'observaciones':df.shape[0]}
 print(dicc)
 return dicc

col = ['property_type', 'place_name',  'state_name',\
 'surface_total_in_m2', 'price_usd_per_m2', 'floor', 'rooms', 'expenses', \
 'pileta|piscina', 'terraza|solarium', 'cochera|garage', 'patio|jardin', 'laundry|lavadero', \
 'parrilla|churrasquera|asadera', 'amenities']

df = df[col]
lista = []
iterador = df['state_name'].unique().tolist()
for st in iterador:
  df_aux = df[df['state_name'] == st]
  if df_aux.shape[0] > 100:
   df_aux = df_aux.drop('state_name', axis=1)
   lista.append(ridge(df_aux,state_name = st))

df_final = pd.DataFrame(lista)
df_final.to_csv('../desafio_ds/df_score.csv')