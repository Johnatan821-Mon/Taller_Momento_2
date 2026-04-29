import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ventas = pd.read_csv('ventas.csv')
clientes = pd.read_csv('cliente.csv')

ventas_reducido = pd.read_csv("ventas.csv", usecols=['producto', 'total'])
ventas.shape
print('\n=== ventas.shape ===')
print('(filas, columnas):', ventas.shape)

print('\n=== clientes.info() ===')
clientes.info()
print('\n=== ventas.describe() ===')
print(ventas.describe())

#acceso a columnas
ventas.total
clientes.edad

print('\n=== ventas.total (head) ===')
print(ventas['total'].head())

print('\n=== clientes.edad (head) ===')
print(clientes['edad'].head())

#indexacion
ventas.index = ventas.id_venta

ventas.set_index('id_venta', inplace=True)
print('\n=== ventas con nuevo índice (head) ===')
print(ventas.head())


