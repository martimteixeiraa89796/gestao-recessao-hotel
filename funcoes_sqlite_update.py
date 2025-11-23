"""
Modulo com funções de atualização de dados
------------------------------------------

Este módulo contém funções para atualizar informações nas tabelas da base de dados SQLite utilizada na aplicação.
"""

from ferramentas_BD import executarBD, get_campos, get_tabelas
import ferramentas_escolha

def update_geral(tabela, campo, novo_dado, campo_condicao, valor):
    """
    Executa um UPDATE dos campos de uma tabela.

    :param tabela: Tabela que se quer atualizar
    :type tabela: string

    :param campo: Campo para ser atualizado
    :tyep campo: string

    :param novo_dado: A nova informação para ser inserida no campo
    :param novo_dado: string, int ou float

    Exemplo de execução:

    >>> update_geral("Cliente", "Nome", "Mário", "ID", 23)
    """

    query = f"""
        update {tabela}
        set {campo} = ?
        where {campo_condicao} = ?
        ;
        """
    
    executarBD(query, (novo_dado, valor))


def update_geral_escolha():
    """
    Menu interativo que permite escolher a tabela no qual permite atualizar.

    Exemplo de execução:

    >>> update_geral_escolha()
    #resultado
    Escolha uma tabela ser alterada.
    Opções disponíveis:
        1. Cliente
        2. Hospede
        3. Quarto
    Escolha uma opção: 1
    Escolha um campo para alterar.
    Opções disponíveis:
        1. Nome
        2. NIF
        3. Telefone
    Escolha uma opção: 1
    Insira dado novo.
    --> João
    Escolha formato.
    Opções disponíveis:
        1. Sql Int
        2. Sql Decimal
        3. Sql String
    Escolha uma opção: 3
    Escolha um campo de condição.
    Opções disponíveis:
        1. Nome
        2. NIF
        3. Telefone
    Escolha uma opção: 2
    Insira valor de condição.
    --> 48394839
    Escolha formato.
    Opções disponíveis:
        1. Sql Int
        2. Sql Decimal
        3. Sql String
    Escolha uma opção: 1
    """

    tabela_lista = get_tabelas()
    
    print("Escolha uma tabela ser alterada.")
    ferramentas_escolha.listar_escolhas(tabela_lista)
    tabela = ferramentas_escolha.fazer_escolha(tabela_lista)

    campo_lista = get_campos(tabela)
    print("Escolha um campo para alterar.")
    ferramentas_escolha.listar_escolhas(campo_lista)
    campo = ferramentas_escolha.fazer_escolha(campo_lista)
    
    print("Insira dado novo.")
    novo_dado = ferramentas_escolha.sql_escolher_tipo()
    
    print("Escolha um campo de condição.")
    ferramentas_escolha.listar_escolhas(campo_lista)
    campo_condicao = ferramentas_escolha.fazer_escolha(campo_lista)

    print("Insira valor de condição.")
    valor = ferramentas_escolha.sql_escolher_tipo()

    update_geral(tabela, campo, novo_dado, campo_condicao, valor)