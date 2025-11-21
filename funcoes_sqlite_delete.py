"""
Módulo com funções de remoção de tabelas
========================================

Este módulo contém funções que são usadas para remover as várias tabelas existentes na base de dados da aplicação.
As funções retornam a query SQL para ser usada na execução na base de dados.
"""

from ferramentas_BD import executarBD, get_tabelas
import ferramentas_escolha

def limpar_tabela_geral(tabela):
    query = f"""
        DELETE FROM {tabela};
    """

    executarBD(query)


def delete_geral(tabela, campo_condicao, valor):
    query = f"""
        DELETE FROM {tabela} WHERE {campo_condicao} = ?;
    """

    executarBD(query, (valor))


def limpar_tabela_geral_escolha():
    tabela_lista = get_tabelas()

    print("Escolha tabela para apagar todos os dados.")
    ferramentas_escolha.listar_escolhas(tabela_lista)

    tabela = ferramentas_escolha.fazer_escolha(tabela_lista)

    limpar_tabela_geral(tabela)

limpar_tabela_geral_escolha()

    
def remover_tabela_tipo_cama():
    """
    Remove tabela com tipos de cama

    :return: Código SQL para *query*
    :rtype: string
    """

    query ="""
        drop table if exists Tipo_Cama
    """

    return query


def remover_tabela_tipo_quarto():
    """
    Remove tabela com tipos de quartos

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        drop table if exists Tipo_Quarto
    """

    return query


def remover_tabela_Quarto():
    """
    Remove tabela com os quartos disponíveis no hotel

    :return: Código SQL para *query*
    :rtype: string
    """

    query ="""
        drop table if exists Quarto
    """

    return query


def remover_tabela_Cliente():
    """
    Remove tabela com dados sobre os clientes

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        drop table if exists Cliente
    """

    return query


def remover_tabela_Tipo_Reserva():
    """
    Remove tabela com tipo de reserva

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        drop table if exists Tipo_Reserva
    """

    return query

    
def remover_tabela_Camas():
    """
    Remover tabela com relação entre tipos de camas e respetivo quarto

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
    drop table if exists tipo_Camas
    """

    return query


def remover_tabela_Funcoes():
    """
    Remove tabela com funções do funcionários

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        drop table if exists Funcoes
    """

    return query


def remover_tabela_Funcionario():
    """
    Remove tabela com dados sobre funcionários

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        drop table if exists Funcionario
    """
    
    return query


def remover_tabela_Horario():
    """
    Remove tabela com o horário de cada funcionário

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        drop table if exists Horario
    """

    return query


def remover_tabela_Reserva():
    """
    Remove tabela com dados sobre reservas feitas

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        drop table if exists Reserva
    """

    return query


def remover_tabela_Hospedes():
    """
    Remove tabela com dados sobre os hospedes referentes a uma reserva

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        drop table if exists Hospedes
    """

    return query