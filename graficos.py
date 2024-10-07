import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

# Cargar el dataset limpio
df = pd.read_csv('preciocasas_limpiado.csv')

# Configuración de estilo para las gráficas
sns.set(style="whitegrid")

# Función para formatear los valores en CLP sin notación científica
def format_price_axis(ax):
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: f'{int(y):,}'))

# Histograma de la distribución del Precio (CLP)
plt.figure(figsize=(10, 6))
ax = sns.histplot(df['Precio'], bins=30, kde=True, color='blue')
format_price_axis(ax)
plt.title('Distribución de los Precios de las Propiedades (CLP)')
plt.xlabel('Precio (CLP)')
plt.ylabel('Frecuencia')
plt.show()

# Histograma de la distribución del número de dormitorios
plt.figure(figsize=(10, 6))
sns.histplot(df['Dormitorios'], bins=10, kde=False, color='green')
plt.title('Distribución del Número de Dormitorios')
plt.xlabel('Número de Dormitorios')
plt.ylabel('Frecuencia')
plt.show()

# Histograma de la distribución del número de baños
plt.figure(figsize=(10, 6))
sns.histplot(df['Banos'].dropna(), bins=10, kde=False, color='orange')
plt.title('Distribución del Número de Baños')
plt.xlabel('Número de Baños')
plt.ylabel('Frecuencia')
plt.show()

# Gráfico de dispersión entre Área Total y Precio
plt.figure(figsize=(10, 6))
ax = sns.scatterplot(x='Area Total', y='Precio', data=df, color='purple')
format_price_axis(ax)
plt.title('Relación entre Área Total y Precio')
plt.xlabel('Área Total (m²)')
plt.ylabel('Precio (CLP)')
plt.show()

# Gráfico de dispersión entre Dormitorios y Precio
plt.figure(figsize=(10, 6))
ax = sns.scatterplot(x='Dormitorios', y='Precio', data=df, color='red')
format_price_axis(ax)
plt.title('Relación entre Número de Dormitorios y Precio')
plt.xlabel('Número de Dormitorios')
plt.ylabel('Precio (CLP)')
plt.show()

# Gráfico de dispersión entre Área Construida y Precio
plt.figure(figsize=(10, 6))
ax = sns.scatterplot(x='Area Construida', y='Precio', data=df, color='brown')
format_price_axis(ax)
plt.title('Relación entre Área Construida y Precio')
plt.xlabel('Área Construida (m²)')
plt.ylabel('Precio (CLP)')
plt.show()

# Histograma de la distribución del Área Construida
plt.figure(figsize=(10, 6))
sns.histplot(df['Area Construida'].dropna(), bins=30, kde=True, color='teal')
plt.title('Distribución de Área Construida de las Propiedades')
plt.xlabel('Área Construida (m²)')
plt.ylabel('Frecuencia')
plt.show()

# Histograma de la distribución del Área Total
plt.figure(figsize=(10, 6))
sns.histplot(df['Area Total'].dropna(), bins=30, kde=True, color='purple')
plt.title('Distribución de Área Total de las Propiedades')
plt.xlabel('Área Total (m²)')
plt.ylabel('Frecuencia')
plt.show()

# Histograma de la distribución de Estacionamientos
plt.figure(figsize=(10, 6))
sns.histplot(df['Estacionamientos'].dropna(), bins=10, kde=False, color='blue')
plt.title('Distribución de Estacionamientos')
plt.xlabel('Número de Estacionamientos')
plt.ylabel('Frecuencia')
plt.show()
