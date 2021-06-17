import pandas as pd

# 7) Imprimir el data frame escrito en el nuevo archivo .csv
# 8) Colocar en forma de tabla las filas 1, 5, 12, 36.
# 9) Imprimir una lista con los nombres de todas las columnas.
# 10) Imprimir los datos de una columna a elección.

df = pd.read_csv("bocas-de-subte.csv")
dfIndex = df.set_index("id")
dfSinDuplicados = dfIndex.drop_duplicates()
df1 = dfSinDuplicados.iloc[0:30]
i1 = len(dfSinDuplicados) - 21
i2 = len(dfSinDuplicados) - 1
df2 = dfSinDuplicados.iloc[i1: i2]
dff = pd.concat([df1, df2])

print(dff)

print(df1.iloc[[1, 5, 12, 29]]) # Use el 29 en vez del 36 por un tema de que no tiene tantas lineas

print(list(dfSinDuplicados.columns))

print(dfSinDuplicados['calle'])

