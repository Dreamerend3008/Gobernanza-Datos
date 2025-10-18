import pandas as pd
import numpy as np

def data_simulator(df_base: pd.DataFrame, n_filas: int = 1000, ruido_pct: float = 0.05) -> pd.DataFrame:
    df_base = df_base.copy()

    reps = int(np.ceil(n_filas / len(df_base)))
    df_big = pd.concat([df_base] * reps, ignore_index=True).iloc[:n_filas].copy()

    for col in df_big:
        if df_big[col].std() > 0: # verificamos si la columna varia si fuera 0 se rompe
            ruido = np.random.randn(len(df_big)) * ruido_pct
            df_big[col] += ruido
    #df_big = df_big.sample(frac=1, random_state=42).reset_index(drop=True)
    return df_big
