"""
Módulo de interação com bases de dados SQLite
---------------------------------------------

Este módulo faz a ligação com os ficheiros **.bd** que contém a base de dados da aplicação.
É utilizado como ponte entre as *queries* SQL e a sua execução na base de dados.

:Authors: Martim Teixeira
:Date: 12 de novembro de 2025
:Version: 1.0
"""

import sqlite3  #Módulo já vem instalado com Python

class FerramentasBD():
    """
    Classe com ferramentas para interagir com base de dados SQLite.
    ===============================================================

    Serve para centralizar todos os processos relacionados ao ponto em cima.
    Desta forma, só se escreve a lógica uma única vez e executa-se quando quisermos.

    Esta classe contém métodos e funções que:
    - Inicia conecção com base de dados;
    - Fecha conecção com base de dados;
    - Executa *queries* SQL na base de dados (com opção de imprimir tabelas);

    >>> basedados = FerramentasBD()
    """
    
    def __init__(self):
        #Conector para se fazer conecção com base de dados, global para a classe toda
        #Isto é necessário não só para não se repetir código com cada query,
        #mas também para que os métodos desta classe o possam usar.
        self.sqlconnector = None


    def conectarBD(self, ficheiro):
        """
        Inicia a conecção com base de dados.

        Para iniciar a base de dados, primeiro é necessário conectar à mesma.
        Se a base de dados não existir, ela será criada automaticamente.

        :param ficheiro: Nome do ficheiro **.bd** da base de dados a ser utilizado
        :type ficheiro: string

        >>> basedados.conectar("bd")
        """

        try:
            self.sqlconnector = sqlite3.connect(f'{str(ficheiro)}.db')
        
        except sqlite3.Error:
            print("Ocorreu um erro ao tentar conectar à base de dados.")


    def desconectarBD(self):
        """
        Desconecta base de dados.
        
        É necessário fechar a base de dados para que, caso a aplicação falhe, os dados não serem perdidos.
        Este método também limpa a variável **sqlconnector** da memória.

        >>> basedados.desconectarBD()
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
        Executa queries na base de dados.
        
        Cria-se um cursor para se poder interagir com a base de dados.
        Se a query enviar um resultado, o mesmo fica guardado, caso contrário fica **None**.
        Faz-se um commit das ações das queries (Não confundir com commits do Git)

        :param query: A query para ser executada na base de dados
        :type query: string
        :param imprimir: Se deve ou não imprimir tabelas
        :type imprimir: boolean

        >>> basedados.executar("SELECT * FROM Tabela;", imprimir=True)
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