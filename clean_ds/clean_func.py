import numpy as np
import pandas as pd
import re


def pisos(data):
    cont = data['floor'].isna().sum()
    cont_orig = cont

    mascara = ((data['property_type'] == 'house') | (data['property_type'] == 'store')) & (data['floor'].isnull())
    data.loc[mascara, 'floor'] = 0
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
    print('Porcentaje de NULLs corregidos para floor: {}%'.format(round((100 - (cont * 100) / cont_orig)), 0))


def precio_aprox_dolar(data):
    cont = data['price_aprox_usd'].isna().sum()
    cont_orig = cont
    pattern = '(?P<moneda>(U\$S|US\$|USD|\$US|U\$D)\s?)(?P<monto>\d+(\.\d+)?)'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['title'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
    mascara_search = (search.notnull()) & data['price_aprox_usd'].isnull()
    data.loc[mascara_search, 'price_aprox_usd'] = search[mascara_search].apply(
        lambda x: round(float(str.replace(re.sub("[^0-9\,]", "", x.group('monto')), ",", ".")), 2))
    resultado = cont - data['price_aprox_usd'].isna().sum()
    cont = data['price_aprox_usd'].isna().sum()
    print('Se completaron con el patron U$ MONTO TITLE: {} registros'.format(resultado))

    pattern = '(?P<moneda>(U\$S|US\$|USD|\$US|U\$D)(\s|:|:\s)?)(?P<monto>\d+(\.\d+)?)'
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


def amenities(data, lista=['pileta|piscina', 'terraza|solarium', 'cochera|garage', 'patio|jardin', 'laundry|lavadero',
                           'parrilla|churrasquera|asadera', 'zoom']):
    total = data.shape[0]
    for i in lista:
        pattern = i
        data[i] = False
        patron_sin_ex = re.compile(pattern, re.IGNORECASE)
        search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
        mascara_search = search.notnull()
        mascara_search2 = search.isnull()
        data.loc[mascara_search, i] = 1
        data.loc[mascara_search2, i] = 0
        cont = data[i].sum()
        print('Se obtuvieron {} registros con {}'.format(cont, i))
        print('El porcentaje de propiedades con {} es {}%'.format(i, round((cont / total) * 100, 2), i))
    data['amenities'] = data[lista].sum(axis=1)


def m2(df):
    superficie_total(df)
    precio_aprox_dolar(df)
    cont_orig = df['price_usd_per_m2'].isnull().sum()
    mascara = df['price_aprox_usd'].notnull() & df['surface_total_in_m2'].notnull() & df['price_usd_per_m2'].isnull()
    df.loc[mascara, 'price_usd_per_m2'] = df.loc[mascara, 'price_aprox_usd'] / df.loc[mascara, 'surface_total_in_m2']

    cont = df['price_usd_per_m2'].isnull().sum()
    print('Registros actualizados para price_usd_per_m2: {}'.format(cont_orig - cont))
    print('Total original de NULLs para price_usd_per_m2: {}'.format(cont_orig))
    print('Total actual de NULLs para price_usd_per_m2: {}'.format(cont))
    print(
        'Porcentaje de NULLs corregidos para price_usd_per_m2: {}%'.format(round((100 - (cont * 100) / cont_orig)), 0))


def superficie_cubierta(data):
    cont = data['surface_covered_in_m2'].isna().sum()
    cont_orig = cont
    pattern = '(?P<sup>\sCUBIERT(A|O|AS|OS)(\s|:|:\s)?)(?P<nro>\d{2,4}[.,]?\d*)'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
    mascara_search = (search.notnull()) & data['surface_covered_in_m2'].isnull()
    data.loc[mascara_search, 'surface_covered_in_m2'] = search[mascara_search].apply(
        lambda x: round(float(str.replace(re.sub("[^0-9\,]", "", x.group('nro')), ",", ".")), 2))
    resultado = cont - data['surface_covered_in_m2'].isna().sum()
    cont = data['surface_covered_in_m2'].isna().sum()
    print('Se completaron con el patron CUBIERTA NRO: {} registros'.format(resultado))

    pattern = '(?P<nro>\d{2,4}[.,]?\d*)(?P<sup>\sCUBIERT(A|O))'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
    mascara_search = (search.notnull()) & data['surface_covered_in_m2'].isnull()
    data.loc[mascara_search, 'surface_covered_in_m2'] = search[mascara_search].apply(
        lambda x: round(float(str.replace(re.sub("[^0-9\,]", "", x.group('nro')), ",", ".")), 2))
    resultado = cont - data['surface_covered_in_m2'].isna().sum()
    cont = data['surface_covered_in_m2'].isna().sum()
    print('Se completaron con el patron NRO CUBIERTA: {} registros'.format(resultado))

    pattern = '(?P<nro>\d{2,4}[.,]?\d*)(?P<sup>\sconstruido)'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
    mascara_search = (search.notnull()) & data['surface_covered_in_m2'].isnull()
    data.loc[mascara_search, 'surface_covered_in_m2'] = search[mascara_search].apply(
        lambda x: round(float(str.replace(re.sub("[^0-9\,]", "", x.group('nro')), ",", ".")), 2))
    resultado = cont - data['surface_covered_in_m2'].isna().sum()
    cont = data['surface_covered_in_m2'].isna().sum()
    print('Se completaron con el patron NRO CONSTRUIDO: {} registros'.format(resultado))

    print('Total original de NULLs para surface_covered_in_m2: {}'.format(cont_orig))
    print('Total actual de NULLs para surface_covered_in_m2: {}'.format(cont))
    print(
        'Porcentaje de NULLs corregidos para surface_covered_in_m2: {}%'.format(round((100 - (cont * 100) / cont_orig)),
                                                                                0))


def superficie_total(data):
    cont = data['surface_total_in_m2'].isna().sum()
    cont_orig = cont
    superficie_cubierta(data)

    pattern = '(?P<sup>\sDESCUBIERT(A|O|OS|AS)(\s|:|:\s)?)(?P<nro>\d{2,4}[.,]?\d*)'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
    mascara_search = search.notnull()
    data.loc[mascara_search, 'surface_uncovered_in_m2'] = search[mascara_search].apply(
        lambda x: round(float(str.replace(re.sub("[^0-9\,]", "", x.group('nro')), ",", ".")), 2))
    resultado = data['surface_uncovered_in_m2'].notnull().sum()
    print('Se completaron con el patron DESCUBIERTA NRO: {} registros'.format(resultado))

    pattern = '(?P<nro>\d{2,4}[.,]?\d*)(?P<sup>\sDESCUBIERT(A|O))'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
    mascara_search = search.notnull() & data['surface_uncovered_in_m2'].isnull()
    data.loc[mascara_search, 'surface_uncovered_in_m2'] = search[mascara_search].apply(
        lambda x: round(float(str.replace(re.sub("[^0-9\,]", "", x.group('nro')), ",", ".")), 2))
    print('Se completaron con el patron NRO DESCUBIERTA : {} registros'.format(resultado))

    mascara_search = data['surface_uncovered_in_m2'].notnull() & data['surface_covered_in_m2'].notnull() & data[
        'surface_total_in_m2'].isnull()
    data.loc[mascara_search, 'surface_total_in_m2'] = data.loc[mascara_search, 'surface_covered_in_m2'] + data.loc[
        mascara_search, 'surface_uncovered_in_m2']
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

    pattern = '(?P<sup>(\s?)SUPERFICIE\sTOTAL(\s|:|:\s)?)(?P<nro>\d{2,4}[.,]?\d*)'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(x))
    mascara_search = search.notnull() & data['surface_covered_in_m2'].isnull()
    data.loc[mascara_search, 'surface_total_in_m2'] = search[mascara_search].apply(
        lambda x: round(float(str.replace(re.sub("[^0-9\,]", "", x.group('nro')), ",", ".")), 2))
    resultado = cont - data['surface_total_in_m2'].isna().sum()
    cont = data['surface_total_in_m2'].isna().sum()
    print('Se completaron con el patron SUPERFICIE TOTAL: {} registros'.format(resultado))

    mascara = ((data['property_type'] == 'apartment')) & (data['surface_total_in_m2'].isnull()) & (
        data['surface_covered_in_m2'].notnull())
    data.loc[mascara, 'surface_total_in_m2'] = data['surface_covered_in_m2']
    resultado = cont - data['surface_covered_in_m2'].isna().sum()
    cont = data['surface_covered_in_m2'].isna().sum()
    print('Se completaron con el patron TYPE APARTMENT: {} registros'.format(resultado))

    print('Total original de NULLs para surface_total_in_m2: {}'.format(cont_orig))
    print('Total actual de NULLs para surface_total_in_m2: {}'.format(cont))
    print('Porcentaje de NULLs corregidos para surface_total_in_m2: {}%'.format(round((100 - (cont * 100) / cont_orig)),
                                                                                0))

    mascara = data['surface_total_in_m2'].notnull() & data['surface_covered_in_m2'].notnull()
    data['surface_uncovered_in_m2'] = data['surface_total_in_m2'] - data['surface_covered_in_m2']
    print('Se completaron para el campo surface_uncovered_in_m2: {} registros'.format(
        data['surface_uncovered_in_m2'].notnull().sum()))


