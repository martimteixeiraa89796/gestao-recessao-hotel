def update_geral(tabela,campo,dados,condicao,valor):
    query = f"""
        update {tabela}
        set {campo} = {dados}
        where {condicao} = {valor};
        """
    
    return query