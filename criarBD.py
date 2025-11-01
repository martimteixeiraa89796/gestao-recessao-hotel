import sqlite3

sqliteConnection = sqlite3.connect('basedados.db')
cursor = sqliteConnection.cursor()

query = """
    Escrever SQL para criação da base de dados aqui
"""

cursor.execute(query)
cursor.close()