def expensas(data):
    cont = data['expenses'].isna().sum()
    cont_orig = cont

    mascara = (data['property_type'] == 'house') & (data['expenses'].isnull())
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

    pattern = '(?P<expensa>expensa\D{1,15})(?P<monto>\d{2,4}[.,]?\d*)'
    patron_sin_ex = re.compile(pattern, re.IGNORECASE)
    search = data['description'].apply(lambda x: x if x is np.NaN else patron_sin_ex.search(re.sub('\.', '', x)))
    mascara_search = (search.notnull()) & data['expenses'].isnull()
    data.loc[mascara_search, 'expenses'] = search[mascara_search].apply(
        lambda x: round(float(str.replace(re.sub("[^0-9\,]", "", x.group('monto')), ",", ".")), 2))
    resultado = cont - data['expenses'].isna().sum()
    cont = data['expenses'].isna().sum()
    print('Se completaron con el patron EXPENSAS MONTO: {} registros'.format(resultado))

    print('Total original de NULLs para expenses: {}'.format(cont_orig))
    print('Total actual de NULLs para expenses: {}'.format(cont))
    print('Porcentaje de NULLs corregidos para expenses: {}%'.format(round((100 - (cont * 100) / cont_orig)), 0))


def rooms(df):
    cont = df['rooms'].isna().sum()
    cont_orig = cont

    pattern_ambientes_num = "(?P<rooms>\d)\s(AMBIENTE|AMBIENTES|AMB|AMBS|AMBIENT|AMBIENTS)"
    ambientes_num_regex = re.compile(pattern_ambientes_num, re.IGNORECASE)
    ambientes_num_search = df.description.apply(lambda x: x if x is np.NaN else ambientes_num_regex.search(x))
    ambientes_num_mask = (ambientes_num_search.notnull()) & (df.rooms.isnull())
    df.loc[ambientes_num_mask, "rooms"] = ambientes_num_search[ambientes_num_mask].apply(
        lambda x: x.group("rooms"))

    resultado = cont - df['rooms'].isna().sum()
    cont = df['rooms'].isna().sum()
    print('Se completaron con el patron AMBIENTES: {} registros'.format(resultado))

    pattern_monoambientes_num = "(?P<monos>MONOAMBIENTE|MONOAMBIENTES|MONO|MONOS|MONOAMB|MONOAMBS)"
    monoambientes_num_regex = re.compile(pattern_monoambientes_num, re.IGNORECASE)
    monoambientes_num_search = df.description.apply(lambda x: x if x is np.NaN else monoambientes_num_regex.search(x))
    monoambientes_mask = (monoambientes_num_search.notnull()) & (df.rooms.isnull())
    df.loc[monoambientes_mask, "rooms"] = 1

    resultado = cont - df['rooms'].isna().sum()
    cont = df['rooms'].isna().sum()
    print('Se completaron con el patron MONOAMBIENTES: {} registros'.format(resultado))

    pattern_habitaciones_num = "(?P<habitaciones>\d)\s(HABITACION|HABITACIONES|HAB|CUARTOS|CUARTO)"
    habitaciones_num_regex = re.compile(pattern_habitaciones_num, re.IGNORECASE)
    habitaciones_num_search = df.description.apply(lambda x: x if x is np.NaN else habitaciones_num_regex.search(x))
    habitaciones_mask = (habitaciones_num_search.notnull()) & (df.rooms.isnull())
    df.loc[habitaciones_mask, "rooms"] = (habitaciones_num_search[habitaciones_mask].apply(
        lambda x: x.group("habitaciones")).astype(int)) + 1

    resultado = cont - df['rooms'].isna().sum()
    cont = df['rooms'].isna().sum()
    print('Se completaron con el patron HABITACIONES: {} registros'.format(resultado))

    dic_ambientes = {'UN': 1, 'DOS': 2, 'TRES': 3, 'CUATRO': 4, 'CINCO': 5, 'SEIS': 6, 'SIETE': 7, 'OCHO': 8,
                     'NUEVE': 9, 'DIEZ': 10}
    pattern_ambientes_letters = "(?P<rooms_letters>UN|DOS|TRES|CUATRO|CINCO|SEIS|SIETE|OCHO|NUEVE|DIEZ)\s?(?P<rooms_amb>AMBIENTE|AMBIENTES|AMB|AMBS|AMBIENT|AMBIENTS|HABITACION|HABITACIONES|HAB|CUARTOS|CUARTO)\s?"
    ambientes_letters_regex = re.compile(pattern_ambientes_letters, re.IGNORECASE)

    ambientes_letters_search = df.description.apply(lambda x: x if x is np.NaN else ambientes_letters_regex.search(x))
    ambientes_letters_mask = (ambientes_letters_search.notnull()) & (df.rooms.isnull())

    df.loc[ambientes_letters_mask, "rooms"] = (ambientes_letters_search[ambientes_letters_mask].apply(
        lambda x: int(dic_ambientes[str.upper(x.group('rooms_letters'))])))

    resultado = cont - df['rooms'].isna().sum()
    cont = df['rooms'].isna().sum()
    print('Se completaron con el patron HABITACIONES UN DOS TRES: {} registros'.format(resultado))
    print('Total original de NULLs para rooms: {}'.format(cont_orig))
    print('Total actual de NULLs para rooms: {}'.format(cont))
    print('Porcentaje de NULLs corregidos para rooms: {}%'.format(round((100 - (cont * 100) / cont_orig)), 0))


