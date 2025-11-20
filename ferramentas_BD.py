"""
Módulo de interação com bases de dados SQLite
---------------------------------------------

Este módulo faz a ligação com os ficheiros **.bd** que contém a base de dados da aplicação.
É utilizado como ponte entre as *queries* SQL e a sua execução na base de dados.
"""

import sqlite3  #Módulo já vem instalado com Python
from funcoes_sqlite_select import select_geral


def executarBD(query, query_dados=(), header_only=False, imprimir=False):
    """
    Executa queries na base de dados.
    
    Cria-se um cursor para se poder interagir com a base de dados.
    Se a query enviar um resultado, o mesmo fica guardado, caso contrário fica **None**.
    Após a execução, faz um commit das ações das queries.

    Caso for necessário, esta também chama uma função para imprimir tabelas formatadas.

    :param query: A query para ser executada na base de dados
    :type query: string

    :param imprimir: Se deve ou não imprimir tabelas
    :type imprimir: boolean

    :return: Resultado da *query*
    :rtype: list

    :raise sqlite3.Error: Se ocorrer algum erro durante a criação do cursor ou na execução

    Exemplo de execução de querie com impressão de tabela:
    
    >>> basedados.executar("SELECT * FROM Tabela;", imprimir=True)
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


def listar_campos(tabela):
    campos = []
    for linha in executarBD(select_geral(tabela), header_only=True):
        campos.append(linha[0])

    print("Campos disponíveis:")
    for numero_campo in range(len(campos)):
        print(f"    {numero_campo + 1}. {campos[numero_campo]}".title())

    return campos


def listar_tabelas():
    tabelas = []
    for linha in executarBD("SELECT name FROM sqlite_master WHERE type='table'"):
        tabelas.append(linha[0])
    
    tabelas.pop()

    print("Tabelas disponíveis:")
    for numero_tabela in range(len(tabelas)):
        print(f"    {numero_tabela + 1}. {tabelas[numero_tabela]}".title())

    return tabelas


def campos_escolha(tabela):
    campos = listar_campos(tabela)

    while True:
        escolha = int(input("escolha um campo: "))

        if 0 < escolha <= len(campos):
            break

        else:
            print("Campo não disponivel")
    
    return campos[escolha-1]


def tabela_escolha():
    tabelas = listar_tabelas()

    while True:
        escolha = int(input("escolha uma tabela: "))

        if 0 < escolha <= len(tabelas):
            break

        else:
            print("Campo não disponivel")

    return tabelas[escolha-1]