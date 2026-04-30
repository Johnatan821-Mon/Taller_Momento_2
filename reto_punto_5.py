import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar y limpiar datos
ventas = pd.read_csv('ventas.csv')
clientes = pd.read_csv('cliente.csv')

# Limpiar ventas
ventas['total'] = pd.to_numeric(ventas['total'], errors='coerce')
ventas = ventas.dropna(subset=['id_cliente', 'total'])

# Limpiar clientes
clientes = clientes.drop_duplicates()
clientes['edad'] = pd.to_numeric(clientes['edad'], errors='coerce')
clientes['edad'] = clientes['edad'].fillna(0)
clientes['salario'] = pd.to_numeric(clientes['salario'], errors='coerce')
clientes = clientes.dropna(subset=['id_cliente', 'nombre'])

# Merge
df = pd.merge(ventas, clientes, on='id_cliente', how='inner')

print("=" * 70)
print("RESPUESTAS - RETO PUNTO 5")
print("=" * 70)

# 1. Categoría con más ingresos
print("\n1. ¿Qué categoría genera más ingresos?")
cat_ingresos = df.groupby('categoria')['total'].sum().sort_values(ascending=False)
print(cat_ingresos)
print(f"✅ RESPUESTA: {cat_ingresos.idxmax()}")

# 2. Canal que vende más
print("\n2. ¿Qué canal vende más?")
canal_ventas = df['canal'].value_counts()
print(canal_ventas)
print(f"✅ RESPUESTA: {canal_ventas.idxmax()}")

# 3. Mayor salario = más compras
print("\n3. ¿Clientes con mayor salario compran más?")
alto = df.loc[df['salario'] > 3000000, 'total'].mean()
bajo = df.loc[df['salario'] <= 3000000, 'total'].mean()
print(f"Salario > $3M: promedio ${alto:,.0f}")
print(f"Salario ≤ $3M: promedio ${bajo:,.0f}")
print(f"✅ RESPUESTA: {'Sí' if alto > bajo else 'No'}")

# 4. Método de pago más usado
print("\n4. ¿Qué método de pago es más usado?")
metodos = df['metodo_pago'].value_counts()
print(metodos)
print(f"✅ RESPUESTA: {metodos.idxmax()}")

# 5. Top 5 clientes
print("\n5. ¿Top 5 clientes con más compras?")
top5 = df.groupby('nombre').size().sort_values(ascending=False).head(5)
print(top5)

# Gráficos
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Gráfico 1
cat_ingresos.sort_values(ascending=True).plot(kind='barh', ax=axes[0, 0], color='steelblue')
axes[0, 0].set_title('1. Ingresos por Categoría', fontweight='bold')

# Gráfico 2
canal_ventas.plot(kind='bar', ax=axes[0, 1], color='coral')
axes[0, 1].set_title('2. Ventas por Canal', fontweight='bold')
axes[0, 1].tick_params(axis='x', rotation=0)

# Gráfico 3
metodos.plot(kind='pie', ax=axes[1, 0], autopct='%1.1f%%')
axes[1, 0].set_title('4. Métodos de Pago', fontweight='bold')
axes[1, 0].set_ylabel('')

# Gráfico 4
top5.plot(kind='bar', ax=axes[1, 1], color='lightgreen')
axes[1, 1].set_title('5. Top 5 Clientes', fontweight='bold')
axes[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('visualizacion/reto_punto_5_graficos.png', dpi=300, bbox_inches='tight')
print("\n✅ Gráficos guardados en: visualizacion/reto_punto_5_graficos.png")
plt.show()
