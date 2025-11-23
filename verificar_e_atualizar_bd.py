from ferramentas_BD import executarBD
from funcoes_sqlite_select import select_geral
import funcoes_sqlite_create

def verificador_tabelas():
    """
    Verifica se as tabelas existem e cria-as.

    Esta função permite verificar se as tabelas da base de dados estão criadas e, caso não estejam, as mesmas são criadas.
    Isto é necessário uma vez que o ficheiro de base de dado é algo à parte do código da aplicação.

    Exemplo de execução:

    >>> verificador_tabelas()
    #resultado
    A verificar tabelas...
    Tabela Tb_Tipo_Cama não existe.
    A criar tabela Tb_Tipo_Cama...
    Tabela Tb_Tipo_Quarto não existe.
    A criar tabela Tb_Tipo_Quarto...
    Verificação concluída.
    """

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
        if executarBD(select_geral(tabelas[tabela]), omitir_sql_erro=True) != None:
            pass

        else:
            print(f"Tabela {tabelas[tabela]} não existe.")
            print(f"A criar tabela {tabelas[tabela]}...")

            funcoes_criacao[tabela]()

    print("Verificação concluída.")