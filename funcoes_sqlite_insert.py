"""
Modulo responsavel por inserir dados nas varias tabelas da base de dados
========================================================================
Este módulo contém funcoes que fazem o input ao utilizador e realizam as insercoes nas respetivas tabelas da base de dados do hotel
"""
from ferramentas_BD import executarBD, get_tabelas
from ferramentas_escolha import input_string, input_int, input_float, input_bool, listar_escolhas, fazer_escolha


def mapeador_inserts():
    """
    Apresenta lista das tabelas e executa a funcao de inserção correspondente.
    
    Esta função obtém a lista das tabelas, apresenta-as ao utilizador e, após a escolha,
    associa automaticamente a tabela à sua funcao de inserção.

    Exemplo de execução:

    >>> mapeador_inserts()
    #Resultado
    Opções disponíveis:
        1. Cliente
        2. Hospede
        3. Quarto
    Escolha uma opção: 1
    Cliente
    #Apartir deste ponto, é chamado o insert correspondente.
    inserir_cliente()
    """

    tabelas = get_tabelas()

    listar_escolhas(tabelas)
    tabela = fazer_escolha(tabelas)

    lista_inserts = [inserir_tipo_cama,
                     inserir_tipo_Quarto,
                     inserir_tipo_reserva,
                     inserir_funcao,
                     inserir_cliente,
                     inserir_quarto,
                     inserir_Funcionario,
                     inserir_camas,
                     inserir_reserva,
                     inserir_horario,
                     inserir_hospede]

    for x in range(len(tabelas)):
        if tabela == tabelas[x]:
            lista_inserts[x]()



def inserir_tipo_cama(): 
    """
    Insere um novo tipo de cama na tabela Tb_Tipo_cama.

    Exemplo de pedido:

    >>> inserir_tipo_cama()
    #Resultado
    Insira nome do tipo de cama:
    --> Luxo
    Luxo
    #Corre a lógica de insert.
    """ 

    print("Insira nome do tipo de cama:")       
    nome_tipo_cama = input_string()
  
    query = f"""
        INSERT INTO Tb_Tipo_Cama (Nome_Tipo_Cama)
        VALUES (?);
    """

    executarBD(query, (nome_tipo_cama,))


def inserir_tipo_Quarto():
    """
    Insere um novo tipo de quarto na tabela Tb_Tipo_Quarto.
    
    Exemplo de pedido:

    >>> inserir_tipo_Quarto()
    #resultado
    Insira o nome do tipo de quarto:
    --> VIP
    VIP
    #Corre a lógica de insert.
    """

    print("Insira o nome do tipo de quarto:")
    nome_tipo_quarto = input_string()
    
    query = f"""
        INSERT INTO Tb_Tipo_Quarto(Nome_Tipo_Quarto)
        VALUES (?);
    """

    executarBD(query, (nome_tipo_quarto,))


def inserir_quarto():
    """
    Insere um novo quarto na tabela Tb_Quarto.
    
    Exemplo de pedido:

    >>> inserir_quarto()
    #resultado
    Insira o número de quarto:
    --> 300
    300
    Insira o numero do tipo de quarto:
    --> 3
    3
    Insira o preço do quarto:
    --> 450.99
    450.99
    O quarto está ocupado?
    Opções disponíveis:
        1. True
        2. False
    Escolha uma opção: 2
    False
    #Corre a lógica de insert.
    """

    print("Insira o número de quarto:")
    num_quarto = input_int()

    print("Insira o numero do tipo de quarto:")
    num_tipo_quarto = input_int()

    print("Insira o preço do quarto:")
    preco = input_float()

    print("O quarto está ocupado?")
    ocupado = input_bool()

    query = f"""
        INSERT INTO Tb_Quarto(Num_Quarto, Num_Tipo_Quarto, Preco, Ocupado)
        VALUES (?, ? , ? , ?);
    """

    executarBD(query, (num_quarto, num_tipo_quarto, preco, ocupado))


def inserir_cliente():
    """
    Insere um cliente na tabela Tb_Cliente.
    
    Exemplo de pedido:

    >>> inserir_cliente()
    #resultado
    Insira o NIF do cliente:
    --> 8439577384
    8439577384
    Insira o nome do cliente:
    --> João
    João
    Insira o numero de telefone do cliente:
    --> 999999999
    999999999
    #Corre a lógica de insert.
    """

    print("Insira o NIF do cliente:")
    nif = input_int()

    print("Insira o nome do cliente:")
    nome_cliente = input_string()

    print("Insira o numero de telefone do cliente:")  
    telefone = input_string()

    query = f"""
        INSERT INTO Tb_Cliente (NIF, Nome_Cliente, Telefone)
        VALUES (?, ?, ?);
    """

    executarBD(query, (nif,nome_cliente,telefone))


def inserir_tipo_reserva():
    """
    Insere um tipo de reserva na tabela Tb_Tipo_Reserva.

    Exemplo de pedido:

    >>> inserir_tipo_reserva()
    #resultado
    Insira o nome do tipo de reserva:
    --> Barato
    Barato
    #Corre a lógica de insert.
    """
    print("Insira o nome do tipo de reserva:")
    nome_tipo_reserva = input_string()

    query = f"""
        INSERT INTO Tb_Tipo_Reserva (Nome_Tipo_Reserva)
        VALUES (?);
    """

    executarBD(query, (nome_tipo_reserva,))


