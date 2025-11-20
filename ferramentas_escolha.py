def listar_escolhas(lista):
    print("Opções disponíveis:")
    for item in range(len(lista)):
        print(f"    {item + 1}. {lista[item]}".title())


def fazer_escolha(lista):
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