"""
Módulo com funções de remoção de tabelas
----------------------------------------

Este módulo contém funções que são usadas para remover as várias tabelas existentes na base de dados da aplicação.
"""

from ferramentas_BD import executarBD, get_campos, get_tabelas
import ferramentas_escolha

def limpar_tabela_geral(tabela):
    """
    Elimina todas a linhas de uma tabela.

    :param tabela: Tabela onde se pretende apagar dados
    :type tabela: string

    Exemplo de execução:

    >>> limpar_tabela_geral("Clientes")
    """

    query = f"""
        DELETE FROM {tabela};
    """

    executarBD(query)


def delete_geral(tabela, campo_condicao, valor):
    """
    Elimina linhas de uma tabela

    Esta função elimina linhas específica segundo uma dada condição definida pelo utilizador.

    :param tabela: A tabela onde se pretende apagar linha
    :type tabela: string

    :param campo_condicao: Campo para servir de condição para apagar linha
    :type campo_condicao: string

    :param valor: Valor que o campo de condição deve ter numa linha
    :type valor: string, int ou float

    Exemplo de execução:

    >>> delete_geral()
    """

    query = f"""
        DELETE FROM {tabela} WHERE {campo_condicao} = ?;
    """

    executarBD(query, (valor,))


def limpar_tabela_geral_escolha():
    """
    Versão interativa de apagar todos os dados de uma tabela

    Esta função pergunta ao utilizador para escolher uma tabela onde este pretende apagar todos os registos de uma tabela.
    Esta função não elimina tabelas, somente os seus dados
    
    Exemplo de pedido:

    >>> limpar_tabela_geral_escolha()
    #resultado
    Escolha tabela para apagar todos os dados.
    Opções disponíveis:
        1. Cliente
        2. Hospede
        3. Quarto
    Escolha uma opção: 4
    Opção não disponivel
    Escolha uma opção: 1
    """

    tabela_lista = get_tabelas()

    print("Escolha tabela para apagar todos os dados.")
    ferramentas_escolha.listar_escolhas(tabela_lista)

    tabela = ferramentas_escolha.fazer_escolha(tabela_lista)

    limpar_tabela_geral(tabela)


def delete_geral_escolha():
    """
    Forma interativa de apagar linhas de uma tabela.

    Esta função permite apagar linhas específica de tabelas que o utilizador escolhe.

    Exemplo de pedido:

    >>> delete_geral_escolha()
    #resultado
    Escolha uma tabela onde quer apagar dados.
    Opções disponíveis:
        1. Cliente
        2. Hospede
        3. Quarto
    Escolha uma opção: 4
    Opção não disponivel
    Escolha uma opção: 1
    Escolha um campo de condição.
    Opções disponíveis:
        1. Nome
        2. NIF
        3. Telefone
    Escolha uma opção: 1
    Insira valor de condição.
    --> João
    Escolha formato.
    Opções disponíveis:
        1. Sql Int
        2. Sql Decimal
        3. Sql String
    Escolha formato.
    Escolha uma opção: 3
    """

    tabela_lista = get_tabelas()
    
    print("Escolha uma tabela onde quer apagar dados.")
    ferramentas_escolha.listar_escolhas(tabela_lista)
    tabela = ferramentas_escolha.fazer_escolha(tabela_lista)

    campo_lista = get_campos(tabela)
    print("Escolha um campo de condição.")
    ferramentas_escolha.listar_escolhas(campo_lista)
    campo_condicao = ferramentas_escolha.fazer_escolha(campo_lista)

    print("Insira valor de condição.")
    valor = ferramentas_escolha.sql_escolher_tipo()

    delete_geral(tabela, campo_condicao, valor)