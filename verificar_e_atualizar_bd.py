from ferramentas_BD import executarBD
from funcoes_sqlite_select import select_geral
import funcoes_sqlite_create

def verificador_tabelas():
    tabelas = ["Tb_Tipo_Cama",
            "Tb_Tipo_Quarto",
            "Tb_Tipo_Reserva",
            "Tb_Funcoes",
            "Tb_Cliente",
            "Tb_Quarto",
            "Tb_Funcionario",
            "Tb_Camas",
            "Tb_Reserva",
            "Tb_Horario",
            "Tb_Hospedes"
            ]

    funcoes_criacao = [funcoes_sqlite_create.criar_tabela_tipo_cama,
                    funcoes_sqlite_create.criar_tabela_tipo_quarto,
                    funcoes_sqlite_create.criar_tabela_Tipo_Reserva,
                    funcoes_sqlite_create.criar_tabela_Funcoes,
                    funcoes_sqlite_create.criar_tabela_Cliente,
                    funcoes_sqlite_create.criar_tabela_Quarto,
                    funcoes_sqlite_create.criar_tabela_Funcionario,
                    funcoes_sqlite_create.criar_tabela_Camas,
                    funcoes_sqlite_create.criar_tabela_Reserva,
                    funcoes_sqlite_create.criar_tabela_Horario,
                    funcoes_sqlite_create.criar_tabela_Hospedes
                    ]

    print("A verificar tabelas...")
    for tabela in range(len(tabelas)):
        if executarBD(select_geral(tabelas[tabela])) != None:
            pass

        else:
            print(f"Tabela {tabelas[tabela]} não existe.")
            print(f"A criar tabela {tabelas[tabela]}...")

            funcoes_criacao[tabela]()

    print("Verificação concluída.")