{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Funcion para hallar propiedades con terraza"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(121220, 26)"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_location='C:/Users/Juan/Documents/Digital House/Data Science/Desafio/properati.csv'\n",
    "data=pd.read_csv(data_location,sep=',')\n",
    "data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "def terraza(df):\n",
    "    pattern='terraza'\n",
    "    terraza_regex=re.compile(pattern,re.IGNORECASE)\n",
    "    terraza_match = df.description.apply(lambda x: x if x is np.NaN else terraza_regex.search(x))\n",
    "    terraza_match_notnull = terraza_match.notnull()\n",
    "    a_reemplazar = list(set(df.description.loc[terraza_match_notnull]))\n",
    "    df['terraza'] = df.description.loc[terraza_match_notnull].replace(a_reemplazar, \"SI\")\n",
    "    reemplazo_nulos_terraza=list(set(df.terraza.loc[df.terraza!='SI']))\n",
    "    df['terraza']= df.terraza.replace(reemplazo_nulos_terraza,'NO')\n",
    "    print('Se han encontrado ',df.terraza.loc[df.terraza=='SI'].count(),' propiedades con terraza')\n",
    "    print('Representa un ',((df.terraza.loc[df.terraza=='SI'].count()/df.shape[0])*100).round(2),' % de las propiedades publicadas')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Se han encontrado  27509  propiedades con terraza\n",
      "Representa un  22.69  % de las propiedades publicadas\n"
     ]
    }
   ],
   "source": [
    "terraza(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
