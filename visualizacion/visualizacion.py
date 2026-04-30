import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ventas = pd.read_csv('ventas.csv')
clientes = pd.read_csv('cliente.csv')

#Gráfico 1: Ventas por categoría
ventas.groupby('categoria')['total'].sum().plot(kind='bar')
plt.title('Ventas por Categoría')
plt.savefig('visualizacion/ventas_por_categoria.png', dpi=300, bbox_inches='tight')
plt.show()

#Gráfico 2: Método de pago
sns.countplot(data=ventas, x='metodo_pago')
plt.savefig('visualizacion/metodo_pago.png', dpi=300, bbox_inches='tight')
plt.show()

#Gráfico 3: Relación salario vs puntaje
sns.scatterplot(data=clientes, x='salario', y='puntaje')
plt.savefig('visualizacion/salario_vs_puntaje.png', dpi=300, bbox_inches='tight')
plt.show()