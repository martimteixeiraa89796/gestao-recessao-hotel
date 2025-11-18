def inserir_tipo_cama():
    num_tipo_cama =input("insira tipocama:")
    
    nome_tipo_cama=input("insira nome cama:")

    
    query = f"""
        INSERT INTO Tipo_Cama (Num_Tipo_Cama, Nome_Tipo_Cama)
        VALUES ({num_tipo_cama}, {nome_tipo_cama});
    """
    return query


inserir_tipo_cama()
