import pandas as pd
import numpy as np


datos = {
    'Nombre': ["Juan", "Ana", "Luis", "Marta", "Pedro"],
    'Calificacion': [85, 90, 78, 92, 88],
    'Deportes': ["Fútbol", "Baloncesto", "Natación", "Tenis", "Ciclismo"],
    'Materias':["Matemáticas", "Historia", "Ciencias", "Literatura", "Geografía"],
    'Edad': [20, 22, 21, 19, 23],
}

df= pd.DataFrame(datos)
print(df)
print("\n"*2)

datos2 = {
    'Nombre': ["Juan", "Ana", "Luis", "N/A", "Pedro"],
    'Calificacion': [85, 90, 78, np.nan, 88],
    'Deportes': ["Fútbol", "N/A", "Natación", "Tenis", "Ciclismo"],
    'Materias':["Matemáticas", "Historia", "Ciencias", "Literatura", "N/A"],
    'Edad': [20, 22, 21, 19, 23],
}

df2 = pd.DataFrame(datos2)
print(df2)
print(df2.info())
print("\n"*2)
print(df2.describe())
