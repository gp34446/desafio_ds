import numpy as np
import pandas as pd
import re

def pisos(data):
    cont = data['floor'].isna().sum()
    cont_orig = cont
    mascara = ((data['property_type'] == 'house') | (data['property_type'] == 'store')) & (data['floor'].isnull())
    data.loc[mascara,'floor'] = 0
    resultado = cont - data['floor'].isna().sum()
    cont = data['floor'].isna().sum()
    print('Se completaron con el patron TYPE HOUSE: {} registros'.format(resultado))

    dic_piso = {'PLANTA BAJA': 0, 'PRIMER': 1, 'SEGUNDO': 2, 'TERCERO': 3, 'CUARTO': 4, 'QUINTO': 5, 'SEXTO': 6,
                'SEPTIMO': 7, 'OCTAVO': 8, 'NOVENO': 9, 'DECIMO': 10}
    pattern = '(?P<nro>PRIMER|SEGUNDO|TERCERO|CUARTO|QUINTO|SEXTO|SEPTIMO|OCTAVO|NOVENO|DECIMO)(?P<piso>\sPISO\s)'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
    mascara_search = (search.notnull()) & data['floor'].isnull()
    data.loc[mascara_search, 'floor'] = search[mascara_search].apply(lambda x: int(dic_piso[str.upper(x.group('nro'))]))
    resultado = cont - data['floor'].isna().sum()
    cont = data['floor'].isna().sum()
    print('Se completaron con el patron PRIMER.SEGUNDO.....PISO: {} registros'.format(resultado))

    pattern = '(?P<nro>\d{1,2})(?P<piso>(er|do|to|mo|vo|no)\spiso\s)'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
    mascara_search = (search.notnull()) & data['floor'].isnull()
    data.loc[mascara_search, 'floor'] = search[mascara_search].apply(
        lambda x: int(x.group('nro')))
    resultado = cont - data['floor'].isna().sum()
    cont = data['floor'].isna().sum()
    print('Se completaron con el patron 1ER....2DO.....PISO: {} registros'.format(resultado))

    pattern = '(?P<nro>\d{1,2})(?P<piso>\spiso\s)'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
    mascara_search = (search.notnull()) & data['floor'].isnull()
    data.loc[mascara_search, 'floor'] = search[mascara_search].apply(
        lambda x: int(x.group('nro')))
    resultado = cont - data['floor'].isna().sum()
    cont = data['floor'].isna().sum()
    print('Se completaron con el patron 1..2.....PISO: {} registros'.format(resultado))

    pattern = '(?P<piso>piso\s)(?P<nro>\d{1,2})'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
    mascara_search = (search.notnull()) & data['floor'].isnull()
    data.loc[mascara_search, 'floor'] = search[mascara_search].apply(
        lambda x: int(x.group('nro')))
    resultado = cont - data['floor'].isna().sum()
    cont = data['floor'].isna().sum()
    print('Se completaron con el patron PISO...1..2....: {} registros'.format(resultado))

    dic_piso = {'UNO': 1, 'DOS': 2, 'TRES': 3, 'CUARTO': 4, 'CINCO': 5, 'SEIS': 6, 'SIETE': 7, 'OCHO': 8, 'NUEVE': 9,
                'DIEZ': 10}
    pattern = '(?P<piso>PISO\s)(?P<nro>UNO|DOS|TRES|CUARTO|CINCO|SEIS|SIETE|OCHO|NUEVE|DIEZ)'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
    mascara_search = (search.notnull()) & data['floor'].isnull()
    data.loc[mascara_search, 'floor'] = search[mascara_search].apply(lambda x: int(dic_piso[str.upper(x.group('nro'))]))
    resultado = cont - data['floor'].isna().sum()
    cont = data['floor'].isna().sum()
    print('Se completaron con el patron PISO...UNO...DOS.....: {} registros'.format(resultado))

    pattern = 'PLANTA\sBAJA'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
    mascara_search = (search.notnull()) & data['floor'].isnull()
    data.loc[mascara_search, 'floor'] = 0
    resultado = cont - data['floor'].isna().sum()
    cont = data['floor'].isna().sum()
    print('Se completaron con el patron PLANTA BAJA: {} registros'.format(resultado))
    print('Total original de NULLs para floor: {}'.format(cont_orig))
    print('Total actual de NULLs para floor: {}'.format(cont))
    print('Porcentaje de NULLs corregidos para floor: {}%'.format(round((100-(cont * 100)/cont_orig)),0))

def precio_aprox_dolar(data):
    cont = data['price_aprox_usd'].isna().sum()
    cont_orig = cont
    pattern = '(?P<moneda>(U\$S|US\$|USD|\$US|U\$D)\s)(?P<monto>\d+(\.\d+)?)'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['title'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
    mascara_search = (search.notnull()) & data['price_aprox_usd'].isnull()
    data.loc[mascara_search, 'price_aprox_usd'] = search[mascara_search].apply(lambda x: float(re.sub("[^0-9]","",x.group('monto'))))
    print(data.loc[mascara_search, 'price_aprox_usd'])
    resultado = cont - data['price_aprox_usd'].isna().sum()
    cont = data['price_aprox_usd'].isna().sum()
    print('Se completaron con el patron USD$: {}'.format(resultado))
    print(data.loc[mascara_search, 'price_aprox_usd'])
    print('Porcentaje de NULLs corregidos para price_aprox_usd: {}%'.format(round((100 - (cont * 100) / cont_orig)), 0))
