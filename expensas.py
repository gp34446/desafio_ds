import numpy as np
import pandas as pd
import re

data = pd.read_csv('../desafio_ds/properati.csv')

def expensas(df,input=0):
    if str(input) == '0':
        pattern = 'SIN EXPENSA|NO HAY EXPENSA|NO TIENE EXPENSA'
    else:
        pattern = '(?P<expensa>expensa*).{1,20}(?P<moneda>\$\D*)(?P<monto>\d+)'
    patron_sin_ex = re.compile(pattern,re.IGNORECASE)
    search = df['description'].apply(lambda x:x if x is np.NaN else patron_sin_ex.search(re.sub('\.','',x)))
    mascara_search = (search.notnull()) & df['expenses'].isnull()
    if str(input) == '0':
        df.loc[mascara_search,'expenses'] = 0
    else:
        df.loc[mascara_search,'expenses'] = search[mascara_search].apply(lambda x: float(x.group('monto')))

data['expenses2'] = data['expenses']
print(data['expenses'].isna().sum())
expensas(data,input = 'nro')
print(data['expenses'].isna().sum())
expensas(data,input = '0')
print(data['expenses'].isna().sum())
print(data.loc[74,'expenses'])
mascara = (data['expenses'] > 50000) & (data['expenses'].notnull()) & (data['expenses2'].isnull())
print(data.loc[mascara,['expenses','expenses2']])