def inserir_camas():
    """
    Insere uma relação entre um quarto e um tipo de cama.

    Exemplo de pedido:

    >>> inserir_camas()
    #resultado
    Insira o número do quarto:
    --> 300
    300
    Insira o número do tipo de cama:
    --> 3
    3
    #Corre a lógica de insert.
    """
    print("Insira o número do quarto:")
    num_quarto =input_int()

    print("Insira o número do tipo de cama:")
    num_tipo_cama =input_int()

    query = f"""
        INSERT INTO Tb_Camas (Num_Quarto, Num_Tipo_Cama)
        VALUES (?, ?);
    """

    executarBD(query, (num_quarto,num_tipo_cama))


def inserir_funcao():
    """
    Insere uma função de funcionario na tabela funcoes.

    Exemplo de pedido:

    >>> inserir_funcao()
    #resultado
    Insira o nome da função:
    --> Gerente
    Gerente
    #Corre a lógica de insert.
    """
    print("Insira o nome da função:")
    nome_funcao = input_string()

    query = f"""
        INSERT INTO funcoes (Nome_Funcao)
        VALUES (?);
    """
    
    executarBD(query, (nome_funcao,))


def inserir_Funcionario():
    """
    Insere um funcionario na tabela Tb_Funcionario.
    
    Exemplo de pedido:

    >>> inserir_Funcionario()
    #resultado
    Insira o nome do funcionário:
    --> João Ratão
    João Ratão
    Insira o número da função:
    --> 8
    8
    #Corre a lógica de insert.
    """

    print("Insira o nome do funcionário:")
    nome_funcionario = input_string()

    print("Insira o número da função:")
    num_funcao = input_int()

    query = f"""
        INSERT INTO Tb_Funcionario (Nome_Funcionario, Num_Funcao)
        VALUES (?, ?);
    """
    
    executarBD(query, (nome_funcionario,num_funcao))


def inserir_horario():
    """
    Insere um horário de funcionario na tabela Tb_Horario.
    
    Exemplo de pedido:
    #resultado

    >>> inserir_horario()
    Insira o número do funcionário:
    --> 4
    4
    Insira o dia da semana :
    --> Segunda
    Segunda
    Insira o intrevalo de horas de trabalho (se nao trabalha insira folga):
    --> 09:00 - 22:00
    09:00 - 22:00
    #Corre a lógica de insert.
    """

    print("Insira o número do funcionário:")
    num_funcionario = input_int()

    print("Insira o dia da semana :")
    dia_semana = input_string()
    
    print("Insira o intrevalo de horas de trabalho (se nao trabalha insira folga):")
    hora_trabalho = input_string()

    query = f"""
        INSERT INTO Tb_Horario (Num_Funcionario, Dia_Semana, Hora_Trabalho)
        VALUES (?, ?, ?);
    """

    executarBD(query, (num_funcionario,dia_semana,hora_trabalho,))


def inserir_reserva():
    """
    Insere uma reserva na tabela Tb_Reserva.
    
    Exemplo de pedido:

    >>> inserir_reserva()
    #resultado
    Insira o número do tipo de reserva:
    --> 99
    99
    Insira a data de check-in (AAAA-MM-DD HH:MM:SS):
    --> 2025-11-23 23:59:00
    2025-11-23 23:59:00
    Insira a data de check-out (AAAA-MM-DD HH:MM:SS):
    --> 2025-12-23 23:59:00
    2025-12-23 23:59:00
    Insira o número do funcionário:
    --> 34
    34
    #Corre a lógica de insert.
    """

    print("Insira o número do tipo de reserva:")
    num_tipo_reserva = input_int()

    print("Insira a data de check-in (AAAA-MM-DD HH:MM:SS):")
    check_in = input_string()

    print("Insira a data de check-out (AAAA-MM-DD HH:MM:SS):")
    check_out = input_string()

    print("Insira o número do funcionário:")
    num_funcionario = input_int()

    query = f"""
        INSERT INTO Tb_Reserva (Num_Tipo_Reserva, Check_in, Check_out, Num_Funcionario)
        VALUES (?, ?, ?, ?);
    """
    
    executarBD(query, (num_tipo_reserva,check_in,check_out,num_funcionario))


def inserir_hospede():
    """
    Insere um hóspede na tabela Tb_Hospede.
    
    Exemplo de pedido:

    >>> inserir_hospede()
    #resultado
    Insira on número da reserva:
    --> 65
    65
    Insira o NIF do cliente:
    --> 548574875845
    548574875845
    Reservado em nome deste cliente?
    Opções disponíveis:
        1. True
        2. False
    Escolha uma opção: 1
    True
    Insira o número do quarto:
    --> 45
    45
    #Corre a lógica de insert.
    """
    print("Insira on número da reserva:")
    num_reserva = input_int()

    print("Insira o NIF do cliente:")
    nif = input_int()

    print("Reservado em nome deste cliente?")
    reservado_em_nome = input_bool()

    print("Insira o número do quarto:")
    num_quarto =input_int()
    
    query = f"""
        INSERT INTO Tb_Hospedes (Num_Reserva, NIF, Reservado_Em_Nome, Num_Quarto)
        VALUES (?, ?, ?, ?);
    """
    
    executarBD(query, (num_reserva,nif,reservado_em_nome,num_quarto))