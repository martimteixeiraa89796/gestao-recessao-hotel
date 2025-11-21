"""
Módulo com funções de criação de tabelas
========================================

Este módulo contém funções que são usadas para criar as várias tabelas existentes na base de dados da aplicação.
As funções retornam a query SQL para ser usada na execução na base de dados.
"""

from ferramentas_BD import executarBD
    
def criar_tabela_tipo_cama():
    """
    Cria tabela com tipos de cama

    :return: Código SQL para *query*
    :rtype: string
    """

    query ="""
        CREATE TABLE Tb_Tipo_Cama(
            Num_Tipo_Cama INTEGER PRIMARY KEY,
            Nome_Tipo_Cama VARCHAR(100) NOT NULL
        );
    """

    executarBD(query)


def criar_tabela_tipo_quarto():
    """
    Cria tabela com tipos de quartos

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        CREATE TABLE Tb_Tipo_Quarto (
            Num_Tipo_Quarto INTEGER PRIMARY KEY,
            Nome_Tipo_Quarto VARCHAR(50) NOT NULL
        );
    """

    executarBD(query)


def criar_tabela_Quarto():
    """
    Cria tabela com os quartos disponíveis no hotel

    :return: Código SQL para *query*
    :rtype: string
    """

    query ="""
        CREATE TABLE Tb_Quarto (
            Num_Quarto INTEGER PRIMARY KEY,
            Num_Tipo_Quarto INT NOT NULL,
            Preco Decimal(10,2) NOT NULL,
            Ocupado BOOLEAN NOT NULL,
            CONSTRAINT FK_Tb_Quarto_Tb_Tipo_Quarto FOREIGN KEY (Num_Tipo_Quarto)
                REFERENCES Tb_Tipo_Quarto(Num_Tipo_Quarto)
                ON UPDATE CASCADE
                ON DELETE RESTRICT
        );  
    """

    executarBD(query)


def criar_tabela_Cliente():
    """
    Cria tabela com dados sobre os clientes

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        CREATE TABLE Tb_Cliente(
            NIF INT NOT NULL,
            Nome_Cliente VARCHAR(50) NOT NULL,
            Telefone VARCHAR(15) NOT NULL,
            CONSTRAINT PK_Tb_Cliente PRIMARY KEY(NIF)
        );
    """

    executarBD(query)


def criar_tabela_Tipo_Reserva():
    """
    Cria tabela com tipo de reserva

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        CREATE TABLE Tb_Tipo_Reserva(
            Num_Tipo_Reserva INTEGER PRIMARY KEY,
            Nome_Tipo_Reserva VARCHAR(50) NOT NULL
        );
    """

    executarBD(query)

    
def criar_tabela_Camas():
    """
    Cria tabela com relação entre tipos de camas e respetivo quarto

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
    CREATE TABLE Tb_Camas(
        Num_Cama INTEGER PRIMARY KEY,
        Num_Quarto INT NOT NULL,
        Num_Tipo_Cama INT NOT NULL,
        CONSTRAINT FK_Tb_Camas_Tb_Quarto FOREIGN KEY(Num_Quarto)
            REFERENCES Tb_Quarto(Num_Quarto)
            ON UPDATE CASCADE
            ON DELETE RESTRICT,
        CONSTRAINT FK_Tb_Camas_Tb_Tipo_Cama FOREIGN KEY(Num_Tipo_Cama)
            REFERENCES Tb_Tipo_Cama(Num_Tipo_Cama)
            ON UPDATE CASCADE
            ON DELETE RESTRICT
        );
    """

    executarBD(query)


def criar_tabela_Funcoes():
    """
    Cria tabela com funções do funcionários

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        CREATE TABLE Tb_Funcoes(
            Num_Funcao INTEGER PRIMARY KEY,
            Nome_Funcao VARCHAR(50) NOT NULL
        );
    """

    executarBD(query)


def criar_tabela_Funcionario():
    """
    Cria tabela com dados sobre funcionários

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        CREATE TABLE Tb_Funcionario(
            Num_Funcionario INTEGER PRIMARY KEY,
            Nome_Funcionario VARCHAR(50) NOT NULL,
            Num_funcao int NOT NULL,
            CONSTRAINT FK_Tb_Funcoes_Tb_Funcionario FOREIGN KEY (Num_Funcao)
                REFERENCES Tb_Funcoes(Num_Funcao)
                ON UPDATE CASCADE
                ON DELETE RESTRICT
        );
    """
    
    executarBD(query)


def criar_tabela_Horario():
    """
    Cria tabela com o horário de cada funcionário

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        CREATE TABLE Tb_Horario(
            Num_funcionario INT NOT NULL,
            Comeca DATETIME NOT NULL,
            Acaba DATETIME NOT NULL,
            Folga VARCHAR(15) NOT NULL,
            CONSTRAINT FK_Tb_Funcionario_Tb_Horario FOREIGN KEY (Num_Funcionario)
                REFERENCES Tb_Funcionario (Num_Funcionario)
                ON UPDATE CASCADE
                ON DELETE RESTRICT
        );
    """

    executarBD(query)


def criar_tabela_Reserva():
    """
    Cria tabela com dados sobre reservas feitas

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        CREATE TABLE Tb_Reserva(
            Num_Reserva INTEGER PRIMARY KEY,
            Num_Tipo_Reserva INT NOT NULL,
            Check_in DATETIME NOT NULL,
            Check_out DATETIME NOT NULL,
            Num_Funcionario INT NOT NULL,
            CONSTRAINT FK_Tb_Tipo_Reserva_Tb_Reserva FOREIGN KEY (Num_Tipo_Reserva)
                REFERENCES Tb_Tipo_Reserva(Num_Tipo_Reserva)
                ON UPDATE CASCADE
                ON DELETE RESTRICT,
            CONSTRAINT FK_Tb_Funcionario_Tb_Reserva FOREIGN KEY (Num_Funcionario)
                REFERENCES Tb_Funcionario(Num_funcionario)
                ON UPDATE CASCADE
                ON DELETE RESTRICT
        );
    """

    executarBD(query)


def criar_tabela_Hospedes():
    """
    Cria tabela com dados sobre os hospedes referentes a uma reserva

    :return: Código SQL para *query*
    :rtype: string
    """

    query = """
        CREATE TABLE Tb_Hospedes(
            Num_Registo INTEGER PRIMARY KEY,
            Num_Reserva INT NOT NULL,
            NIF INT NOT NULL,
            Reservado_Em_Nome BOOLEAN NOT NULL,
            Num_Quarto INT NOT NULL,
            CONSTRAINT FK_Tb_Reserva_Tb_Hospedes FOREIGN KEY (Num_Reserva)
                REFERENCES Tb_Reserva (Num_Reserva)
                ON UPDATE CASCADE
                ON DELETE RESTRICT,
            CONSTRAINT FK_Tb_Cliente_Tb_Hospedes FOREIGN KEY (NIF)
                REFERENCES Tb_Cliente (NIF)
                ON UPDATE CASCADE
                ON DELETE RESTRICT,
            CONSTRAINT FK_Tb_Quarto_Tb_Hospedes FOREIGN KEY (Num_Quarto)
                REFERENCES Tb_Quarto (Num_Quarto)
                ON UPDATE CASCADE
                ON DELETE RESTRICT
        );
    """

    executarBD(query)


criar_tabela_tipo_cama()