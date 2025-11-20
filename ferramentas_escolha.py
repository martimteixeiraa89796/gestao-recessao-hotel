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