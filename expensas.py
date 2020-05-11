import numpy as np
import pandas as pd
import re

data = pd.read_csv('../desafio_ds/properati.csv')

def expensas(df):
    cont = data['expenses'].isna().sum()
    cont_orig = cont
    pattern = '(SIN\sEXPENSA|NO\sHAY\sEXPENSA|NO\sTIENE\sEXPENSA)'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = df['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(re.sub('\.', '', x)))
    mascara_search = (search.notnull()) & df['expenses'].isnull()
    df.loc[mascara_search, 'expenses'] = 0
    resultado = cont - data['expenses'].isna().sum()
    cont = data['expenses'].isna().sum()
    print('Se completaron con el patron SIN EXPENSA: {} registros'.format(resultado))

    pattern = '(?P<expensa>expensa.{1,20})(?P<moneda>\$\D*)(?P<monto>\d+)'
    patron_sin_ex = re.compile(pattern,re.IGNORECASE)
    search = df['description'].apply(lambda x:x if x is np.NaN else patron_sin_ex.search(re.sub('\.','',x)))
    mascara_search = (search.notnull()) & df['expenses'].isnull()
    df.loc[mascara_search,'expenses'] = search[mascara_search].apply(lambda x: float(x.group('monto')))
    resultado = cont - data['expenses'].isna().sum()
    cont = data['expenses'].isna().sum()
    print('Se completaron con el patron EXPENSAS MONTO: {} registros'.format(resultado))
    print('Total original de NULLs para expenses: {}'.format(cont_orig))
    print('Total actual de NULLs para expenses: {}'.format(cont))
    print('Porcentaje de NULLs corregidos para expenses: {}%'.format(round((100 - (cont * 100) / cont_orig)), 0))
expensas(data)


