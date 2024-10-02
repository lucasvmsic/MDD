import pandas as pd
from scipy import stats

# Leer un archivo CSV
df = pd.read_csv('preciocasas.csv')

# Ver las primeras 5 filas
print(df.head())

#Renombrar las cabeceras
df = df.rename(columns={'Price_CLP': 'Precio','Dorms': 'Dormitorios', 'Baths': 'Banos', 'Built Area': 'Area Construida', 'Total Area': 'Area Total', 'Parking': 'Estacionamientos'})
df.info()
#Quitar filas vacias
df=df.dropna(how='all')
#Quitar duplicados
df=df.drop_duplicates()
#Quitar lineas vacias


# Reemplazar 'QuintaNormal' por 'Quinta Normal' en la columna 'Comuna'
df['Comuna'] = df['Comuna'].replace('EstaciónCentral', 'Estacion Central')
df['Comuna'] = df['Comuna'].replace('Maipú', 'Maipu')
df['Comuna'] = df['Comuna'].replace('Ñuñoa', 'Nunoa')
df['Comuna'] = df['Comuna'].replace('Peñalolen', 'Penalolen')
df['Comuna'] = df['Comuna'].replace('SanRamón', 'San Ramon')
df['Comuna'] = df['Comuna'].replace('Conchalí', 'Conchali')
df['Comuna'] = df['Comuna'].replace('Peñaflor', 'Penaflor')
df['Comuna'] = df['Comuna'].replace('Curacaví', 'Curacavi')

# Eliminar columnas 
df = df.drop(columns=['Price_USD', 'Price_UF', 'id', 'Realtor', 'Ubicacion'])




#Outliers fuera
alpha = 0.004
limite_inferior = df['Precio'].quantile(alpha)
limite_superior = df['Precio'].quantile(1 - alpha)

# Filtrar los valores que estén fuera de estos límites
df = df[(df['Precio'] >= limite_inferior) & (df['Precio'] <= limite_superior)]

# Mostrar estadísticas después de eliminar outliers
print(f"Cantidad de filas después de eliminar outliers: {len(df)}")



df = df.dropna(subset=['Precio'])


# Asegurarse de que la columna 'Precio' sea numérica, eliminando o reemplazando valores no numéricos
df['Precio'] = pd.to_numeric(df['Precio'], errors='coerce')

# Eliminar filas donde 'Precio' no se pudo convertir a número (NaN)
df = df.dropna(subset=['Precio'])


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


# Guardar el nuevo archivo CSV sin outliers
df.to_csv('preciocasas_sin_outliers.csv', index=False)




df.info()

df.to_csv('preciocasas_limpiado.csv', index=False)
