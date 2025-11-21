"""
Módulo com função para ajudar com input do utilizador
-----------------------------------------------------

Este módulo contém funções com tudo o que é necessário para se interagir com o utilizador.
"""

def listar_escolhas(lista):
    """
    Imprime uma listagem de listas.

    Esta função faz uma listagem numérica do que lhe é fornecido.
    Isto é feito através da iteração na lista e construção de strings para serem imprimidas.

    :param lista: Lista com os objetos para listagem
    :type lista: list

    Exemplo de listagem:

    >>> listar_escolhas(["Azul", "Vermelho", "Amarelo"])
    """

    print("Opções disponíveis:")
    for item in range(len(lista)):
        print(f"    {item + 1}. {lista[item]}".title())


def fazer_escolha(lista):
    """
    De uma lista, pregunta *input* ao utilizador e retorna a resposta.

    Esta função cria um loop onde o utilizador tem de escolher uma opção baseado numa lista que
    é fornecida á função. O loop termina se a escolha for válida.

    :return: Opção escolhida pelo utilizador
    :rtype: Depende do valor inseridos

    Exemplo de ambiente de escolha:

    >>> fazer_escolha(["Banana", "Maçã", "Pera"])
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

    :return: Resposta do utilizador traduzida
    :rtype: string, int ou float

    Exemplo de execução:

    >>> sql_escolher_tipo()
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