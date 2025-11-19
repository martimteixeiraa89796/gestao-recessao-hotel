def inserir_tipo_cama():
    num_tipo_cama =int(input("insira tipo de cama:"))                 
    nome_tipo_cama=input("insira nome cama:")
  
    query = f"""
        INSERT INTO Tipo_Cama (Num_Tipo_Cama, Nome_Tipo_Cama)
        VALUES ({num_tipo_cama}, '{nome_tipo_cama}');
    """
    return query

def inserir_tipo_Quarto():
    Num_Tipo_Quarto =int(input("insira Numerotipocama:"))
    Nome_Tipo_Quarto =input("insira Tipo Quarto:")
    
    query = f"""
    INSERT INTO Tipo_Quarto(Num_Tipo_Quarto,Nome_Tipo_Quarto)
    VALUES ({Num_Tipo_Quarto},'{Nome_Tipo_Quarto}');
"""
    return query

def inserir_quarto():
    num_tipo_quarto = int(input("insira o numero do tipo de quarto"))
    preco = float(input(" o preco do quarto:"))
    ocupado = input("O quarto está ocupado (Sim/Não): ")

    query = f"""
    INSERT INTO Quarto(Num_Tipo_Quarto,preco, ocupado)
    VALUES ({num_tipo_quarto}, {preco}, '{ocupado}');
"""
    return query

def inserir_cliente():
    nif = int(input("Insira o NIF do Cliente:"))
    nome_cliente = input("Insira o nome do Cliente:")  
    telefone = input("Insira o telefone do Cliente:")

    query = f"""
    INSERT INTO Cliente (NIF,Nome_Cliente,Telefone)
    VALUES ({nif},'{nome_cliente}','{telefone}');
"""
    return query

def inserir_tipo_reserva():

    num_tipo_reserva = int(input("Insira o numero  do tipo reservas:"))
    nome_tipo_reserva = input("Insira o nome do tipo da reserva:")

    query = f"""
    INSERT INTO Tipo_Reserva (Num_Tipo_Reserva, Nome_Tipo_Reserva)
    VALUES ({num_tipo_reserva}, '{nome_tipo_reserva}');
"""
    return query

def inserir_camas():

    num_quarto =int(input("Insira o numero do quarto:"))
    num_tipo_cama =int(input("Insira o numero do tipo de cama:"))

    query = f"""
    INSERT INTO tipo_Camas (Num_Quarto, Num_Tipo_Cama)
    VALUES ({num_quarto}, {num_tipo_cama});
"""
    return query

def inserir_funcao():
    num_funcao = int(input("Insira o numero da funcao:"))
    nome_funcao = input("Insira o nome da funcao:")

    query = f"""
    INSERT INTO funcoes (Num_Funcao, Nome_Funcao)
    VALUES ({num_funcao}, '{nome_funcao}');
    """
    return query

def inserir_Funcionario():
    num_funcionario = int(input("Insira o número do funcionário: "))
    nome_funcionario = input("Insira o nome do funcionário: ")
    num_funcao = int(input("Insira o número da função: "))

    query = f"""
    INSERT INTO Funcionario (Num_Funcionario, Nome_Funcionario, Num_Funcao)
    VALUES ({num_funcionario}, '{nome_funcionario}', {num_funcao});
    """
    return query

def inserir_horario():
    num_funcionario = int(input("Insira o número do funcionário: "))
    comeca = input("Insira o horário de início (AAAA-MM-DD HH:MM:SS): ")
    acaba = input("Insira o horário de fim (AAAA-MM-DD HH:MM:SS): ")
    folga = input("Insira o dia de folga: ")

    query = f"""
    INSERT INTO Horario (Num_Funcionario, Comeca, Acaba, Folga)
    VALUES ({num_funcionario}, '{comeca}', '{acaba}', '{folga}');
    """
    return query

def inserir_reserva():
    num_reserva = int(input("Insira o número da reserva: "))
    num_tipo_reserva = int(input("Insira o número do tipo de reserva: "))
    check_in = input("Insira a data de check-in (AAAA-MM-DD HH:MM:SS): ")
    check_out = input("Insira a data de check-out (AAAA-MM-DD HH:MM:SS): ")
    num_funcionario = int(input("Insira o número do funcionário responsável: "))

    query = f"""
    INSERT INTO Reserva (Num_Reserva, Num_Tipo_Reserva, Check_in, Check_out, Num_Funcionario)
    VALUES ({num_reserva}, {num_tipo_reserva}, '{check_in}', '{check_out}', {num_funcionario});
    """
    return query

def inserir_hospede():
    num_reserva = int(input("Insira o número da reserva: "))
    nif = int(input("Insira o NIF do hóspede: "))
    reservado_em_nome = input("Insira o nome em que a reserva foi feita: ")
    num_quarto =int(input("insira o numero do quarto:"))
    
    query = f"""
    INSERT INTO Hospedes (Num_Reserva, NIF, Reservado_Em_Nome, Num_Quarto)
    VALUES ({num_reserva}, {nif}, '{reservado_em_nome}', {num_quarto});
    """
    return query

