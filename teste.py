import sqlite3

db_name = 'livraria_hjm.db'

connection = sqlite3.connect(db_name)

cursor = connection.cursor()

query = '''
    SELECT DISTINCT titulo
    FROM livros
'''

titulos = cursor.execute(query).fetchall()

cursor.close()

connection.close()

print(titulos)
