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
    resultado = cont - data['price_aprox_usd'].isna().sum()
    cont = data['price_aprox_usd'].isna().sum()
    print('Se completaron con el patron USD$: {}'.format(resultado))
    print(data.loc[mascara_search, 'price_aprox_usd'])
    print('Porcentaje de NULLs corregidos para price_aprox_usd: {}%'.format(round((100 - (cont * 100) / cont_orig)), 0))

def amenities(data,lista):
    total = data.shape[0]
    for i in lista:
        pattern = i
        data[i] = False
        patron_sin_ex = re.compile(pattern, re.IGNORECASE)
        search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
        mascara_search = search.notnull()
        data.loc[mascara_search, i] = True
        cont = data[i].sum()
        print('Se obtuvieron {} registros con {}'.format(cont,i))
        print('El porcentaje de propiedades con {} es {}%'.format(i,round((cont/total)*100,2),i))

def m2(df):
    cont = df['price_usd_per_m2'].isnull().sum()
    mascara = df['price_aprox_usd'].notnull() & df['surface_covered_in_m2'].notnull() & df['price_usd_per_m2'].isnull()
    df['price_usd_per_m2'] = df['price_aprox_usd']/ df['surface_covered_in_m2']
    print('Registrs actualizados para price_usd_per_m2: {}' .format(cont - df['price_usd_per_m2'].isnull().sum()))

def superficie(data):
    cont = data['surface_covered_in_m2'].isna().sum()
    cont_orig = cont
    "^\d*[.,]?\d*$"
    pattern = '(?P<sup>\sCUBIERT(A|O)\s)(?P<nro>\d{2,4}[.,]?\d*)'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
    mascara_search = (search.notnull()) & data['surface_covered_in_m2'].isnull()
    data.loc[mascara_search, 'surface_covered_in_m2'] = search[mascara_search].apply(lambda x: round(float(str.replace(re.sub("[^0-9\,]", "", x.group('nro')),",",".")),2))
    resultado = cont - data['surface_covered_in_m2'].isna().sum()
    cont = data['surface_covered_in_m2'].isna().sum()
    print('Se completaron con el patron CUBIERTA NRO: {} registros'.format(resultado))

    pattern = '(?P<nro>\d{2,4}[.,]?\d*)(?P<sup>\sCUBIERT(A|O)\s)'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
    mascara_search = (search.notnull()) & data['surface_covered_in_m2'].isnull()
    data.loc[mascara_search, 'surface_covered_in_m2'] = search[mascara_search].apply(
        lambda x: round(float(str.replace(re.sub("[^0-9\,]", "", x.group('nro')),",",".")),2))
    resultado = cont - data['surface_covered_in_m2'].isna().sum()
    cont = data['surface_covered_in_m2'].isna().sum()
    print('Se completaron con el patron NRO CUBIERTA: {} registros'.format(resultado))

    pattern = '(?P<sup>\sSUPERFICIE\s\D{0,15})(?P<nro>\d{2,4}[.,]?\d*)'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
    mascara_search = (search.notnull()) & data['surface_covered_in_m2'].isnull()
    data.loc[mascara_search, 'surface_covered_in_m2'] = search[mascara_search].apply(
        lambda x: round(float(str.replace(re.sub("[^0-9\,]", "", x.group('nro')),",",".")),2))
    resultado = cont - data['surface_covered_in_m2'].isna().sum()
    cont = data['surface_covered_in_m2'].isna().sum()
    print('Se completaron con el patron SUPERFICIE: {} registros'.format(resultado))

    pattern = '(?P<nro>\d{2,4}[.,]?\d*)(?P<sup>\sconstruido\s)'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
    mascara_search = (search.notnull()) & data['surface_covered_in_m2'].isnull()
    data.loc[mascara_search, 'surface_covered_in_m2'] = search[mascara_search].apply(
        lambda x: round(float(str.replace(re.sub("[^0-9\,]", "", x.group('nro')),",",".")),2))
    resultado = cont - data['surface_covered_in_m2'].isna().sum()
    cont = data['surface_covered_in_m2'].isna().sum()
    print('Se completaron con el patron NRO CONSTRUIDO: {} registros'.format(resultado))

    pattern = '(?P<nro>\d{2,4}[.,]?\d*)(?P<sup>(\s?)(M2|METROS\sCUADRADOS|M²))'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
    mascara_search = (search.notnull()) & data['surface_covered_in_m2'].isnull()
    data.loc[mascara_search, 'surface_covered_in_m2'] = search[mascara_search].apply(
        lambda x: round(float(str.replace(re.sub("[^0-9\,]", "", x.group('nro')),",",".")),2))
    resultado = cont - data['surface_covered_in_m2'].isna().sum()
    cont = data['surface_covered_in_m2'].isna().sum()
    print('Se completaron con el patron M2: {} registros'.format(resultado))

    print('Total original de NULLs para surface_covered_in_m2: {}'.format(cont_orig))
    print('Total actual de NULLs para surface_covered_in_m2: {}'.format(cont))
    print('Porcentaje de NULLs corregidos para surface_covered_in_m2: {}%'.format(round((100 - (cont * 100) / cont_orig)), 0))


