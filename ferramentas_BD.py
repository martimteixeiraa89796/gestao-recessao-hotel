import sqlite3  #Módulo já vem instalado com Python

class FerramentasBD():
    """
    # FerramentasBD
    Classe com ferramentas para interagir com base de dados sqlite. É necessário inicia-la para poder ser usada.
    
    **Não colocar SQL queries dentro desta classe! Esta classe faz somente a ponte para a base de dados**

    ## Métodos:
    - **conectarBD:** Inicia a conecção com base de dados.
    - **desconectarBD:** Desconecta base de dados.
    - **executarBD:** Executa queries na base de dados.
    """
    
    def __init__(self):
        #Conector para se fazer conecção com base de dados, global para a classe toda
        #Isto é necessário não só para não se repetir código com cada query,
        #mas também para que os métodos desta classe o possam usar.
        self.sqlconnector = None


    def conectarBD(self, ficheiro):
        """
        # conectarBD
        Inicia a conecção com base de dados.
        - Para iniciar a base de dados, primeiro é necessário conectar à mesma.
        - Se a base de dados não existir, ela será criada automaticamente.

        ## Argumentos:
        - **ficheiro:** Nome do ficheiro da base de dados a ser utilizado
          - **Nota:** Ficheiros são automaticamente criados com extensão .bd
        """

        try:
            self.sqlconnector = sqlite3.connect(f'{str(ficheiro)}.db')
        
        except sqlite3.Error:
            print("Ocorreu um erro ao tentar conectar à base de dados.")


    def desconectarBD(self):
        """
        # desconectarBD
        Desconecta base de dados.
        - É necessário fechar a base de dados para que, caso a aplicação falhe, os dados não serem perdidos.
        - Este método também limpa a variável **sqlconnector** da memória.
        """

        if self.sqlconnector:
            try:
                self.sqlconnector.close()
                self.sqlconnector = None
            
            except sqlite3.Error:
                print("Ocorreu um erro ao tentar desconectar base de dados.")
        
        else:
            print("Base de dados não está conectada.")


    def executarBD(self, query, imprimir=False):
        """
        # executarBD
        Executa queries na base de dados.
        - Cria-se um cursor para se poder interagir com a base de dados.
        - Se a query enviar um resultado, o mesmo fica guardado, caso contrário fica **None**.
        - Faz-se um commit das ações das queries (Não confundir com commits do Git)

        ## Argumentos:
        - **query:** A query para ser executada
        """
        
        if self.sqlconnector:
            try:
                cursor = self.sqlconnector.cursor()  #Criar cursor para interagir com base de dados
            
            except sqlite3.Error:
                print("Ocorreu um erro ao tentar criar cursor.")

            if cursor:
                try:
                    cursor.execute(str(query))
                    self.sqlconnector.commit()  #Fazer commit das ações

                    if imprimir:
                        resultado = self.imprimir_tabela(cursor.description, cursor.fetchall())
                    
                    resultado = cursor.fetchall()  #Retirar todas as linhas e guardar na variável
                    return resultado
                    
                except sqlite3.Error:
                    print("Ocorreu um erro ao executar commandos SQL.")
            
            else:
                print("Não é possível executar SQL porque cursor não existe.")
            
        else:
            print("Base de dados não está conectada.")


    def imprimir_tabela(self, headers, dados):
        headers_listados = []
        comprimento_listado = []

        #Listar headers
        for linha in headers:
            headers_listados.append(linha[0])

        #Calcular comprimento para cada coluna
        for coluna in range(len(headers_listados)): #Iterar pelas colunas horizontalmente
            comprimento_celula = len(str(headers_listados[coluna]))
            
            for linha in dados: #Iterar pelas linhas verticalmente
                novo_comprimento = len(str(linha[coluna])) #Celula

                if comprimento_celula < novo_comprimento:
                    comprimento_celula = novo_comprimento

            comprimento_listado.append(comprimento_celula)

        #Contruir tabela
        tabela = []
        tabela.append(headers_listados)
        
        for linha in dados:
            tabela.append(linha)

        #Formatar tabela
        tabela_formatada = []

        for linha in tabela:
            nova_linha = "| "
            for coluna in range(len(linha)):
                formatado = str(linha[coluna]) + " "*(comprimento_listado[coluna]-len(str(linha[coluna])))
                nova_linha += formatado + " | "
            tabela_formatada.append(nova_linha)

        #imprimir tabela
        for linha in tabela_formatada:
            print(linha)