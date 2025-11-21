from ferramentas_BD import executarBD
from ferramentas_escolha import input_string, input_int, input_float, input_bool


def inserir_tipo_cama():          
    print("Insira nome do tipo de cama:")       
    nome_tipo_cama = input_string()
  
    query = f"""
        INSERT INTO Tipo_Cama (Nome_Tipo_Cama)
        VALUES (?);
    """

    executarBD(query, (nome_tipo_cama))


def inserir_tipo_Quarto():
    print("Insira o nome do tipo de quarto:")
    nome_tipo_quarto = input_string()
    
    query = f"""
        INSERT INTO Tipo_Quarto(Nome_Tipo_Quarto)
        VALUES (?);
    """

    executarBD(query, (nome_tipo_quarto))


def inserir_quarto():
    print("Insira o número de quarto:")
    num_quarto = input_int()

    print("Insira o numero do tipo de quarto:")
    num_tipo_quarto = input_int()

    print("Insira o preço do quarto:")
    preco = input_float()

    print("O quarto está ocupado?")
    ocupado = input_bool()

    query = f"""
        INSERT INTO Quarto(Num_Quarto, Num_Tipo_Quarto, Preco, Ocupado)
        VALUES (?, ? , ? , ?);
    """

    executarBD(query, (num_quarto, num_tipo_quarto, preco, ocupado))


def inserir_cliente():
    print("Insira o NIF do cliente:")
    nif = input_int

    print("Insira o nome do cliente:")
    nome_cliente = input_string()

    print("Insira o numero de telefone do cliente:")  
    telefone = input_string()

    query = f"""
        INSERT INTO Cliente (NIF, Nome_Cliente, Telefone)
        VALUES (?, ?, ?);
    """

    executarBD(query, (nif,nome_cliente,telefone))


def inserir_tipo_reserva():
    print("Insira o nome do tipo de reserva:")
    nome_tipo_reserva = input_string()

    query = f"""
        INSERT INTO Tipo_Reserva (Nome_Tipo_Reserva)
        VALUES (?);
    """

    executarBD(query, (nome_tipo_reserva))


def inserir_camas():
    print("Insira o número do quarto:")
    num_quarto =input_int()

    print("Insira o número do tipo de cama:")
    num_tipo_cama =input_int()

    query = f"""
        INSERT INTO tipo_Camas (Num_Quarto, Num_Tipo_Cama)
        VALUES (?, ?);
    """

    executarBD(query, (num_quarto,num_tipo_cama))


def inserir_funcao():
    print("Insira o nome da função:")
    nome_funcao = input_string()

    query = f"""
        INSERT INTO funcoes (Nome_Funcao)
        VALUES (?);
    """
    
    executarBD(query, (nome_funcao))


def inserir_Funcionario():
    print("Insira o nome do funcionário:")
    nome_funcionario = input_string()

    print("Insira o número da função:")
    num_funcao = input_int

    query = f"""
        INSERT INTO Funcionario (Nome_Funcionario, Num_Funcao)
        VALUES (?, ?);
    """
    
    executarBD(query, (nome_funcionario,num_funcao))


def inserir_horario():
    print("Insira o número do funcionário:")
    num_funcionario = input_int()

    print("Insira o horário de iníco (AAAA-MM-DD HH:MM:SS):")
    comeca = input_string()
    
    print("Insira o horário de fim (AAAA-MM-DD HH:MM:SS):")
    acaba = input_string()

    print("Insira o dia de folga:")
    folga = input_string()

    query = f"""
        INSERT INTO Horario (Num_Funcionario, Comeca, Acaba, Folga)
        VALUES (?, ?, ?, ?);
    """

    executarBD(query, (num_funcionario,comeca,acaba,folga))


def inserir_reserva():
    print("Insira o número do tipo de reserva:")
    num_tipo_reserva = input_int()

    print("Insira a data de check-in (AAAA-MM-DD HH:MM:SS):")
    check_in = input_string()

    print("Insira a data de check-out (AAAA-MM-DD HH:MM:SS):")
    check_out = input_string()

    print("Insira o número do funcionário:")
    num_funcionario = input_float()

    query = f"""
        INSERT INTO Reserva (Num_Tipo_Reserva, Check_in, Check_out, Num_Funcionario)
        VALUES (?, ?, ?, ?, ?);
    """
    
    executarBD(query, (num_tipo_reserva,check_in,check_out,num_funcionario))


def inserir_hospede():
    print("Insira on número da reserva:")
    num_reserva = input_int()

    print("Insira o NIF do cliente:")
    nif = input_int()

    print("Reservado em nome deste cliente?")
    reservado_em_nome = input_bool()

    print("Insira o número do quarto:")
    num_quarto =input_int()
    
    query = f"""
        INSERT INTO Hospedes (Num_Reserva, NIF, Reservado_Em_Nome, Num_Quarto)
        VALUES (?, ?, ?, ?);
    """
    
    executarBD(query, (num_reserva,nif,reservado_em_nome,num_quarto))

