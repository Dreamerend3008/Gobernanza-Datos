# Taller 2: Calidad de Datos

**Colaboradores:**  
- Juan Andrés Bravo Mejía (Desarrollador principal)

El objetivo de este taller fue desarrollar un ejercicio de calidad de datos en donde, a partir de un dataset proporcionado, se identificaran las diferentes problemáticas de la recolección y uso de los datos.

## Paso a paso del proceso de limpieza

1. Se importaron los datasets que estaban en formato .txt y se realizó un proceso de unión efectiva de los datasets.  
    **[dataUnion.py]**

2. Se realizó un análisis exploratorio inicial para reconocer las dimensiones que queríamos atacar para mejorar el análisis de los datos.  
    **[eda.ipynb]**

3. Se realizó un proceso de limpieza y estandarización de los datos, en donde se obtuvo el resultado de un nuevo dataset listo para el análisis (**[/datasets/cleanData.csv]**). Todo esto fue desarrollado en un cuaderno en Jupyter (toda la información específica se encuentra dentro de este).  
    **[main.ipynb]**

4. Se realizó otro análisis exploratorio del dataset limpio para verificar la consistencia de este.  
    **[report.ipynb]**

5. Se usó la inteligencia artificial Claude Sonnet 4 para crear un sistema de puntaje de los datasets que genera un chequeo previo para saber la necesidad de aplicar la limpieza ya automatizada.  
    **[scoring_system.ipynb]**

6. Se implementó una política de gobierno de datos para asegurarse de una buena operatividad de estos a futuro, para la optimización de análisis.  
    **[politica_gobierno_de_datos.md]**

*La documentación del documento se encuentra en ingles por practicas de programación del desarrollador del repositorio*