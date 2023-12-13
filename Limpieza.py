# Importar librerías
from sqlite3 import IntegrityError
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Lectura Archivo remoto
ruta = "https://seminario2.blob.core.windows.net/fase1/global.csv?sp=r&st=2023-12-06T03:45:26Z&se=2024-01-04T11:45:26Z&sv=2022-11-02&sr=b&sig=xdx7LdUOekGyBvGL%2FNE55ZZj9SBvCC%2FWegxtpSsKjJg%3D"
data = pd.read_csv(ruta)

# Conteo Datos
print(data.shape)
data.head()

# Quitar Datos Faltantes
data.dropna(inplace=True)
data.info()


# Conteo de los niveles en las diferentes columnas categóricas
cols_cat = ['Date_reported', 'Country_code', 'Country', 'WHO_region', 'New_cases', 'Cumulative_cases', 'New_deaths', 'Cumulative_deaths']

for col in cols_cat:
  print(f'Columna {col}: {data[col].nunique()} subniveles')
#datos numericos
data.describe()
# Repetidas
print(f'Tamaño del set antes de eliminar las filas repetidas: {data.shape}')
data.drop_duplicates(inplace=True)
print(f'Tamaño del set después de eliminar las filas repetidas: {data.shape}')


# Generar gráficas individuales pues las variables numéricas
# están en rangos diferentes
cols_num = ['New_cases', 'Cumulative_cases' , 'Cumulative_deaths',  'New_deaths']

fig, ax = plt.subplots(nrows=4, ncols=1, figsize=(8,30))
fig.subplots_adjust(hspace=0.5)

for i, col in enumerate(cols_num):
    sns.boxplot(x=col, data=data, ax=ax[i])
    ax[i].set_title(col)

# Graficar los subniveles de cada variable categórica
cols_cat = ['Country_code', 'Country', 'WHO_region']

fig, ax = plt.subplots(nrows=3, ncols=1, figsize=(10,30))
fig.subplots_adjust(hspace=1)

for i, col in enumerate(cols_cat):
  sns.countplot(x=col, data=data, ax=ax[i])
  ax[i].set_title(col)
  ax[i].set_xticklabels(ax[i].get_xticklabels(),rotation=30)


# Lectura Archivo Local
ruta2 = "municipio.csv"
data2 = pd.read_csv(ruta2)

# Conteo Datos
print(data2.shape)
data2.head()

#Repetidos
data2.dropna(inplace=True)
data2.info()


# Conteo de los niveles en las diferentes columnas categóricas
cols_cat2 = ['departamento', 'codigo_departamento', 'municipio', 'codigo_municipio', 'poblacion']

for col2 in cols_cat2:
  print(f'Columna {col2}: {data2[col2].nunique()} subniveles')

data2.describe()

#Quitar Duplicados
print(f'Tamaño del set antes de eliminar las filas repetidas: {data2.shape}')
data2.drop_duplicates(inplace=True)
print(f'Tamaño del set después de eliminar las filas repetidas: {data2.shape}')

#Cambiar Columna departamento inicio mayuscula siguientes minusculas
data2['departamento'] = data2['departamento'].apply(lambda x: x.title())

#Cambiar titulo columna departamento a Country
data2 = data2.rename(columns={'departamento': 'Country'})

#Unir las 2 tablas con indice Country
merged = pd.merge(data, data2, on='Country', how='outer')

# Eliminar filas donde departamento sea Nulo
print(f'Tamaño del set antes de eliminar registros: {merged.shape}')
merged = merged[merged['codigo_departamento']>0]
print(f'Tamaño del set después de eliminar registros: {merged.shape}')

#Eliminar Filas donde no exista date
merged = merged.dropna(subset=['Date_reported'])
#Imprimimos tala merge
print(merged)
#Creamos Ruta
ruta = "Result.csv"
#Exportamos Archivo
merged.to_csv(ruta, index=False)
#Creamos dataFrame
df = pd.DataFrame(merged)

# Establecer la conexión a la base de datos MySQL
engine = create_engine('mysql://root:@localhost/seminario2')

# Especificar el tamaño del lote
tamanio_lote = 50
# Inicializar la lista de lotes con error
lotes_con_error = []
# Dividir el DataFrame en lotes más pequeños
lotes_df = [df[i:i + tamanio_lote] for i in range(0, len(df), tamanio_lote)]

# Iterar sobre los lotes y pasarlos a la base de datos 
for lote_df in lotes_df:
    try:
        # Intentar insertar el lote en la base de datos
        lote_df.to_sql(name='carga', con=engine, if_exists='append', index=False)
        print(f"Lote insertado en la base de datos.")
    except IntegrityError as e:
        # Manejar la excepción de integridad (por ejemplo, clave duplicada)
        print(f"Error de integridad: {e}")
        lotes_con_error.append(lote_df)
    except Exception as e:
        # Manejar otras excepciones
        print(f"Error durante la inserción: {e}")


# Intentar insertar los lotes con error nuevamente
for lote_con_error in lotes_con_error:
    try:
        lote_con_error.to_sql(name='carga', con=engine, if_exists='append', index=False)
        print(f"Reintento de lote insertado en la base de datos.")
    except Exception as e:
        print(f"Error durante el segundo intento de inserción: {e}")

    