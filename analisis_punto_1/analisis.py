import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ventas = pd.read_csv('ventas.csv')
clientes = pd.read_csv('cliente.csv')

ventas_reducido = pd.read_csv("ventas.csv", usecols=['producto', 'total'])
ventas.shape
print('\nForma del DataFrame `ventas` (shape) - (filas, columnas):', ventas.shape)

print('\nMostrando información del DataFrame `clientes` (info):')
clientes.info()

print('\nResumen estadístico del DataFrame `ventas` (describe):')
print(ventas.describe())

#acceso a columnas
ventas.total
clientes.edad

print('\nPrimeras entradas de la columna `total` en `ventas` (head):')
print(ventas['total'].head())

print('\nPrimeras entradas de la columna `edad` en `clientes` (head):')
print(clientes['edad'].head())

#indexacion
ventas.index = ventas.id_venta

ventas.set_index('id_venta', inplace=True)
print('\n`ventas` con nuevo índice `id_venta` - primeras filas:')
print(ventas.head())


