import pandas as pd

# 1) Leer su archivo csv utilizado.
# 2) De ser posible, elegir una columna que pueda servir como índice y setearla como tal.
# 3) Eliminar las filas duplicadas
# 4) Eliminar las filas con valores que no sirven (espacios vacíos y "NaN")
# 5) Escribir un nuevo archivo .csv con las modificaciones realizadas
# 6) Colocar en forma de tabla, las primeras 3000 filas  y luego, las ultimas 2000.
# Si su archivo csv no tiene una cantidad de datos que cumpla lo pedido,
# la tabla deberá tener las primeras 300 y las últimas 200.

df = pd.read_csv("bocas-de-subte.csv")

dfIndex = df.set_index("id")

# Te dejo el comando que saca los espacios vacios pero no lo uso porque el csv que use, en todas la lineas tiene un null
# dfSinVacio = dfIndex.dropna()

dfSinDuplicados = dfIndex.drop_duplicates()

df1 = dfSinDuplicados.iloc[0:30]

i1 = len(dfSinDuplicados) - 21
i2 = len(dfSinDuplicados) - 1

df2 = dfSinDuplicados.iloc[i1: i2]

dff = pd.concat([df1, df2])

print(len(dff))

dff.to_csv("nuevo.csv")
