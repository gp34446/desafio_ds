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
    pattern = '(?P<moneda>(U\$S|US\$|USD|\$US|U\$D)\s?)(?P<monto>\d+(\.\d+)?)'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['title'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
    mascara_search = (search.notnull()) & data['price_aprox_usd'].isnull()
    data.loc[mascara_search, 'price_aprox_usd'] = search[mascara_search].apply(lambda x: round(float(str.replace(re.sub("[^0-9\,]", "", x.group('monto')),",",".")),2))
    resultado = cont - data['price_aprox_usd'].isna().sum()
    cont = data['price_aprox_usd'].isna().sum()
    print('Se completaron con el patron U$ MONTO TITLE: {} registros'.format(resultado))

    pattern = '(?P<moneda>(U\$S|US\$|USD|\$US|U\$D)\s?)(?P<monto>\d+(\.\d+)?)'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
    mascara_search = (search.notnull()) & data['price_aprox_usd'].isnull()
    data.loc[mascara_search, 'price_aprox_usd'] = search[mascara_search].apply(
        lambda x: round(float(str.replace(re.sub("[^0-9\,]", "", x.group('monto')), ",", ".")), 2))
    resultado = cont - data['price_aprox_usd'].isna().sum()
    print('Se completaron con el patron U$ MONTO DESC: {} registros'.format(resultado))

    print('Total original de NULLs para price_aprox_usd: {}'.format(cont_orig))
    print('Total actual de NULLs para price_aprox_usd: {}'.format(cont))
    print('Porcentaje de NULLs corregidos para price_aprox_usd: {}%'.format(round((100 - (cont * 100) / cont_orig)), 0))

def amenities(data,lista=['pileta','terraza','cochera','patio']):
    total = data.shape[0]
    for i in lista:
        pattern = i
        data[i] = False
        patron_sin_ex = re.compile(pattern, re.IGNORECASE)
        search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
        mascara_search = search.notnull()
        mascara_search2 = search.isnull()
        data.loc[mascara_search, i] = True
        data.loc[mascara_search2, i] = False
        cont = data[i].sum()
        print('Se obtuvieron {} registros con {}'.format(cont,i))
        print('El porcentaje de propiedades con {} es {}%'.format(i,round((cont/total)*100,2),i))

def m2(df):
    superficie_total(df)
    precio_aprox_dolar(df)
    cont_orig = df['price_usd_per_m2'].isnull().sum()
    mascara = df['price_aprox_usd'].notnull() & df['surface_total_in_m2'].notnull() & df['price_usd_per_m2'].isnull()
    df.loc[mascara,'price_usd_per_m2'] = df.loc[mascara,'price_aprox_usd']/ df.loc[mascara,'surface_total_in_m2']

    cont = df['price_usd_per_m2'].isnull().sum()
    print('Registros actualizados para price_usd_per_m2: {}' .format(cont_orig - cont))
    print('Total original de NULLs para price_usd_per_m2: {}'.format(cont_orig))
    print('Total actual de NULLs para price_usd_per_m2: {}'.format(cont))
    print('Porcentaje de NULLs corregidos para price_usd_per_m2: {}%'.format(round((100 - (cont * 100) / cont_orig)),0))

def superficie_cubierta(data):
    cont = data['surface_covered_in_m2'].isna().sum()
    cont_orig = cont
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

    pattern = '(?P<nro>\d{2,4}[.,]?\d*)(?P<sup>\sconstruido\s)'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
    mascara_search = (search.notnull()) & data['surface_covered_in_m2'].isnull()
    data.loc[mascara_search, 'surface_covered_in_m2'] = search[mascara_search].apply(
        lambda x: round(float(str.replace(re.sub("[^0-9\,]", "", x.group('nro')),",",".")),2))
    resultado = cont - data['surface_covered_in_m2'].isna().sum()
    cont = data['surface_covered_in_m2'].isna().sum()
    print('Se completaron con el patron NRO CONSTRUIDO: {} registros'.format(resultado))

    print('Total original de NULLs para surface_covered_in_m2: {}'.format(cont_orig))
    print('Total actual de NULLs para surface_covered_in_m2: {}'.format(cont))
    print('Porcentaje de NULLs corregidos para surface_covered_in_m2: {}%'.format(round((100 - (cont * 100) / cont_orig)), 0))

def superficie_total(data):
    cont = data['surface_total_in_m2'].isna().sum()
    cont_orig = cont
    superficie_cubierta(data)

    pattern = '(?P<sup>\sDESCUBIERT(A|O)\s)(?P<nro>\d{2,4}[.,]?\d*)'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
    mascara_search = search.notnull()
    data.loc[mascara_search, 'surface_uncovered_in_m2'] = search[mascara_search].apply(
        lambda x: round(float(str.replace(re.sub("[^0-9\,]", "", x.group('nro')), ",", ".")), 2))
    resultado = data['surface_uncovered_in_m2'].notnull().sum()
    print('Se completaron con el patron DESCUBIERTA NRO: {} registros'.format(resultado))

    pattern = '(?P<nro>\d{2,4}[.,]?\d*)(?P<sup>\sDESCUBIERT(A|O)\s)'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
    mascara_search = search.notnull() & data['surface_uncovered_in_m2'].isnull()
    data.loc[mascara_search, 'surface_uncovered_in_m2'] = search[mascara_search].apply(
        lambda x: round(float(str.replace(re.sub("[^0-9\,]", "", x.group('nro')), ",", ".")), 2))
    print('Se completaron con el patron NRO DESCUBIERTA : {} registros'.format(resultado))

    mascara_search = data['surface_uncovered_in_m2'].notnull() & data['surface_covered_in_m2'].notnull() & data['surface_total_in_m2'].isnull()
    data.loc[mascara_search,'surface_total_in_m2'] = data.loc[mascara_search,'surface_covered_in_m2'] + data.loc[mascara_search,'surface_uncovered_in_m2']
    resultado = cont - data['surface_total_in_m2'].isna().sum()
    cont = data['surface_total_in_m2'].isna().sum()
    print('Se completaron sumando superficie descubierta con superficie cubierta: {} registros'.format(resultado))

    pattern = '(?P<nro>\d{2,4}[.,]?\d*)(?P<sup>(\s?)(M\s|M2|METRO\sCUADRADOS|M²))'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
    mascara_search = search.notnull() & data['surface_covered_in_m2'].isnull()
    data.loc[mascara_search, 'surface_total_in_m2'] = search[mascara_search].apply(
        lambda x: round(float(str.replace(re.sub("[^0-9\,]", "", x.group('nro')), ",", ".")), 2))
    resultado = cont - data['surface_total_in_m2'].isna().sum()
    cont = data['surface_total_in_m2'].isna().sum()
    print('Se completaron con el patron M2: {} registros'.format(resultado))

    pattern = '(?P<sup>(\s?)SUPERFICIE\sTOTAL\s)(?P<nro>\d{2,4}[.,]?\d*)'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
    mascara_search = search.notnull() & data['surface_covered_in_m2'].isnull()
    data.loc[mascara_search, 'surface_total_in_m2'] = search[mascara_search].apply(
        lambda x: round(float(str.replace(re.sub("[^0-9\,]", "", x.group('nro')), ",", ".")), 2))
    resultado = cont - data['surface_total_in_m2'].isna().sum()
    cont = data['surface_total_in_m2'].isna().sum()
    print('Se completaron con el patron SUPERFICIE TOTAL: {} registros'.format(resultado))

    mascara = ((data['property_type'] == 'apartment')) & (data['surface_total_in_m2'].isnull()) & (data['surface_covered_in_m2'].notnull())
    data.loc[mascara, 'surface_total_in_m2'] = data['surface_covered_in_m2']
    resultado = cont - data['surface_covered_in_m2'].isna().sum()
    cont = data['surface_covered_in_m2'].isna().sum()
    print('Se completaron con el patron TYPE APARTMENT: {} registros'.format(resultado))

    print('Total original de NULLs para surface_total_in_m2: {}'.format(cont_orig))
    print('Total actual de NULLs para surface_total_in_m2: {}'.format(cont))
    print('Porcentaje de NULLs corregidos para surface_total_in_m2: {}%'.format(round((100 - (cont * 100) / cont_orig)),0))


def expensas(data):
    cont = data['expenses'].isna().sum()
    cont_orig = cont

    mascara = ((data['property_type'] == 'house') ) & (data['expenses'].isnull())
    data.loc[mascara, 'expenses'] = 0
    resultado = cont - data['expenses'].isna().sum()
    cont = data['expenses'].isna().sum()
    print('Se completaron con el patron TYPE HOUSE: {} registros'.format(resultado))

    pattern = '(SIN\sEXPENSA|NO\sHAY\sEXPENSA|NO\sTIENE\sEXPENSA)'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(re.sub('\.', '', x)))
    mascara_search = (search.notnull()) & data['expenses'].isnull()
    data.loc[mascara_search, 'expenses'] = 0
    resultado = cont - data['expenses'].isna().sum()
    cont = data['expenses'].isna().sum()
    print('Se completaron con el patron SIN EXPENSA: {} registros'.format(resultado))

    pattern = '(?P<expensa>expensa\w{1,15})(?P<monto>\d{2,4}[.,]?\d*)'
    patron_sin_ex = re.compile(pattern,re.IGNORECASE)
    search = data['description'].apply(lambda x:x if x is np.NaN else patron_sin_ex.search(re.sub('\.','',x)))
    mascara_search = (search.notnull()) & data['expenses'].isnull()
    data.loc[mascara_search,'expenses'] = search[mascara_search].apply(lambda x: round(float(str.replace(re.sub("[^0-9\,]", "", x.group('monto')), ",", ".")), 2))
    resultado = cont - data['expenses'].isna().sum()
    cont = data['expenses'].isna().sum()
    print('Se completaron con el patron EXPENSAS MONTO: {} registros'.format(resultado))

    print('Total original de NULLs para expenses: {}'.format(cont_orig))
    print('Total actual de NULLs para expenses: {}'.format(cont))
    print('Porcentaje de NULLs corregidos para expenses: {}%'.format(round((100 - (cont * 100) / cont_orig)), 0))

def completar(df):
    expensas(df)
    pisos(df)
    m2(df)
    amenities(df)

def filtrar_errores(df):
    mascara = df['price_usd_per_m2'].notnull()
    df2 = df.loc[mascara]
    df = df2
    #df = df.loc[df['price_aprox_usd'] > 9999]
    #df = df.loc[df['surface_total_in_m2'] > 9]