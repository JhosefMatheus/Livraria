import pandas as pd

df = pd.read_csv('livros.csv')

id = len(df) + 1 if not df['id'].to_list() else df['id'].to_list()[-1] + 1

print(id)
