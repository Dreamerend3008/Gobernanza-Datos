import pandas as pd

files_path = [f'datasets/ConjuntoDatos_MedidoresAgua/ConjuntoDatos_{i}_{i*50}.txt' for i in range(1, 11)]
final_file_path = 'datasets/data.csv'

# df[0] porque unicamente este tiene los headers
df = [] 
df.append(pd.read_csv(files_path[0], sep=','))

for i in files_path[1:]:
    dftmp = pd.read_csv(i, sep=',', header=None, names=df[0].columns)
    df.append(dftmp)
    
df_u = pd.concat(df, ignore_index=True)


# lo que hace es filtrar cada linea en si la columna 'No' tiene algun digito asi filtramos los titulos
df_u = df_u[df_u['No'].apply(lambda x: str(x).isdigit())]

df_u.to_csv(final_file_path, index=False)

print("Succesfull!!")