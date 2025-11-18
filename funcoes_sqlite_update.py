def update_geral(tabela,campo,dados,condicao,valor):
    query = f"""
        update {tabela}
        set {campo} = {dados}
        where {condicao} = {valor};
        """
    
    return query

def update_geral_escolha():
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
        tabela_escolha = int(input("Escolha uma tabela: "))

        if 0 < tabela_escolha <= len(tabelas):
            break

        else:
            print("Tabela não disponível.")

    while True:
        if tabela_escolha == 0:
            print("""
            Campos disponiveis:
                  1. NIF
                  2. Nome_Cliente
                  3. Telefone
            """)

            campos = ["NIF",
                      "Nome_Cliente",
                      "Telefone"
                      ]
            

        if tabela_escolha == 1:
            print("""
            Campos disponiveis:
                  1. Num_Reserva
                  2. NIF
                  3. Reservado_Em_Nome
                  4. Num_Quarto
            """)

            campos = ["Num_Reserva"
                      "NIF",
                      "Reservado_Em_Nome",
                      "Num_Quarto"
                      ]
            

        if tabela_escolha == 2:
            print("""
            Campos disponiveis:
                  1. Num_Reserva
                  2. Num_Tipo_Reserva
                  3. Check_In
                  4. Check_Out
                  5. Num_Funcionario
            """)

            campos = ["Num_Reserva",
                      "Num_Tipo_Reserva",
                      "Check_In",
                      "Check_Out",
                      "Num_Funcionario"
                      ]
            

        if tabela_escolha == 3:
            print("""
            Campos disponiveis:
                  1. Num_Tipo_Reserva
                  2. Nome_Tipo_Reserva
            """)

            campos = ["Num_Tipo_Reserva",
                      "Nome_Tipo_Reserva",
                      ]


        if tabela_escolha == 4:
            print("""
            Campos disponiveis:
                  1. Num_Quarto
                  2. Num_Tipo_Quarto
                  3. Preco
                  4. Ocupado
            """)

            campos = ["Num_Quarto",
                      "Num_Tipo_Quarto",
                      "Preco",
                      "Ocupado"
                      ]
            

        if tabela_escolha == 5:
            print("""
            Campos disponiveis:
                  1. Num_tipo_Quarto
                  2. Nome_TipoQuarto
            """)

            campos = ["Num_Tipo_Quarto",
                      "Nome_Tipo_Quarto"
                      ]


        if tabela_escolha == 6:
            print("""
            Campos disponiveis:
                  1. Num_Quarto
                  2. Num_Tipo_Cama
            """)

            campos = ["Num_Quarto",
                      "Num_Tipo_Cama"
                      ]
            

        if tabela_escolha == 7:
            print("""
            Campos disponiveis:
                  1. Num_Tipo_Cama
                  2. Nome_Tipo_Cama
            """)

            campos = ["Num_Tipo_Cama",
                      "Nome_Tipo_Cama"
                      ]
            

        if tabela_escolha == 8:
            print("""
            Campos disponiveis:
                  1. Num_Funcionario
                  2. Nome_Funcionario
                  3. Num_Funcao
            """)

            campos = ["Num_Funcionario",
                      "Nome_Funcionario",
                      "Num_Funcao"
                      ]
            

        if tabela_escolha == 9:
            print("""
            Campos disponiveis:
                  1. Num_Funcao
                  2. Nome_Funcao
            """)

            campos = ["Num_Funcao",
                      "Nome_Funcao"
                      ]
            

        if tabela_escolha == 10:
            print("""
            Campos disponiveis:
                  1. Num_Funcionario
                  2. Comeca
                  3. Acaba
                  4. Folga
            """)

            campos = ["Num_Funcionario",
                      "Comeca",
                      "Acaba",
                      "Folga"
                      ]


            campo_escolha = int(input("escolha um campo: "))

            if 0 < campo_escolha <= len(campos):
                break

        else:
            print("Campo não disponivel")
            

    
    dados = input("insira o novo dado: ")

    condicao = input("insira a condição: ")

    valor = input("insira o valor: ")

    update_geral(tabelas[tabela_escolha-1], campos[campo_escolha-1], dados, condicao, valor)