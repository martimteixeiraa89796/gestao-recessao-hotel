"""
Modulo responsavel por inserir dados nas varias tabelas da base de dados
========================================================================
Este módulo contém funcoes que fazem o input ao utilizador e realizam as insercoes nas respetivas tabelas da base de dados do hotel
"""
from ferramentas_BD import executarBD, get_tabelas
from ferramentas_escolha import input_string, input_int, input_float, input_bool, listar_escolhas, fazer_escolha


def mapeador_inserts():
    """
    Apresenta lista das tabelas e executa a funcao de inserçao correspondente.
    Esta função obtém a lista das tabelas,apresenta-as ao utilizador e, após a escolha, associa automaticamente a tabela á sua funcao de inserção
    :return: none
    :rtype: NoneType
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
    Insere um novo tipo de cama na tabela Tb_Tipo_cama
    :return: none
    :rtype: NoneType
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
    Insere um novo tipo de quarto na tabela Tb_Tipo_Quarto
    :return: none
    :rtype: NoneType
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
    Insere um novo tipo de quarto na tabela Tb_Tipo_Quarto
    :return: none
    :rtype: NoneType
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
    Insere um cliente na tabela Tb_Cliente
    :return: none
    :rtype: NoneType
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
    Insere um tipo de reserva na tabela Tb_Tipo_Reserva
    :return: none
    :rtype: NoneType
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
    Insere uma relação entre um quarto e um tipo de cama
    :return: none
    :rtype: NoneType
    """
    print("Insira o número do quarto:")
    num_quarto =input_int()

    print("Insira o número do tipo de cama:")
    num_tipo_cama =input_int()

    query = f"""
        INSERT INTO Tb_tipo_Camas (Num_Quarto, Num_Tipo_Cama)
        VALUES (?, ?);
    """

    executarBD(query, (num_quarto,num_tipo_cama))


def inserir_funcao():
    """
    Insere uma função de funcionario na tabela funcoes
    :return: none
    :rtype: NoneType
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
    Insere um funcionario na tabela Tb_Funcionario
    :return: none
    :rtype: NoneType
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
    Insere um horário de funcionario na tabela Tb_Horario
    :return: none
    :rtype: NoneType
    """
    print("Insira o número do funcionário:")
    num_funcionario = input_int()

    print("Insira o horário de iníco (AAAA-MM-DD HH:MM:SS):")
    comeca = input_string()
    
    print("Insira o horário de fim (AAAA-MM-DD HH:MM:SS):")
    acaba = input_string()

    print("Insira o dia de folga:")
    folga = input_string()

    query = f"""
        INSERT INTO Tb_Horario (Num_Funcionario, Comeca, Acaba, Folga)
        VALUES (?, ?, ?, ?);
    """

    executarBD(query, (num_funcionario,comeca,acaba,folga))


def inserir_reserva():
    """
    Insere uma reserva na tabela Tb_Reserva
    :return: none
    :rtype: NoneType
    """
    print("Insira o número do tipo de reserva:")
    num_tipo_reserva = input_int()

    print("Insira a data de check-in (AAAA-MM-DD HH:MM:SS):")
    check_in = input_string()

    print("Insira a data de check-out (AAAA-MM-DD HH:MM:SS):")
    check_out = input_string()

    print("Insira o número do funcionário:")
    num_funcionario = input_float()

    query = f"""
        INSERT INTO Tb_Reserva (Num_Tipo_Reserva, Check_in, Check_out, Num_Funcionario)
        VALUES (?, ?, ?, ?, ?);
    """
    
    executarBD(query, (num_tipo_reserva,check_in,check_out,num_funcionario))


def inserir_hospede():
    """
    Insere um hóspede na tabela Tb_Hospede
    :return: none
    :rtype: NoneType
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