"""
Módulo com funções para fazer *selects*
=======================================

Este módulo contém funções que criam o código SQL para ser utilizado em *queries select*.
"""

from ferramentas_BD import executarBD, get_tabelas
from ferramentas_escolha import input_int,input_string, listar_escolhas, fazer_escolha


def select_geral(tabela):
    """
    Retorna código SQL para *queries select* de uma tabela.

    Esta função é usada para criar as *queries* para visualizar todos os dados de uma das tabelas disponíveis na base de dados.
    Serve para ter uma ideia dos dados existentes.

    :param tabela: A tabela que se pretende consultar
    :type tabela: string

    :return: Código SQL para a *query*
    :rtype: string

    Exemplo de um *select* de uma tabela:

    >>> select_geral("Tb_Cliente")
    """

    query = f"""
        SELECT * FROM {tabela};
    """

    return query


def select_geral_escolha():
    """
    Forma interativa de fazer *select* de uma tabela.

    É pedido ao utilizador uma tabela para ser feito um *select*.
    A tabela escolhida é depois enviada para a função **select_geral** e imprimida.

    Exemplo de execução:

    >>> select_geral_escolha()
    #Resultado
    Escolha tabela para visualizar.
    Opções disponíveis:
        1. Cliente
        2. Hospede
        3. Quarto
    Escolha uma opção: 1
    ID | Nome    | Contacto  |
    1  | João    | 999999999 |
    2  | Mariana | 888888888 |
    """

    tabela_lista = get_tabelas()

    print("Escolha tabela para visualizar.")
    listar_escolhas(tabela_lista)

    tabela =fazer_escolha(tabela_lista)

    executarBD(select_geral(tabela), imprimir=True)



def ver_horario():
    """
    Mostra o Horario do funcionario
    O utilizador mostra o numero do funcionario e a função mostra a informação do dia_semana e Hora_Trabalho.

    Exemplo de execução:

    >>> ver_horario()
    #resultado
    insira o seu numero de fucionario:
    --> 5
    Dia_Semana | Hora_Trabalho |
    Segunda    | 09:00 - 10:00 |
    Terça      | 08:00 - 17:00 |
    """
        
    print("insira o seu numero de fucionario: ")
    Numero = input_int()

    query = f'''
        select Dia_Semana, Hora_Trabalho from Tb_Horario
         where Num_funcionario = ?;
        '''

    executarBD(query, (Numero,), imprimir=True)


def ver_quarto_livers():
    """
    Mostra o numero de quartos livres
    Seleciona o numero do quarto ocupado=False

    Exemplo de execução:

    >>> ver_quarto_livers()
    #resultado
    Num_Quarto |
    23         |
    45         |
    """

    query = f'''
        select Num_Quarto from Tb_Quarto
        where Ocupado = "False";
    '''

    executarBD(query, imprimir=True)


def ver_cliente_em_quarto():
    """
    Mostra o numero do quarto e nome do cliente

    Exemplo de execução:

    >>> ver_cliente_em_quarto()
    #resultado
    Num_Quarto | Nome_Cliente |
    23         | João         |
    45         | Maria        |
    """

    query = f'''
        select Num_Quarto, Nome_Cliente from Tb_Hospedes
        inner join Tb_Cliente on Tb_Hospedes.NIF = Tb_Cliente.NIF;
    '''
    
    executarBD(query, imprimir=True)



def ver_chegada_cliente():
    """
    Mostra os clientes que fizeram Check_In entre as datas.

    Exemplo de execução:

    >>> ver_chegada_cliente()
    #resultado
    insira a incial data(AAAA-MM-DD HH:MM:SS):
    --> 2000-12-20
    insira a final data(AAAA-MM-DD HH:MM:SS):
    --> 2001-01-10
    Nome_Cliente | Check_In   |
    João         | 2000-12-24 |
    Maria        | 2001-01-02 |
    """

    print("insira a incial data(AAAA-MM-DD HH:MM:SS): ")
    data1 = input_string()

    print("insira a final data(AAAA-MM-DD HH:MM:SS): ")
    data2 = input_string()

    query = f'''
        select Nome_Cliente, Check_In from Tb_Reserva
        inner join Tb_Hospedes on Tb_Reserva.Num_Reserva = Tb_Hospedes.Num_Reserva
        inner join Tb_Cliente on Tb_Hospedes.NIF = Tb_Cliente.NIF
        where Check_In between ? and ?;
    '''

    executarBD(query, (data1,data2),imprimir=True)


def contar_camas_em_quarto():
    """
    Mostra quantas camas exitem em cada quarto.

    Exemplo de execução:
    
    >>> contar_camas_em_quarto()
    #resultado
    Num_Quarto | Numero_Camas |
    23         | 3            |
    45         | 2            |
    """

    query = f'''
        select Num_Quarto, count(Num_Cama) as Numero_Camas from Tb_Camas
        group by Num_Quarto;
    '''

    executarBD(query, imprimir=True)



def estadia():
    """
    Mostra as datas dos clientes com Check_In e Check_Out.

    Exemplo de execução:

    >>> estadia()
    #resultado
    Nome_Cliente | Check_In   | Check_Out  |
    João         | 2000-12-24 | 2000-12-20 |
    Maria        | 2000-12-19 | 2000-12-31 |
    """
    query = f'''
        select Nome_Cliente, Check_In, Check_Out from Tb_Reserva
        inner join Tb_Hospedes on Tb_Reserva.Num_Reserva = Tb_Hospedes.Num_Reserva
        inner join Tb_Cliente on Tb_Hospedes.NIF = Tb_Cliente.NIF;
    '''

    executarBD(query, imprimir=True)