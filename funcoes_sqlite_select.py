"""
Módulo com funções para fazer *selects*
=======================================

Este módulo contém funções que criam o código SQL para ser utilizado em *queries select*.
"""

def select_master():
    query = f"""
        SELECT name FROM sqlite_master WHERE type='table'
    """

    return query

def select_geral(tabela):
    """
    Retorna código SQL para *queries select* de uma tabela.

    Esta função é usada para criar as *queries* para visualizar todos os dados de uma das tabelas disponíveis na base de dados.
    Serve para ter uma ideia dos dados existentes.

    :param tabela: A tabela que se pretende consultar
    :type tabela: string

    :return: Código SQL para a *query*
    :rtype: string

    Exemplo de um *select* de uma tabela:

    >>> select_geral("Tb_Cliente")
    """

    query = f"""
        SELECT * FROM {tabela};
    """

    return query


def select_geral_escolha():
    """
    Forma interativa de fazer *select* de uma tabela.

    É pedido ao utilizador uma tabela para ser feito um *select*.
    A tabela escolhida é depois enviada para a função **select_geral**.
    """

    info = """
        Tabelas disponíveis:
            1.  Cliente
            2.  Hospedes
            3.  Reserva
            4.  Tipo de Reserva
            5.  Quarto
            6.  Tipos de Quarto
            7.  Camas
            8.  Tipos de Cama
            9.  Funcionários
            10. Funções
            11. Horário
    """

    tabelas = ["Tb_Cliente",
               "Tb_Hospede",
               "Tb_Reserva",
               "Tb_Tipo_Reserva",
               "Tb_Quarto",
               "Tb_Tipo_Quarto",
               "Tb_Cama",
               "Tb_Tipo_Cama",
               "Tb_Funcionario",
               "Tb_Funcoes",
               "Tb_Horario"
               ]
    print(info)

    while True:
        escolha = int(input("Escolha uma tabela: "))

        if 0 < escolha <= len(tabelas):
            break

        else:
            print("Tabela não disponível.")

    select_geral(tabelas[escolha-1])