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
        CREATE TABLE Tipo_Cama(
            Num_Tipo_Cama INT NOT NULL AUTO_INCREMENT,
            Nome_Tipo_Cama VARCHAR(100) NOT NULL,
            CONSTRAINT PK_Tipo_Cama PRIMARY KEY (Num_Tipo_Cama)
        );
    """

    return query


def criar_tabela_tipo_quarto():
    """
    Cria tabela com tipos de quartos

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        CREATE TABLE Tipo_Quarto (
            Num_Tipo_Quarto INT NOT NULL AUTO_INCREMENT,
            Nome_Tipo_Quarto VARCHAR(50) NOT NULL,
            CONSTRAINT PK_Tipo_Quarto PRIMARY KEY (Num_Tipo_Quarto)
        );
    """

    return query


def criar_tabela_Quarto():
    """
    Cria tabela com os quartos disponíveis no hotel

    :return: Código SQL para *query*
    :rtype: string
    """

    query ="""
        CREATE TABLE Quarto (
            Num_Quarto INT NOT NULL AUTO_INCREMENT,
            Num_Tipo_Quarto INT NOT NULL,
            Preco Decimal(10,2) NOT NULL,
            Ocupado BOOLEAN NOT NULL,
            CONSTRAINT PK_quarto Primary key (Num_Quarto),
            CONSTRAINT FK_Quarto_Tipo_Quarto FOREIGN KEY (Num_Tipo_Quarto)
                REFERENCES Tipo_Quarto(Num_Tipo_Quarto)
                ON UPDATE CASCADE
                ON DELETE RESTRICT
        );  
    """

    return query


def criar_tabela_Cliente():
    """
    Cria tabela com dados sobre os clientes

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        CREATE TABLE Cliente(
            NIF INT NOT NULL,
            Nome_Cliente VARCHAR(50) NOT NULL,
            Telefone VARCHAR(15) NOT NULL,
            CONSTRAINT PK_Cliente PRIMARY KEY(NIF)
        );
    """

    return query


def criar_tabela_Tipo_Reserva():
    """
    Cria tabela com tipo de reserva

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        CREATE TABLE Tipo_Reserva(
            Num_Tipo_Reserva INT NOT NULL AUTO_INCREMENT,
            Nome_Tipo_Reserva VARCHAR(50) NOT NULL,
            CONSTRAINT PK_Tipo_Reserva PRIMARY KEY (Num_Tipo_Reserva)
        );
    """

    return query

    
def criar_tabela_Camas():
    """
    Cria tabela com relação entre tipos de camas e respetivo quarto

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
    CREATE TABLE Camas(
        Num_Cama INT NOT NULL AUTO_INCREMENT,
        Num_Quarto INT NOT NULL,
        Num_Tipo_Cama INT NOT NULL,
        CONSTRAINT PK_Camas PRIMARY KEY(Num_Cama),
        CONSTRAINT FK_Camas_Quarto FOREIGN KEY(Num_Quarto)
            REFERENCES Quartos(Num_Quarto)
            ON UPDATE CASCADE
            ON DELETE RESTRICT,
        CONSTRAINT FK_Camas_Tipo_Cama FOREIGN KEY(Num_Tipo_Cama)
            REFERENCES Tipo_Cama(Num_Tipo_Cama)
            ON UPDATE CASCADE
            ON DELETE RESTRICT
        );
    """

    return query


def criar_tabela_Funcoes():
    """
    Cria tabela com funções do funcionários

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        CREATE TABLE Funcoes(
            Num_Funcao INT NOT NULL AUTO_INCREMENT,
            Nome_Funcao VARCHAR(50) NOT NULL,
            CONSTRAINT PK_Funcoes PRIMARY KEY (Num_Funcao)
        );
    """

    return query


def criar_tabela_Funcionario():
    """
    Cria tabela com dados sobre funcionários

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        CREATE TABLE Funcionario(
            Num_Funcionario INT NOT NULL AUTO_INCREMENT,
            Nome_Funcionario VARCHAR(50) NOT NULL,
            Num_funcao int NOT NULL,
            CONSTRAINT PK_Funcionario PRIMARY KEY (Num_Funcionario),
            CONSTRAINT FK_Funcoes_Funcionario FOREIGN KEY (Num_Funcao)
                REFERENCES Funcoes(Num_Funcao)
                ON UPDATE CASCADE
                ON DELETE RESTRICT
        );
    """
    
    return query


def criar_tabela_Horario():
    """
    Cria tabela com o horário de cada funcionário

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        CREATE TABLE Horario(
            Num_funcionario INT NOT NULL,
            Comeca DATETIME NOT NULL,
            Acaba DATETIME NOT NULL,
            Folga VARCHAR(15) NOT NULL,
            CONSTRAINT FK_Funcionario_Horario FOREIGN KEY (Num_Funcionario)
                REFERENCES Funcionario (Num_Funcionario)
                ON UPDATE CASCADE
                ON DELETE RESTRICT
        );
    """

    return query


def criar_tabela_Reserva():
    """
    Cria tabela com dados sobre reservas feitas

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        CREATE TABLE Reserva(
            Num_Reserva INT NOT NULL AUTO_INCREMENT,
            Num_Tipo_Reserva INT NOT NULL,
            Check_in DATETIME NOT NULL,
            Check_out DATETIME NOT NULL,
            Num_Funcionario INT NOT NULL,
            CONSTRAINT PK_Reserva PRIMARY KEY (Num_Reserva),
            CONSTRAINT FK_Tipo_Reserva_Reserva FOREIGN KEY (Num_Tipo_Reserva)
                REFERENCES Tipo_Reserva(Num_Tipo_Reserva)
                ON UPDATE CASCADE
                ON DELETE RESTRICT,
            CONSTRAINT FK_Funcionario_Reserva FOREIGN KEY (Num_Funcionario)
                REFERENCES Funcionario(Num_funcionario)
                ON UPDATE CASCADE
                ON DELETE RESTRICT
        );
    """

    return query


def criar_tabela_Hospedes():
    """
    Cria tabela com dados sobre os hospedes referentes a uma reserva

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        CREATE TABLE Hospedes(
            Num_Registo INT NOT NULL AUTO_INCREMENT,
            Num_Reserva INT NOT NULL,
            NIF INT NOT NULL,
            Reservado_Em_Nome BOOLEAN NOT NULL,
            Num_Quarto INT NOT NULL,
            CONSTRAINT FK_Reserva_Hospedes FOREIGN KEY (Num_Reserva)
                REFERENCES Reserva (Num_Reserva)
                ON UPDATE CASCADE
                ON DELETE RESTRICT,
            CONSTRAINT FK_Cliente_Hospedes FOREIGN KEY (NIF)
                REFERENCES Cliente (NIF)
                ON UPDATE CASCADE
                ON DELETE RESTRICT,
            CONSTRAINT FK_Quarto_Hospedes FOREIGN KEY (Num_Quarto)
                REFERENCES Quarto (Num_Quarto)
                ON UPDATE CASCADE
                ON DELETE RESTRICT
        );
    """

    return query