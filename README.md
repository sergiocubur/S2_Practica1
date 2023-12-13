Proceso de Análisis de Datos y Carga en Base de Datos
Este script de Python realiza varias operaciones de análisis de datos utilizando la biblioteca pandas y matplotlib, y luego carga los datos en una base de datos MySQL utilizando SQLAlchemy.

Requisitos
Python 3.x
pandas
matplotlib
seaborn
SQLAlchemy
Instala las bibliotecas necesarias con:

bash
Copy code
pip install pandas matplotlib seaborn sqlalchemy
Análisis de Datos
Archivo Remoto
Lectura de Archivo Remoto: El script lee un archivo CSV remoto desde https://seminario2.blob.core.windows.net/fase1/global.csv.

Conteo de Datos: Imprime la forma y las primeras filas del DataFrame.

Manejo de Datos Faltantes: Elimina filas con valores faltantes.

Conteo de Niveles en Columnas Categóricas: Muestra el número de subniveles únicos en ciertas columnas categóricas.

Estadísticas Descriptivas: Imprime estadísticas descriptivas para las columnas numéricas.

Eliminación de Filas Repetidas: Elimina filas duplicadas del DataFrame.

Visualización de Datos
Gráficos Boxplot: Genera gráficos boxplot para variables numéricas.

Gráficos de Barras: Muestra gráficos de barras para variables categóricas.

Archivo Local
Lectura de Archivo Local: Lee un archivo CSV local llamado "municipio.csv".

Conteo de Datos: Imprime la forma y las primeras filas del DataFrame.

Manejo de Datos Faltantes: Elimina filas con valores faltantes.

Conteo de Niveles en Columnas Categóricas: Muestra el número de subniveles únicos en ciertas columnas categóricas.

Estadísticas Descriptivas: Imprime estadísticas descriptivas para las columnas numéricas.

Eliminación de Filas Repetidas: Elimina filas duplicadas del DataFrame.

Manipulación de Datos: Cambia las mayúsculas y minúsculas en la columna "departamento" y renombra la columna a "Country".

Unión de Tablas: Fusiona los dos DataFrames utilizando la columna "Country" como índice.

Eliminación de Registros Nulos: Elimina filas donde la columna "codigo_departamento" es nula.

Eliminación de Filas Nulas en la Columna "Date_reported": Elimina filas nulas en la columna "Date_reported".

Exportación de Datos Fusionados: Exporta los datos fusionados a un archivo CSV llamado "Result.csv".

Carga en Base de Datos MySQL
Conexión a la Base de Datos: Se conecta a una base de datos MySQL llamada "seminario2" localmente.

División de Datos en Lotes: Divide el DataFrame fusionado en lotes más pequeños para facilitar la carga.

Inserción de Lotes en la Base de Datos: Itera sobre los lotes y los inserta en la tabla "carga". Maneja excepciones, como errores de integridad, e intenta nuevamente si hay errores.

Notas
Asegúrate de tener las bibliotecas necesarias instaladas antes de ejecutar el script.
Personaliza las rutas de los archivos y las credenciales de la base de datos según tus necesidades.
