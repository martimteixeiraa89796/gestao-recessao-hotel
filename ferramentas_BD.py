"""
Módulo de interação com bases de dados SQLite
---------------------------------------------

Este módulo faz a ligação com os ficheiros **.bd** que contém a base de dados da aplicação.
É utilizado como ponte entre as *queries* SQL e a sua execução na base de dados e obter dados da mesma.
"""

import sqlite3  #Módulo já vem instalado com Python


def executarBD(query, query_dados=(), header_only=False, imprimir=False):
    """
    Executa queries na base de dados.
    
    Esta função cria uma conecção ao ficheiro de base de dados SQLite e, caso não exista, o mesmo é criado.
    Após a ligação, é criado o leitor e o cursor para se poder interagir dentro da base de dados.
    Se houver alterações feitas à base de dados, esta função também as guarda.
    Caso seja feito um select, esta função também consegue imprimir os resultado com a ajuda de uma função adjacente.
    No final das operções, a função desconecta-se da base de dados.

    :param query: A query para ser executada na base de dados
    :type query: string

    :param query_dados: Tuple com variáveis a serem introduzidas na query.
    :type query_dados: tuple

    :param header_only: Faz com que a função retorne apenas os headers das tabelas
    :type header_only: boolean

    :param imprimir: Se deve ou não imprimir tabelas
    :type imprimir: boolean

    :return: Por padrão, a função retorna o conteudo de tabelas, mas pode ser alterado para apenas retornar os headers das mesmas.
    :rtype: list

    :raise sqlite3.Error: Se ocorrer algum erro durante a execução de ações do módulo SQLite.

    Exemplo de execução de querie com impressão de tabela:
    
    >>> executarBD("SELECT * FROM Tabela;", imprimir=True)
    """
    
    #Fazer conecção com base de dados
    try:
        sqlconnector = sqlite3.connect(f'basedados.db')
    
    except sqlite3.Error:
        print("Ocorreu um erro ao tentar conectar à base de dados.")

    try:
        cursor = sqlconnector.cursor()  #Criar cursor para interagir com base de dados
    
    except sqlite3.Error:
        print("Ocorreu um erro ao tentar criar cursor.")

    #Executar comandos sql
    try:
        cursor.execute(str(query), query_dados)
        sqlconnector.commit()  #Fazer commit das ações

        if imprimir:
            imprimir_tabela(cursor.description, cursor.fetchall())
        
        if header_only:
            resultado = cursor.description

        else:
            resultado = cursor.fetchall()  #Retirar todas as linhas e guardar na variável
        
        return resultado
        
    except sqlite3.Error:
        print("Ocorreu um erro ao executar commandos SQL.")

    #Deconectar base de dados
    try:
        sqlconnector.close()
        sqlconnector = None
        
    except sqlite3.Error:
        print("Ocorreu um erro ao tentar desconectar base de dados.")


def imprimir_tabela(headers, dados):
    """
    Imprime tabelas de forma formatada.

    Uma vez que o resultado que advém da execução de queries que devolvem tabelas é uma lista com tuples,
    para que o utilizador perceba o que está a ser apresentado, o resultado tem de ser formatado.

    Para tal, este método faz a iteração pelos *headers* (cabeçalhos) e dados para encontrar aquele com maior comprimento.
    Estes comprimentos são depois guardados numa lista para serem usados na construção das colunas da tabela.
    Quando os dados necessários para a construção da tabelas estiverem prontos, são construídas strings para cada linha da tabela,
    que são depois guardados numa lista, prontos para serem impressos.

    Uma limitação do método, é que os header têm de estar no mesmo formato que o módulo **sqlite** fornece em **cursor.description**.

    :param headers: Headers (cabeçalhos) da tabela, cada valor deve estar numa lista/tuple
    :type headers: list

    :param dados: Lista de dados retirados de uma tabela, organizados por linha
    :type dados: list

    Exemplo com dados retirados de queries:

    >>> imprimir_tabela(cursor.description, cursor.fetchall())

    Exemplo com dados externos:

    >>> imprimir_tabela([("Idade"), ("Nome"), ("Contacto")],
                        [(21, "João", 999999999),
                        (23, "Mariana", 888888888)
                        ])
    """

    headers_listados = []
    comprimento_listado = []

    #Listar headers
    for linha in headers:
        headers_listados.append(linha[0])

    #Calcular comprimento para cada coluna
    for coluna in range(len(headers_listados)): #Iterar pelas colunas horizontalmente
        comprimento_celula = len(str(headers_listados[coluna]))
        
        for linha in dados: #Iterar pelas linhas verticalmente
            novo_comprimento = len(str(linha[coluna])) #Celula

            if comprimento_celula < novo_comprimento:
                comprimento_celula = novo_comprimento

        comprimento_listado.append(comprimento_celula)

    #Contruir tabela
    tabela = []
    tabela.append(headers_listados)
    
    for linha in dados:
        tabela.append(linha)

    #Formatar tabela
    tabela_formatada = []

    for linha in tabela:
        nova_linha = "| "
        for coluna in range(len(linha)):
            formatado = str(linha[coluna]) + " "*(comprimento_listado[coluna]-len(str(linha[coluna])))
            nova_linha += formatado + " | "
        tabela_formatada.append(nova_linha)

    #imprimir tabela
    for linha in tabela_formatada:
        print(linha)


def get_campos(tabela):
    """
    Retorna uma lista com campos de uma tabela na base de dados.

    Esta função acede à base de dados e retorna os campos/colunas de uma tabela.
    Isto é feito através da função executarBD e mandá-la retornar apenas os headers das tabelas.

    :param tabela: O nome da tabela que se pretende obter os campos
    :type tabela: string

    :return: Os nomes dos campos de uma tabela
    :rtype: list

    Exemplo de obtenção de campos:

    >>> get_campos("Tb_Clientes")
    """
    
    campos = []
    for linha in executarBD(f"SELECT * FROM {tabela};", header_only=True):
        campos.append(linha[0])

    return campos


def get_tabelas():
    """
    Retorna uma lista com o nome das tabelas na base de dados.

    Esta função acede à base de dados e retorna os nomes das tabelas na base de dados.
    Isto é feito através do executarBD, com uma *query **select*** que verifica a tabela master.
    Esta função remove da lista tabelas de sistema.

    :return: Os nomes das tabela na base de dados
    :rtype: list

    Exemplo de obtenção de campos:

    >>> get_tabelas()
    """

    tabelas = []
    for linha in executarBD("SELECT name FROM sqlite_master WHERE type='table'"):
        tabelas.append(linha[0])
    
    try:
        tabelas.remove("sqlite_sequence")
    except ValueError:
        pass

    return tabelas