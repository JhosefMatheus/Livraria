import pandas as pd

df = pd.read_csv('autores_livros.csv')

autores = df['autor'].to_list()

print(autores)
