import pandas as pd
import numpy as np
from typing import Dict, List, Any, Tuple

# Column groups based on business logic

produccion = ["VENTA", "BRUTA", "CONSUI", "AGREGA", "CTO"]

expenses_op = ["GAS","EMPAQUE","HONORA","COMISION","ARRIENDO","SEGURO",
             "ASEO","ENERGIA","COMUNICA","PUBLICO","FLETES","PUBLICI",
             "ADECUA","REGALA","OUTSOURCING","OTROS"]
general_G = ['GASTOS','GASTOSNOP','GASTOPNOP','CTOINS']
# produccion
def rule_nuls(df: pd.DataFrame) -> dict:
    nuls = df[produccion+expenses_op].isnull()
    return {
        'cantidad': nuls.any(axis=1).sum(),
        'filas': df[nuls.any(axis=1)],
        'porcentaje': nuls.any(axis=1).mean() * 100
    }
def rule_venta_produccion(df: pd.DataFrame):
    invalid = (df['BRUTA'] > df['VENTA']*1.05)
    return{
        'cantidad': invalid.sum(),
        'filas': df[invalid],
        'porcentaje': invalid.mean()*100
    }
def rule_produccion_consumo(df: pd.DataFrame):
    invalid = (df['BRUTA'] < df['CONSUI'])
    return{
        'cantidad': invalid.sum(),
        'filas': df[invalid],
        'porcentaje': invalid.mean()*100
    }
def rule_val_agregado(df: pd.DataFrame):
    invalid = (df['AGREGA'] < df['BRUTA'] - df['CONSUI'])
    return{
        'cantidad': invalid.sum(),
        'filas': df[invalid],
        'porcentaje': invalid.mean()*100
    }
def rule_costos(df: pd.DataFrame):
    invalid = ( df['CTOINS'] < df['CTO'])
    return{
        'cantidad': invalid.sum(),
        'filas': df[invalid],
        'porcentaje': invalid.mean()*100
    }
def rule_eficiencia(df: pd.DataFrame):
    invalid = (df['VENTA']<df['CTOINS'])
    return{
        'cantidad': invalid.sum(),
        'filas': df[invalid],
        'porcentaje': invalid.mean()*100
    }
def rule_margen_val_agregado(df: pd.DataFrame):
    invalid = ~((0<=df['AGREGA']) & (df['AGREGA'] <= df['VENTA']))
    return{
        'cantidad': invalid.sum(),
        'filas': df[invalid],
        'porcentaje': invalid.mean()*100
    }
# expenses_op
def rule_consistencial_total(df: pd.DataFrame):
    invalid = df[general_G].sum(axis=1) < df[expenses_op].sum(axis=1)
    return{
        'cantidad': invalid.sum(),
        'filas': df[invalid],
        'porcentaje': (invalid).mean()*100
    }
def rule_proporcion_ventas(df: pd.DataFrame):
    invalid = (df['GASTOS'] > df['VENTA'])
    return{
        'cantidad': invalid.sum(),
        'filas': df[invalid],
        'porcentaje': (invalid).mean()*100
    }
def rule_peso_relativo_gastos(df: pd.DataFrame):
    invalid = (df[expenses_op].div(df['GASTOS'], axis=0) > 0.5).any(axis=1)
    return{
        'cantidad': invalid.sum(),
        'filas': df[invalid],
        'porcentaje': (invalid).mean()*100
    }
def rule_rentabilidad_bruta(df: pd.DataFrame):
    invalid = ((df['VENTA']-df['CTOINS']) < 0)
    return{
        'cantidad': invalid.sum(),
        'filas': df[invalid],
        'porcentaje': (invalid).mean()*100
    }
rules = {
    'nulos': rule_nuls,
    'venta_produccion': rule_venta_produccion,
    'produccion_consumo': rule_produccion_consumo,
    'valor_agregado': rule_val_agregado,
    'costos': rule_costos,
    'eficiencia': rule_eficiencia,
    'margen_val_agregado': rule_margen_val_agregado,
    'consistencia_gastos': rule_consistencial_total,
    'proporcion_ventas': rule_proporcion_ventas,
    'peso_relativo_gastos': rule_peso_relativo_gastos,
    'rentabilidad_bruta': rule_rentabilidad_bruta
}
def validador(df: pd.DataFrame, rules_dict: dict):
    resultados = []
    for nombre, funcion in rules_dict.items():
            r = funcion(df)
            resultados.append({
                'regla': nombre,
                'cantidad_invalidos': r['cantidad'],
                'porcentaje_invalidos': round(r['porcentaje'], 2)
            })
    return pd.DataFrame(resultados)