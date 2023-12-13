# Análisis de Datos y Carga en MySQL

## Descripción

Este script de Python realiza un análisis de datos a partir de dos conjuntos de datos, uno remoto y otro local. Luego, carga los datos analizados en una base de datos MySQL local. Se utilizan diversas bibliotecas como pandas, matplotlib y seaborn para el análisis exploratorio y la visualización de datos.

## Requisitos

- Python 3.x
- pandas
- matplotlib
- seaborn
- sqlalchemy

### Asegúrate de tener las bibliotecas instaladas ejecutando el siguiente comando:
`pip install pandas matplotlib seaborn sqlalchemy`


## Ejecución del Script
Para ejecutar el script, asegúrate de tener la base de datos MySQL configurada y luego ejecuta:
`python Limpieza.py`


# Funcionalidades del Script

## Análisis de Datos Remotos:
* Descarga un conjunto de datos remoto desde una URL.
* Realiza un análisis exploratorio de datos y elimina registros faltantes.
* Genera visualizaciones de datos utilizando gráficos de caja y barras.

## Análisis de Datos Locales:
* Lee un conjunto de datos local desde un archivo CSV.
* Realiza un análisis exploratorio de datos y elimina registros faltantes.
* Realiza manipulaciones de datos, como cambiar mayúsculas y unir tablas.

## Unión de Datos y Exportación:
* Une los conjuntos de datos remotos y locales utilizando la columna "Country".
* Elimina registros con valores nulos o cero en la columna "codigo_departamento".
* Exporta el resultado a un archivo CSV llamado "Result.csv".

## Carga en MySQL:
* Establece una conexión a una base de datos MySQL local.
* Divide los datos en lotes y los inserta en la base de datos.
* Maneja posibles errores, como claves duplicadas, y realiza reintentos.

## Notas Importantes
* Asegúrate de configurar la conexión a tu base de datos MySQL con las credenciales adecuadas.
* Personaliza las rutas de los archivos y otros parámetros según tus necesidades.
## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.



