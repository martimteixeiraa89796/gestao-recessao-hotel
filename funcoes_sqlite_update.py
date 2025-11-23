"""
Modulo com funções de atualização de dados
==========================================

Este módulo contém funções para atualizar informações nas tabelas da base de dados SQLite utilizada na aplicação

funções Principais:
-update_geral(): Executa um UPDATE dos campos de uma tabela
-update_geral_escolha(): menu interativo que permite escolher a tabela no qual permite atualizar
"""

from ferramentas_BD import executarBD, get_campos, get_tabelas
import ferramentas_escolha

def update_geral(tabela, campo, novo_dado, campo_condicao, valor):
    query = f"""
        update {tabela}
        set {campo} = ?
        where {campo_condicao} = ?
        ;
        """
    
    executarBD(query, (novo_dado, valor))


def update_geral_escolha():
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