# **Política de Gobierno de Datos - Sistema de Medición de Agua**

## **1. Propósito y Alcance**

### **1.1. Propósito**
Garantizar la calidad, consistencia y confiabilidad de los datos de medición de agua para soportar modelos predictivos y operaciones de mantenimiento.

### **1.2. Alcance**
- Sistemas de captura de datos de medidores
- Procesos ETL y transformación  
- Almacenamiento y análisis de datos
- Modelos de machine learning predictivo

## **2. Estándares de Calidad de Datos**

### **2.1. Dimensiones de Calidad**
| Dimensión | Estándar | Umbral Aceptable |
|-----------|----------|------------------|
| Completitud | Datos completos por variable | ≥95% numéricos, ≥98% categóricos |
| Exactitud | Valores dentro de rangos definidos | 0-1000 m³ para lecturas |
| Consistencia | Formatos estandarizados | No conclictos de formato |
| Validez | Valores alineados con diccionarios | 100% categorías válidas |

### **2.2. Diccionarios de Datos Controlados**
- **Type of Contract**: residential, comercial, industrial
- **Reading Frequency**: monthly, bimonthly  
- **Reading Validity**: true, false
- **Certification ERP**: true, false


## **3. Sistema de Monitoreo Continuo**

### **3.1. Checks Automatizados de Calidad**
```python
# Validaciones realizadas en el archivo .py
# scoring_system.ipynb

```

### **3.2. Scoring de Calidad en Tiempo Real**
- **Excelente**: 90-100 puntos
- **Bueno**: 70-89 puntos  
- **Aceptable**: 50-69 puntos
- **Crítico**: < 50 puntos

## **4. Protocolos de Actuación**

### **4.1. Para Datos Faltantes**
1. Identificar la categoria
2. Revisar el set de reglas para saber si es un dato que puede estar nulo
4. Analizar la posibilidad de uso de estrategia de estandarización
4. Documentar proceso

### **4.2. Para Valores Atípicos**  
1. Verificar valores con el set de reglas
2. Aplicar estandarización si es error
3. Reportar si es perjudicial

### **4.3. Para Categorías Inválidas**
1. Agregar a diccionario si es válido
2. Rechazar el dataset si es invalido
3. Notificar la inconsistencia de formato

## **5. Auditoría y Mejora Continua**

### **5.1. Revisiones Periódicas**
- Mensual: Reporte de métricas de calidad
- Trimestral: Revisión de diccionarios
- Anual: Auditoría completa de políticas

### **5.2. Proceso de Mejora**  
1. Medir desempeño contra estándares
2. Identificar desviaciones y causas
3. Implementar acciones correctivas
4. Verificar efectividad

---
