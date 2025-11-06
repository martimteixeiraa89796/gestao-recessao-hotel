#Este ficheiro é onde vai ser colocado funções com comandos de SQL
#O objetivo é que estas sejam chamadas dentro de um ficheiro python
#onde depois a classe que está dentro de ferramentas_BD.py
#vai depois ser iniciada e utilizada.

#Isto é somente para separar a query e a lógica do código.



#Exemplo de função e estrutura
def função(exemplo, exemplo2, exemplo3):  #<--- Colocar argumentos para alterar partes da query antes de ser mandada para ser executada
    """Função de exemplo"""
    
    #Query é construída com as variáveis de cima
    query = f"""
        SELECT * FROM {exemplo};
    """

    return query #Retorna a query finalizada para depois ser executada
    #A query seria guardada numa variável para depois ser executada noutro lado

    
def criar_tabela_tipo_cama():
    query ="""
        create table Tipo_Cama(
        Num_Tipo_Cama int not null,
        Nome_Tipo_Cama varchar(100),
        constraint PK_Tipo_Cama primary key (Num_Tipo_Cama)
        )
    """


def criar_tabela_tipo_quarto():
    """Cria a tabela Tipo_quarto"""
    query = """
        CREATE TABLE IF NOT EXISTS Tipo_quarto(
        Num_Tipo_quarto INT,
        Num_Tipo_quarto varchar(50),
        Constraint PK_tipo_quarto Primary key (Num_Tipo_Quarto)
        )
    """
def criar_tabela_Quarto():
    """Criar tabela Quarto"""
    query ="""
        Create table IF NOT EXISTS Quarto(
        Num_Tipo_Quarto INT,
        Preco Decimal(10,2)
        Ocupado VARCHAR(3) CHECK(ocupado IN ('sim' 'Nao'))
         Constraint PK_quarto Primary key (Num_Quarto)
         Constrait FK_Quarto_Tipo_Quarto FOREIGNT KEY (Num_Tipo_Quarto)
         REFERENCES TB_Tipo_Quarto(Num_Tipo_Quarto)
    );  
    """