def completar(df, lista_amenities=['pileta|piscina', 'terraza|solarium', 'cochera|garage', 'patio|jardin',
                                   'laundry|lavadero', 'parrilla|churrasquera|asadera']):
    df2 = df
    expensas(df)
    pisos(df)
    rooms(df)
    m2(df)
    amenities(df, lista_amenities)
    campos = ['property_type', 'place_name', 'state_name', 'price_aprox_usd', 'surface_total_in_m2',
              'surface_covered_in_m2', 'price_usd_per_m2', 'floor', 'rooms', 'expenses']
    print('-------------------SITUACION INICIAL-------------------------')
    print(round(df2[campos].isnull().sum() / df2.shape[0] * 100), 2)
    print('-------------------SITUACION ACTUAL-------------------------')
    print(round(df[campos].isnull().sum() / df.shape[0] * 100), 2)
    print('--------------------------------------------')


def filtrar_errores(df):
    campos = ['property_type', 'place_name', 'state_name', 'price_aprox_usd', 'surface_total_in_m2',
              'surface_covered_in_m2', 'price_usd_per_m2', 'floor', 'rooms', 'expenses']
    mascara = (df['price_usd_per_m2'].notnull()) & (df['price_aprox_usd'] > 9999) & (df['surface_total_in_m2'] > 19)
    print('Se eliminaron {} registros por inconsistencias en el campo price_usd_per_m2'.format(df.shape[0]-df[mascara].shape[0]))
    print('-------------------SITUACION INICIAL-------------------------')
    print('-------------------%NULLS-------------------------')
    print(round(df[campos].isnull().sum() / df.shape[0] * 100), 2)
    print('-------------------CANTIDAD DE REGISTROS-------------------------')
    print(df[campos].count())
    print('-------------------SITUACION ACTUAL-------------------------')
    print('-------------------%NULLS-------------------------')
    print(round(df.loc[mascara,campos].isnull().sum() / df.loc[mascara,campos].shape[0] * 100), 2)
    print('-------------------CANTIDAD DE REGISTROS-------------------------')
    print(df.loc[mascara,campos].count())
    print('--------------------------------------------')
    return df[mascara]

