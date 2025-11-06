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
    """Cria a tabela Tipo_Quarto"""
    query = """
        CREATE TABLE IF NOT EXISTS Tipo_Quarto (
            Num_Tipo_Quarto INT NOT NULL,
            Nome_Tipo_Quarto VARCHAR(50) NOT NULL,
            CONSTRAINT PK_Tipo_Quarto PRIMARY KEY (Num_Tipo_Quarto)
        );
    """
def criar_tabela_Quarto():
    """Criar tabela Quarto"""
    query ="""
        CREATE TABLE IF NOT EXISTS Quarto (
            Num_Quarto INT AUTO_INCREMENT,
            Num_Tipo_Quarto INT NOT NULL,
            Preco Decimal(10,2) NOT NULL,
            Ocupado VARCHAR(3) CHECK(Ocupado IN ('sim','Nao')),
            CONSTRAINT PK_quarto Primary key (Num_Quarto),
            CONSTRAINT FK_Quarto_Tipo_Quarto FOREIGN KEY (Num_Tipo_Quarto)
                REFERENCES Tipo_Quarto(Num_Tipo_Quarto)
    );  
    """



def criar_tabela_Cliente():
    query = """
        create table Cliente(
        NIF int not null,
        Nome_Cliente varchar(50),
        Telefone varchar(15),
        constraint PK_Cliente primary key(NIF)
        )
    """

def criar_tabela_Tipo_Reserva():
    query = """
        create table Tipo_Reserva(
        Num_Tipo_Reserva int not nul,
        Nome_Tipo_Reserva varchar(50),
        constraint PK_Tipo_Reserva primary key (Num_Tipo_Reserva)
        )
    """

def criar_tabela_Funcoes():
    query = """
        create table Funcoes(
        Num_Funcao int not null,
        Nome_Funcao varchar(50),
        constraint PK_Funcoes primary key (Num_Funcao)
        )
    """

def criar_tabela_Funcionario():
    query = """
        create table Funcionario(
        Num_Funcionario int not null,
        Nome_Funcionario varchar(50),
        Num_funcao int,
        constraint PK_Funcionario primary key (Num_Funcionario)
        constraint FK_Funcoes_Funcionario foreign key (Num_Funcao)
        references Funcoes(Num_Funcao)
        )
    """
def criar_tabela_Horario():
    query = """
        create table Horario(
        Num_funcionario int,
        Comeca datetime,
        Acaba datetime,
        Folga varchar(15),
        constraint FK_Funcionario_Horario foreign key (Num_Funcionario)
        reference Funcionario (Num_Funcionario)
        )
    """