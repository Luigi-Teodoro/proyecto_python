import pandas as pd 
import numpy as np

datos = pd.read_csv("matches_serie_A.csv", encoding="latin-1")
df = pd.DataFrame(datos)    
print(df)
print("\n"*1)
print("cuantos goles anoto el napoli en la temporada 2025:")
print(df[(df['Team'] == 'Napoli') & (df['Season'] == 2025)]['GF'].sum())