def imputar_floor_room(df):
    g = df.groupby(['state_name', 'place_name']).agg({'floor': 'mean', 'rooms': 'mean'})
    g = pd.DataFrame(g)
    g = g.add_suffix('_mean').reset_index()
    g = g.fillna(0)
    df2 = df.merge(how='inner', right=g, on=['state_name', 'place_name'])
    mascara_rooms = df2['rooms'].isnull()
    mascara_floor = df2['floor'].isnull()
    df2.loc[mascara_rooms, 'rooms'] = df2.loc[mascara_rooms, 'rooms_mean'].apply(lambda x: round(x))
    df2.loc[mascara_floor, 'floor'] = df2.loc[mascara_floor, 'floor_mean'].apply(lambda x: round(x))
    df2 = df2.drop(['rooms_mean', 'floor_mean'], axis=1)
    campos = ['rooms', 'floor']
    print('Se imputaron {} valores para rooms ' .format(mascara_rooms.sum()))
    print('Se imputaron {} valores para floor '.format(mascara_floor.sum()))
    print('-------------------SITUACION INICIAL-------------------------')
    print('-------------------%NULLS-------------------------')
    print(round(df.loc[campos].isnull().sum() / df.shape[0] * 100), 2)
    print('-------------------CANTIDAD DE REGISTROS-------------------------')
    print(df.loc[campos].count())
    print('-------------------SITUACION ACTUAL-------------------------')
    print('-------------------%NULLS-------------------------')
    print(round(df2.loc[campos].isnull().sum() / df2.shape[0] * 100), 2)
    print('-------------------CANTIDAD DE REGISTROS-------------------------')
    print(df2.loc[campos].count())
    print('--------------------------------------------')
    df = df2
def df_gen(df):
    pd.set_option('display.max_columns', None)
    completar(df)
    df2 = filtrar_errores(df)
    imputar_floor_room(df2)
    df2.to_csv('../desafio_ds/df_clean.csv')
    pd.set_option('display.max_columns', 5)
