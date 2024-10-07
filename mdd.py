import pandas as pd
from scipy import stats

# Leer un archivo CSV
df = pd.read_csv('preciocasas.csv')

# Renombrar las cabeceras
df = df.rename(columns={'Price_CLP': 'Precio', 'Dorms': 'Dormitorios', 'Baths': 'Banos', 
                        'Built Area': 'Area Construida', 'Total Area': 'Area Total', 
                        'Parking': 'Estacionamientos'})

# Quitar filas vacías
df = df.dropna(how='all')

# Quitar duplicados
df = df.drop_duplicates()

# Reemplazar nombres de comunas
df['Comuna'] = df['Comuna'].replace({'EstaciónCentral': 'Estacion Central', 'Maipú': 'Maipu', 
                                      'Ñuñoa': 'Nunoa', 'Peñalolen': 'Penalolen', 'SanRamón': 'San Ramon',
                                      'Conchalí': 'Conchali', 'Peñaflor': 'Penaflor', 'Curacaví': 'Curacavi'})

# Eliminar columnas no necesarias
df = df.drop(columns=['Price_USD', 'Price_UF', 'id', 'Realtor', 'Ubicacion'])

# Filtrar los outliers en la columna 'Precio'
alpha = 0.004
limite_inferior = df['Precio'].quantile(alpha)
limite_superior = df['Precio'].quantile(1 - alpha)

df = df[(df['Precio'] >= limite_inferior) & (df['Precio'] <= limite_superior)]

# Quitar filas con 'Precio' no numérico o NaN
df['Precio'] = pd.to_numeric(df['Precio'], errors='coerce')
df = df.dropna(subset=['Precio'])

# Filtrar registros donde Área Total sea mayor a 20,000, Área Construida mayor a 2,500, Dormitorios mayor a 15 y Baños mayor a 10
df = df[(df['Area Total'] <= 20000) & (df['Estacionamientos'] <= 50) & (df['Area Construida'] <= 2500) & (df['Dormitorios'] <= 15) & (df['Banos'] <= 10)]

# Mostrar estadísticas después de eliminar registros
print(f"Cantidad de filas después de filtrar: {len(df)}")

# 1. Calcular las frecuencias de la variable dependiente
frecuencias = df['Precio'].value_counts().sort_index()

# 2. Calcular las medidas de tendencia central y dispersión
media = df['Precio'].mean()
mediana = df['Precio'].median()
desv_std = df['Precio'].std()
cuartiles = df['Precio'].quantile([0.25, 0.5, 0.75])

# 3. Calcular los valores mínimos y máximos
minimo = df['Precio'].min()
maximo = df['Precio'].max()

# 4. Resumen estadístico de la variable dependiente
resumen = df['Precio'].describe()

# Mostrar resultados
print(f"Frecuencias:\n{frecuencias}")
print(f"\nMedia: {media}")
print(f"Mediana: {mediana}")
print(f"Desviación Estándar: {desv_std}")
print(f"Cuartiles:\n{cuartiles}")
print(f"Valor Mínimo: {minimo}")
print(f"Valor Máximo: {maximo}")
print(f"\nResumen estadístico:\n{resumen}")

# Opcional: correlación entre la variable dependiente y otras variables
columnas_interes = ['Precio', 'Dormitorios', 'Area Total', 'Estacionamientos', 'Area Construida', 'Banos']

# Calcular la correlación solo para las columnas seleccionadas
correlaciones = df[columnas_interes].corr()['Precio']
print(f"\nCorrelación con las columnas seleccionadas:\n{correlaciones}")

# Guardar el nuevo archivo CSV sin outliers, sin áreas grandes y sin dormitorios o baños excesivos
df.to_csv('preciocasas_limpiado.csv', index=False)

# Información del dataframe final
df.info()
