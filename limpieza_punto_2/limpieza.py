import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def print_header(title: str):
	sep = "=" * 60
	print(f"\n{sep}\n{title}\n{sep}")
ventas = pd.read_csv('ventas.csv')
clientes = pd.read_csv('cliente.csv')

# --- clientes_sin_nulos: snapshot antes/despues ---
orig_clientes_rows = len(clientes)
clientes_sin_nulos = clientes.dropna()
print_header('clientes_sin_nulos')
print(f"Antes  - filas: {orig_clientes_rows:d}")
print(f"Después- filas: {len(clientes_sin_nulos):d}")
print("Mostrando información del DataFrame 'clientes_sin_nulos' (clientes sin nulos):")
clientes_sin_nulos.info()

# --- llenar edad nula: Antes/Después ---
edad_nulos_antes = clientes['edad'].isna().sum()
clientes["edad"] = clientes["edad"].fillna(0)
print_header('clientes con edad nula reemplazada por 0')
print(f"Antes  - edad nulas: {edad_nulos_antes:d}")
print(f"Después- edad nulas: {clientes['edad'].isna().sum():d}")
print("Mostrando información del DataFrame 'clientes' después de rellenar 'edad':")
clientes.info()

# --- eliminar duplicados: Antes/Después ---
rows_before_dup = len(clientes)
clientes = clientes.drop_duplicates()
print_header('clientes sin duplicados')
print(f"Antes  - filas: {rows_before_dup:d}")
print(f"Después- filas: {len(clientes):d}")
print("Mostrando información del DataFrame 'clientes' después de eliminar duplicados:")
clientes.info()

# --- convertir tipos numéricos: Antes/Después ---
edad_nonnull_antes = clientes['edad'].notna().sum()
salario_nonnull_antes = clientes['salario'].notna().sum()
clientes["edad"] = pd.to_numeric(clientes["edad"], errors='coerce')
clientes["salario"] = pd.to_numeric(clientes["salario"], errors='coerce')
print_header('clientes con tipos de datos corregidos')
print(f"Antes  - edad no nulos: {edad_nonnull_antes:d}")
print(f"Después- edad no nulos: {clientes['edad'].notna().sum():d}")
print(f"Antes  - salario no nulos: {salario_nonnull_antes:d}")
print(f"Después- salario no nulos: {clientes['salario'].notna().sum():d}")
print("Mostrando información del DataFrame 'clientes' después de corregir tipos de datos:")
clientes.info()

# --- limpieza de texto: Antes/Después (ciudad) ---
# contar nulos o cadenas vacías antes
ciudad_blank_mask = clientes['ciudad'].isna() | (clientes['ciudad'].fillna('').str.strip() == '')
ciudad_nulos_antes = int(ciudad_blank_mask.sum())
# limpiar y rellenar con valor por defecto
clientes["ciudad"] = clientes["ciudad"].fillna('').str.strip()
clientes["ciudad"] = clientes["ciudad"].replace('', 'Desconocida').str.title()
clientes["activo"] = clientes["activo"].str.upper()
print_header('clientes con datos de texto limpiados (muestra)')
print(f"Antes  - ciudad nulas/vacias: {ciudad_nulos_antes:d}")
print(f"Después- ciudad 'Desconocida': {(clientes['ciudad'] == 'Desconocida').sum():d}")
print(clientes.head().to_string(index=False))

# Guardar originales para mostrar antes/después
orig_clientes_fecha = clientes['fecha_registro'].copy()
orig_ventas_fecha = ventas['fecha_venta'].copy()

# Conversión sencilla.
clientes["fecha_registro"] = pd.to_datetime(clientes["fecha_registro"], dayfirst=True, errors='coerce')
ventas["fecha_venta"] = pd.to_datetime(ventas["fecha_venta"], dayfirst=True, errors='coerce')

print_header('Clientes fecha_registro: Antes / Después (resumen)')
print(f"Antes  - no nulos: {orig_clientes_fecha.notna().sum():d}")
print(f"Después- no nulos: {clientes['fecha_registro'].notna().sum():d}")

print_header('Ventas fecha_venta: Antes / Después (resumen)')
print(f"Antes  - no nulos: {orig_ventas_fecha.notna().sum():d}")
print(f"Después- no nulos: {ventas['fecha_venta'].notna().sum():d}")


print_header('clientes y ventas con fechas convertidas')
print("Mostrando información del DataFrame 'clientes' con fechas convertidas:")
clientes.info()
print("Mostrando información del DataFrame 'ventas' con fechas convertidas:")
ventas.info()

