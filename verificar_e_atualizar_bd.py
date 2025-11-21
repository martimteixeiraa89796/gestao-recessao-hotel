import os
import subprocess
import ferramentas_BD
from funcoes_sqlite_select import select_geral
import funcoes_sqlite_create


def atualizar_repositorio():
    """
    Atualiza o repositório local com a versão do GitHub.

    :return: True se o pull foi bem-sucedido
    :rtype: bool
    """
    try:
        print("A atualizar ficheiros a partir do GitHub...")
        resultado = subprocess.run(
            ["git", "pull"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        print(resultado.stdout)

        if resultado.returncode == 0:
            print("Repositório atualizado com sucesso.\n")
            return True
        else:
            print("Erro ao tentar fazer git pull:")
            print(resultado.stderr)
            return False

    except Exception as e:
        print(f"Ocorreu um erro ao tentar atualizar: {e}")
        return False



def verificar_e_atualizar_tabelas():
    """
    Verifica se as tabelas existem na base de dados 'gestao-recessao-hotel'.
    Caso não existam, tenta atualizar o repositório com um 'git pull' e cria
    as tabelas em falta.

    :return: None
    """

    bd = ferramentas_BD.FerramentasBD()
    bd.conectarBD("gestao-recessao-hotel")

    tabelas = [
        "Tb_Cliente",
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

    funcoes_criacao = [
        funcoes_sqlite_create.criar_tabela_Cliente,
        funcoes_sqlite_create.criar_tabela_Hospedes,
        funcoes_sqlite_create.criar_tabela_Reserva,
        funcoes_sqlite_create.criar_tabela_Tipo_Reserva,
        funcoes_sqlite_create.criar_tabela_Quarto,
        funcoes_sqlite_create.criar_tabela_tipo_quarto,
        funcoes_sqlite_create.criar_tabela_Camas,
        funcoes_sqlite_create.criar_tabela_tipo_cama,
        funcoes_sqlite_create.criar_tabela_Funcionario,
        funcoes_sqlite_create.criar_tabela_Funcoes,
        funcoes_sqlite_create.criar_tabela_Horario
    ]

    print("A verificar tabelas...\n")

    for i in range(len(tabelas)):
        existe = bd.executarBD(select_geral(tabelas[i]))

        if existe is None or existe == []:
            print(f"Tabela '{tabelas[i]}' não encontrada.")

            # Tentar atualizar o repositório antes de criar
            atualizar_repositorio()

            print(f"A criar tabela {tabelas[i]} ...")
            bd.executarBD(funcoes_criacao[i]())
            print(f"Tabela {tabelas[i]} criada com sucesso.\n")

        else:
            print(f"Tabela '{tabelas[i]}' já existe.")

    print("\nVerificação concluída.")
    bd.desconectarBD()
