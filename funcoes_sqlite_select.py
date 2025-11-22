"""
Módulo com funções para fazer *selects*
=======================================

Este módulo contém funções que criam o código SQL para ser utilizado em *queries select*.
"""

from ferramentas_BD import executarBD, get_tabelas
from ferramentas_escolha import input_int


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
    A tabela escolhida é depois enviada para a função **select_geral** e imprimida.

    Exemplo de execução:

    >>> select_geral_escolha()
    """

    tabela_lista = get_tabelas()

    print("Escolha tabela para visualizar.")
    ferramentas_escolha.listar_escolhas(tabela_lista)

    tabela = ferramentas_escolha.fazer_escolha(tabela_lista)

    executarBD(select_geral(tabela), imprimir=True)



    def ver_horario():
        
        print("insira o seu numero de fucionario: ")
        Numero = input_int()

        query = f'''
            select Dia_Semana, Hora_Trabalho from Tb_Horario
            where Num_funcionario = ?
            '''

        executarBD(query, (Numero))


