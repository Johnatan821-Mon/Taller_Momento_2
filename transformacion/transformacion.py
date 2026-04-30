import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ventas = pd.read_csv('ventas.csv')
clientes = pd.read_csv('cliente.csv')

# Mostrar primeras filas: columnas 'producto' y 'total'
primeros_producto_total = ventas.loc[0:5, ['producto', 'total']]
print("Primeras 6 filas (index 0-5) - columnas 'producto' y 'total':\n", primeros_producto_total)

# Mostrar primeras filas por posición de columnas (columnas 0 y 3)
primeros_cols_pos = ventas.iloc[0:5, [0, 3]]
print("Primeras 5 filas (por posición) - columnas 0 y 3:\n", primeros_cols_pos)

# Suma del total por categoría
totales_por_categoria = ventas.groupby("categoria")["total"].sum()
print("Suma de 'total' por 'categoria':\n", totales_por_categoria)

# Agrupar por canal y mostrar el objeto GroupBy
grupo = ventas.groupby("canal")
print("Objeto GroupBy agrupado por 'canal':\n", grupo)

# Obtener ventas del canal 'Online' (si existe)
try:
	ventas_online = grupo.get_group("Online")
	print("Filas del grupo 'Online':\n", ventas_online)
except Exception:
	print("No existe el grupo 'Online' en la columna 'canal'.")

# Merge entre ventas y clientes
df = pd.merge(ventas, clientes)
print("Resultado de pd.merge(ventas, clientes):\n", df)

# Concatenación vertical de ventas y clientes (si tiene sentido)
df_total = pd.concat([ventas, clientes])
print("Resultado de pd.concat([ventas, clientes]) - filas combinadas:\n", df_total)