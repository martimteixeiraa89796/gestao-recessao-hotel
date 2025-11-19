def inserir_tipo_cama():
    num_tipo_cama =int(input("insira tipocama:"))                 
    nome_tipo_cama=input("insira nome cama:")
  
    query = f"""
        INSERT INTO Tipo_Cama (Num_Tipo_Cama, Nome_Tipo_Cama)
        VALUES ({num_tipo_cama}, {nome_tipo_cama});
    """
    return query

def inserir_tipo_Quarto():
    Num_Tipo_Quarto =int(input("insira Numerotipocama:"))
    Nome_Tipo_Quarto =input("insira Tipo Quarto:")
    
    query = f"""
    INSERT INTO Tipo_Quarto(Num_Tipo_Quarto,Nome_Tipo_Quarto)
    VALUES ({Num_Tipo_Quarto},{Nome_Tipo_Quarto});
"""
    return query

def inserir_quarto():
    num_tipo_quarto = int(input("insira o numero do tipo de quarto"))
    preco = float(input(" o preco do quarto:"))
    ocupado = input("O quarto está ocupado (Sim/Não): ")

    query = f"""
    INSERT INTO Quarto(Num_Tipo_Quarto,preco, ocupado)
    VALUES ({num_tipo_quarto}, {preco}, {ocupado});
"""
    return query

def inserir_cliente():
    nif = int(input("Insira o NIF do Cliente:"))
    nome_clente = input("Insira o nome do Cliente:")  
    telefone = input("Insira o telefone do Cliente:")

    query = f"""
    INSERT INTO Cliente (NIF,Nome_Cliente,Telefone)
    VALUES ({nif},{nome_clente},{telefone});
"""
    return query

def inserir_tipo_reserva():

    num_tipo_reserva = int(input("Insira o numero  do tipo reservas:"))
    nome_tipo_reserva = input("Insira o nome do tipo da reserva:")

    query = f"""
    INSERT INTO Tipo_Reserva (Num_Tipo_Reserva, Nome_Tipo_Reserva)
    VALUES ({num_tipo_reserva}, {nome_tipo_reserva};
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
    VALUES ({num_funcao}, {nome_funcao});
    """
    return query