# Proyecto de Análisis de Calidad de Datos - EAC DANE

Este proyecto implementa un sistema de validación de calidad de datos para la Encuesta Anual de Comercio (EAC) del DANE, enfocado en detectar inconsistencias y anomalías en datos empresariales del sector comercio.

## Descripción del Proyecto

El proyecto desarrolla un validador comprehensivo que aplica reglas de negocio y coherencia contable para evaluar la calidad de los datos empresariales. Incluye capacidades de simulación de datos y análisis comparativo de diferentes escenarios de calidad.

## Linea del tiempo del proyecto
* Analisis exploratorio incial ``start_eda.ipynb``
* Creación de funiones validadoras ``**validator.py** ``
* Creación de simulador de datos ``**simulator.py**``
* Analisis de calidad ``analisis_calidad.ipynb``

## Acerca de la limpieza
El dataset proporcionado por el dane, contaba con unos exelentes controles de limpieza de datos, por lo tanto los procesos de limpieza fueron minimos y se buscaron otras perspectivas para analizar las dimensiones de calidad de los datos. Por lo tanto este proyecto toma perspectivas diferentes a las pedidas dentro de los protocolos del proyecto.

## Componentes Principales

### Sistema de Validación
*11 reglas de validación organizadas en algunas de las siguientes categorias:*
- Revisión de parametros nulos
- Verificación de coherencia en producción y ventas
- Proporcionalidad de los gastos
- Revision de valor agregado

### Simulador de Datos
- Generación de datasets sintéticos con errores controlados
- Calibración del sistema con diferentes niveles de calidad
- Pruebas de sensibilidad del validador

### Análisis de Calidad
- Evaluación de 9,984 registros empresariales usando las reglas de validación
- Generación de metricas de calidad detalladas
- Visualización de resultados por categoría

## Resultados del Análisis

Dentro del analsis realizado al dataset, este tuvo un rendimiento excepcional en donde la columna con mayor tasa de error fue la de proporción de ventas con un *1.95%* de columnas invalidas, dado a este resultado se creo una función para la generación de datos sinteticos para analizar el comportamiento de las reglas de validación.

### Problemas Más Frecuentes
1. Inconsistencia en proporción de ventas (1.95% de violaciones)
2. Errores en el calculo del valor agregado (0.96% de violaciones)
3. Incoherencia en relacion de produccion-consumo (0.96% de violaciones)

## Archivos de Datos

### Reporte del analisis exploratorio inicial
Dentro de el archivo `eda_original_dataframe.html` se encuentra el output de la libreria ydata-profiling que nos permitio generar un reporte inicial del conjunto de datos que nos permitio tomar deciiones fundamentales en la direccion del proyecto.

### Documentación de las reglas
El archivo `reglas.md` contiene todas las reglas aplicadas al analsisis de calidad

### Dataset Principal
El archivo `data.csv` contiene 9,984 registros de empresas del sector comercio con variables de:
- Identificación empresarial
- Producción y ventas
- Gastos operacionales y no operacionales
- Personal y remuneración
- Inventarios

### Datos Simulados
- `simulated_Data.csv`: 10,000 registros con tasa de error del 0.1%
- `simulated_invalid_Data.csv`: 5,000 registros con tasa de error del 5%
- `invalidData.csv`: Registros originales que violaron al menos una regla


## Documentación escrita de los procedimientos:

* [Documento diagnostico en Word](https://livejaverianaedu-my.sharepoint.com/:w:/g/personal/sofia_mora_javeriana_edu_co/EcEgkVBwuLtAtg204MRTv1oBIeIgBBCDZ-O8nIyV8DdieQ?e=YiRw14)
* [Diccionario construido para el proyecto](https://livejaverianaedu-my.sharepoint.com/:x:/g/personal/sofia_mora_javeriana_edu_co/ER0du6nP_31MthWXSNCe980BfGQGMChr5qIlQ4bokjmkkg?e=SswcVv)

## Acceso a los Datos Originales

Los datos utilizados en este proyecto están disponibles en el siguiente enlace:  
[https://microdatos.dane.gov.co/index.php/catalog/833/study-description](https://microdatos.dane.gov.co/index.php/catalog/833/study-description)
