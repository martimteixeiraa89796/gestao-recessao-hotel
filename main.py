import ferramentas_BD
import ferramentas_escolha
import funcoes_sqlite_create
import funcoes_sqlite_delete
import funcoes_sqlite_insert
import funcoes_sqlite_select
import funcoes_sqlite_update
import verificar_e_atualizar_bd

def continuar():
    input("Primma Enter para continuar... ")


verificar_e_atualizar_bd.verificador_tabelas()


while True:
    print("""
  ____           _   /\\/|             _                                       
 / ___| ___  ___| |_|/\\/_  ___     __| | ___                                  
| |  _ / _ \\/ __| __/ _` |/ _ \\   / _` |/ _ \\                                 
| |_| |  __/\\__ \\ || (_| | (_) | | (_| |  __/                                 
 \\____|\\___||___/\\__\\__,_|\\___/\\/|\\__,_|\\___|  _        _   _       _       _ 
|  _ \\ ___  ___ ___  ___ ___ |/\\/_  ___     __| | ___  | | | | ___ | |_ ___| |
| |_) / _ \\/ __/ _ \\/ __/ __|/ _` |/ _ \\   / _` |/ _ \\ | |_| |/ _ \\| __/ _ \\ |
|  _ <  __/ (_|  __/\\__ \\__ \\ (_| | (_) | | (_| |  __/ |  _  | (_) | ||  __/ |
|_| \\_\\___|\\___\\___||___/___/\\__,_|\\___/   \\__,_|\\___| |_| |_|\\___/ \\__\\___|_|
                                                                               
    """)

    opcoes = ["Visualizar dados",
              "Atualizar dados",
              "Inserir dados",
              "Apagar dados",
              "Sair"
              ]
    
    ferramentas_escolha.listar_escolhas(opcoes)
    escolha = ferramentas_escolha.fazer_escolha(opcoes, cancelar=False)
    
    if escolha == opcoes[0]:
        opcoes = ["Ver Tabelas",
                  "Dados específicos"
                  ]

        ferramentas_escolha.listar_escolhas(opcoes)
        escolha = ferramentas_escolha.fazer_escolha(opcoes)
        
        if escolha:
            if escolha == opcoes[0]:
                funcoes_sqlite_select.select_geral_escolha()
                continuar()

            elif escolha == opcoes[1]:
                opcoes = ["Ver Horario",
                        "Ver Quartos Livres",
                        "Ver Clientes Nos Quartos",
                        "Ver Chegada De Clientes",
                        "Contar Camas",
                        "Estadia"
                        ]

                ferramentas_escolha.listar_escolhas(opcoes)
                escolha = ferramentas_escolha.fazer_escolha(opcoes) 

                if escolha:
                    if escolha == opcoes[0]:
                        funcoes_sqlite_select.ver_horario()
                        continuar()

                    elif escolha == opcoes[1]:
                        funcoes_sqlite_select.ver_quarto_livers()
                        continuar()

                    elif escolha == opcoes[2]:
                        funcoes_sqlite_select.ver_cliente_em_quarto()
                        continuar()

                    elif escolha == opcoes[3]:
                        funcoes_sqlite_select.ver_chegada_cliente()
                        continuar()

                    elif escolha == opcoes[4]:
                        funcoes_sqlite_select.contar_camas_em_quarto()
                        continuar()
                    
                    elif escolha == opcoes[5]:
                        funcoes_sqlite_select.estadia()
                        continuar()

    elif escolha == opcoes[1]:
        funcoes_sqlite_update.update_geral_escolha()
        continuar()

    elif escolha == opcoes[2]:
        funcoes_sqlite_insert.mapeador_inserts()
        continuar()

    elif escolha == opcoes[3]:
        opcoes = ["Apagar todos os dados",
                  "Apagar dado específico"
                  ]
        
        ferramentas_escolha.listar_escolhas(opcoes)
        escolha = ferramentas_escolha.fazer_escolha(opcoes)

        if escolha:
            if escolha == opcoes[0]:
                funcoes_sqlite_delete.limpar_tabela_geral_escolha()
                continuar()

            elif escolha == opcoes[1]:
                funcoes_sqlite_delete.delete_geral_escolha()

    elif escolha == opcoes[4]:
        break
