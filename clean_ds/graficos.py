import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
from clean_ds import clean_func as cf
pd.set_option('display.max_columns', None)

data = pd.read_csv('C:/Users/Gonzalo/dh/curso/ds_blend_students_2020/desafio_ds/df_aux.csv')

mask_provincia = data['state_name'].isin(['Bs.As. G.B.A. Zona Sur', 'Bs.As. G.B.A. Zona Norte', 'Bs.As. G.B.A. Zona Oeste'])
data = data.loc[mask_provincia]
df_agg = data.groupby(['state_name','place_name']).agg({'price_usd_per_m2':np.mean})
g = df_agg['price_usd_per_m2'].groupby(level=0, group_keys=False)
g = g.nlargest(5)
g = pd.DataFrame(g)
g['price_usd_per_m2'] = g['price_usd_per_m2'].round()
g= g.add_suffix('_mean').reset_index()
g = g.rename({'state_name':'Zona','place_name':'Barrio','price_usd_per_m2_mean':'Media M2 USD'},axis=1)
print(g)

sns.set(style="whitegrid")

graph = sns.catplot(x="Barrio", y="Media M2 USD", hue="Zona", data=g,
                height=6, kind="bar", palette="muted")
graph.despine(left=True)
graph.set_ylabels("Media M2 USD Barrios Gran BsAs")
plt.show()



