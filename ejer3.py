import pandas as pd
import numpy as np

datos = pd.read_csv("ElectronicsData.csv", encoding="latin-1")
print(datos)
print(datos.info())
print('\n'*2)
print(datos.head())
nuevo = pd.DataFrame(datos)
print(nuevo.info())
print(nuevo.describe())

nuevo['Price'] = nuevo['Price'].astype(int)
print(nuevo)