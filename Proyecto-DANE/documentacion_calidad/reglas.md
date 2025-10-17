# Reglas de Validación

* Estas reglas fueron dieseñadas para la deteccion de valores invalidos dentro del dataset

| Regla | Condición |
|--------|------------|
| nulos | Valores nulos en columnas de producción o gastos |
| venta_produccion | BRUTA > VENTA × 1.05 |
| produccion_consumo | BRUTA < CONSUI |
| valor_agregado | AGREGA != BRUTA − CONSUI |
| costos | CTOINS < CTO |
| eficiencia | VENTA < CTOINS |
| margen_val_agregado | AGREGA fuera de rango (0 <= AGREGA <= VENTA) |
| consistencia_gastos | GASTOS != suma de subcuentas de gastos |
| proporcion_ventas | GASTOS > VENTA |
| peso_relativo_gastos | Algún gasto individual > 50% de GASTOS |
| rentabilidad_bruta | VENTA − CTOINS < 0 |
