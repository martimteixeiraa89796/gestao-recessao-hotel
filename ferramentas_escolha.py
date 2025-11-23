"""
Módulo com função para ajudar com input do utilizador
-----------------------------------------------------

Este módulo contém funções com tudo o que é necessário para se interagir com o utilizador.
"""

def listar_escolhas(lista):
    """
    Imprime uma listagem de itens.

    Esta função faz uma listagem numérica do que lhe é fornecido.
    Isto é feito através da iteração na lista e construção de strings para serem imprimidas.

    Útil para apresentar escolhas ao utilizador.

    :param lista: Lista com os objetos para listagem
    :type lista: list

    Exemplo de listagem:

    >>> listar_escolhas(["Azul", "Vermelho", "Amarelo"])
    #Resultado
    Opções disponíveis:
        1. Azul
        2. Vermelho
        3. Amarelo
    """

    print("Opções disponíveis:")
    for item in range(len(lista)):
        print(f"    {item + 1}. {lista[item]}".title())


def fazer_escolha(lista):
    """
    De uma lista, pregunta *input* ao utilizador e retorna a resposta.

    Esta função cria um loop onde o utilizador tem de escolher uma opção baseado numa lista que
    é fornecida á função. O loop termina se a escolha for válida.

    Esta função convém ser usada em conjunto com **listar_escolhas**.

    :return: Opção escolhida pelo utilizador
    :rtype: Depende do valor inseridos

    Exemplo de ambiente de escolha:

    >>> fazer_escolha(["Banana", "Maçã", "Pera"])
    #Resultado
    Escolha uma opção: 4
    Opção não disponivel
    Escolha uma opção: 1
    Banana
    """

    while True:
        try:
            escolha = int(input("Escolha uma opção: "))

            if 0 < escolha <= len(lista):
                break

            else:
                print("Opção não disponivel")
        
        except ValueError:
            pass
    
    return lista[escolha-1]


def sql_escolher_tipo():
    """
    Pede ao utilizador para introduzir dados e formato sql equivalente.

    Esta função pede ao utilizador para inserir dados e o formato que o mesmo pretende.
    A função faz depois a tradução entre os tipos em Python que são equivalente no sql.

    Esta função é util quando o utilizador necessita de inserir dados, onde o formato deste não podem ser definidos.

    :return: Resposta do utilizador traduzida
    :rtype: string, int ou float

    Exemplo de execução:

    >>> sql_escolher_tipo()
    --> João
    Escolha formato.
    Opções disponíveis:
        1. Sql Int
        2. Sql Decimal
        3. Sql String
    Escolha uma opção: 2
    Formato incompatível.
    Opções disponíveis:
        1. Sql Int
        2. Sql Decimal
        3. Sql String
    Escolha formato.
    Escolha uma opção: 3
    João
    """

    while True:
        while True:
            resposta = input("--> ")

            if not resposta:
                pass

            else:
                break

        tipo_dado_lista = ["sql int",
                        "sql decimal",
                        "sql string"]

        print("Escolha formato.")
        listar_escolhas(tipo_dado_lista)


        escolha = fazer_escolha(tipo_dado_lista)

        try:
            if escolha == tipo_dado_lista[0]:
                resposta = int(resposta)
            
            elif escolha == tipo_dado_lista[1]:
                resposta = float(resposta)
            
            elif not escolha:
                continue
            
            else:
                pass
            
            break

        except ValueError:
                print("Formato incompatível.")

    return resposta


def input_string():
    """
    Pede ao utilizador uma string.

    Esta função coloca o utilizador dentro de um loop onde é-lhe pedido uma que introduza uma string.
    Esta função também verifica se o que foi introduzido está de acordo com o que se pretende.

    :return: Resposta do utilizador
    :rtype: string

    Exemplo de pedido:

    >>> input_string()
    #Resultado
    --> #Utilizador apenas prime ENTER, loop continua
    --> Ok
    Ok
    """

    while True:
            resposta = input("--> ")

            if not resposta:
                pass

            else:
                break

    return resposta


def input_int():
    """
    Pede ao utilizador um número inteiro.

    Esta função coloca o utilizador dentro de um loop onde é-lhe pedido uma que introduza um número inteiro.
    Esta função também verifica se o que foi introduzido está de acordo com o que se pretende.

    :return: Resposta do utilizador
    :rtype: int

    Exemplo de pedido:

    >>> input_int()
    #Resultado
    --> #Utilizador apenas prime ENTER, loop continua
    Tem de ser um número!
    --> quatro
    Tem de ser um número!
    --> 4
    4
    """

    while True:
        try:
            resposta = int(input("--> "))
            break
        
        except ValueError:
            print("Tem de ser um número!")

    return resposta


def input_float():
    """
    Pede ao utilizador um número decimal.

    Esta função coloca o utilizador dentro de um loop onde é-lhe pedido uma que introduza um número decimal.
    Esta função também verifica se o que foi introduzido está de acordo com o que se pretende.

    :return: Resposta do utilizador
    :rtype: float

    Exemplo de pedido:

    >>> input_float()
    #Resultado
    --> #Utilizador apenas prime ENTER, loop continua
    Tem de ser um número decimal!
    --> quatro ponto noventa e nove
    Tem de ser um número decimal!
    --> 4.99
    4.99
    """
    
    while True:
        try:
            resposta = float(input("--> "))
            break
        
        except ValueError:
            print("Tem de ser um número decimal!")

    return resposta


def input_bool():
    """
    Pede ao utilizador para escolher entre verdadeiro ou falso.

    Esta função coloca o utilizador dentro de um loop onde é-lhe pedido uma que introduza um valor de True ou False.
    Esta função também verifica se o que foi introduzido está de acordo com o que se pretende.

    :return: Resposta do utilizador
    :rtype: boolean

    Exemplo de pedido:

    >>> input_bool()
    #Resultado
    Opções disponíveis:
        1. True
        2. False
    Escolha uma opção: 3
    Opção não disponivel
    Opções disponíveis:
        1. True
        2. False
    Escolha uma opção: 2
    False
    """

    opcoes = ["True", "False"]

    listar_escolhas(opcoes)
    resposta = fazer_escolha(opcoes)

    return resposta