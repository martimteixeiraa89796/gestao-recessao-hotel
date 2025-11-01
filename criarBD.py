import sqlite3

# Para iniciar a base de dados, primeiro é necessário conectar à mesma.
# Se a base de dados não existir, ela será criada automaticamente.
sqliteConnection = sqlite3.connect('basedados.db')
cursor = sqliteConnection.cursor()  # O Cursor server para interagir com a base de dados.

# Esta string é onde vai ser escrido o SQL para a criação da base de dados.
# É necessário criar tabelas, mas terão de estar vazias pois o nosso programa é o que vai adicionar dados à mesma.
query = """
    Escrever SQL para criação da base de dados aqui
"""

# Isto simplesmente executa o código que colocamos na string acima.
# Para adicionar dados ou apagar dados, é necessário usar a função .commit() após execução. 
cursor.execute(query)

# No final, fechar a conecção coma base de dados para não se perder dados em caso de acidente.
cursor.close()