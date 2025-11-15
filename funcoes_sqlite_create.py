"""
Módulo com funções de criação de tabelas
========================================

Este módulo contém funções que são usadas para criar as várias tabelas existentes na base de dados da aplicação.
As funções retornam a query SQL para ser usada na execução na base de dados.
"""


    
def criar_tabela_tipo_cama():
    """
    Cria tabela com tipos de cama

    :return: Código SQL para *query*
    :rtype: string
    """

    query ="""
        create table Tipo_Cama(
        Num_Tipo_Cama int not null,
        Nome_Tipo_Cama varchar(100),
        constraint PK_Tipo_Cama primary key (Num_Tipo_Cama)
        );
    """


def criar_tabela_tipo_quarto():
    """
    Cria tabela com tipos de quartos

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        CREATE TABLE IF NOT EXISTS Tipo_Quarto (
            Num_Tipo_Quarto INT NOT NULL,
            Nome_Tipo_Quarto VARCHAR(50) NOT NULL,
            CONSTRAINT PK_Tipo_Quarto PRIMARY KEY (Num_Tipo_Quarto)
        );
    """
def criar_tabela_Quarto():
    """
    Cria tabela com os quartos disponíveis no hotel

    :return: Código SQL para *query*
    :rtype: string
    """

    query ="""
        CREATE TABLE IF NOT EXISTS Quarto (
            Num_Quarto INT AUTO_INCREMENT,
            Num_Tipo_Quarto INT NOT NULL,
            Preco Decimal(10,2) NOT NULL,
            Ocupado VARCHAR(15),
            CONSTRAINT PK_quarto Primary key (Num_Quarto),
            CONSTRAINT FK_Quarto_Tipo_Quarto FOREIGN KEY (Num_Tipo_Quarto)
                REFERENCES Tipo_Quarto(Num_Tipo_Quarto)
    );  
    """


def criar_tabela_Cliente():
    """
    Cria tabela com dados sobre os clientes

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        create table Cliente(
        NIF int not null,
        Nome_Cliente varchar(50),
        Telefone varchar(15),
        constraint PK_Cliente primary key(NIF)
        );
    """

def criar_tabela_Tipo_Reserva():
    """
    Cria tabela com tipo de reserva

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        create table Tipo_Reserva(
        Num_Tipo_Reserva int not null,
        Nome_Tipo_Reserva varchar(50),
        constraint PK_Tipo_Reserva primary key (Num_Tipo_Reserva)
        );
    """
    
def criar_tabela_Camas():
    """
    Cria tabela com relação entre tipos de camas e respetivo quarto

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
    CREATE TABLE IF NOT EXISTS tipo_Camas(
    Num_Quarto INT NOT NULL,
    Num_Tipo_Cama INT NOT NULL,
    CONSTRAINT FK_Camas_Quarto FOREIGN KEY(Num_Quarto)
        REFERENCES Quartos(Num_Quarto),
    CONSTRAINT FK_Camas_Tipo_Cama FOREIGN KEY(Num_Tipo_Quarto)
        REFERENCES Tipo_Cama(Num_Tipo_Cama)
    );
"""

def criar_tabela_Funcoes():
    """
    Cria tabela com funções do funcionários

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        create table Funcoes(
        Num_Funcao int not null,
        Nome_Funcao varchar(50),
        constraint PK_Funcoes primary key (Num_Funcao)
        );
    """

def criar_tabela_Funcionario():
    """
    Cria tabela com dados sobre funcionários

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        create table Funcionario(
        Num_Funcionario int not null,
        Nome_Funcionario varchar(50),
        Num_funcao int,
        constraint PK_Funcionario primary key (Num_Funcionario),
        constraint FK_Funcoes_Funcionario foreign key (Num_Funcao)
        references Funcoes(Num_Funcao)
        );
    """
def criar_tabela_Horario():
    """
    Cria tabela com o horário de cada funcionário

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        create table Horario(
        Num_funcionario int,
        Comeca datetime,
        Acaba datetime,
        Folga varchar(15),
        constraint FK_Funcionario_Horario foreign key (Num_Funcionario)
        references Funcionario (Num_Funcionario)
        );
    """

def criar_tabela_Reserva():
    """
    Cria tabela com dados sobre reservas feitas

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        create table Reserva(
        Num_Reserva int not null,
        Num_Tipo_Reserva int,
        Check_in datetime,
        Check_out datetime,
        Num_Funcionario int,
        constraint PK_Reserva primary key (Num_Reserva),
        constraint FK_Tipo_Reserva_Reserva foreign key (Num_Tipo_Reserva)
        references Tipo_Reserva(Num_Tipo_Reserva),
        constraint FK_Funcionario_Reserva foreign key (Num_Funcionario)
        references Funcionario(Num_funcionario)
        );
    """

def criar_tabela_Hospedes():
    """
    Cria tabela com dados sobre os hospedes referentes a uma reserva

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        create table Hospedes(
        Num_Reserva int,
        NIF int,
        Reservado_Em_Nome varchar(20),
        Num_Quarto int,
        constraint FK_Reserva_Hospedes foreign key (Num_Reserva)
        references Reserva (Num_Reserva),
        constraint FK_Cliente_Hospedes foreign key (NIF)
        references Cliente (NIF),
        constraint FK_Quarto_Hospedes foreign key (Num_Quarto)
        references Quarto (Num_Quarto)
        );
    """