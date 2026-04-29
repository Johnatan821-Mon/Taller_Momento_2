import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ventas = pd.read_csv('ventas.csv')
clientes = pd.read_csv('cliente.csv')

ventas.loc[0:5, ['producto', 'total']]
ventas.iloc[0:5, [0, 3]]

ventas.groupby("categoria")["total"].sum()

grupo = ventas.groupby("canal")
ventas_online = grupo.get_group("Online")

df = pd.merge(ventas, clientes, )