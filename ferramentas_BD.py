"""
Módulo de interação com bases de dados SQLite
---------------------------------------------

Este módulo faz a ligação com os ficheiros **.bd** que contém a base de dados da aplicação.
É utilizado como ponte entre as *queries* SQL e a sua execução na base de dados.
"""

import sqlite3  #Módulo já vem instalado com Python

class FerramentasBD():
    """
    Classe com ferramentas para interagir com base de dados SQLite.

    Serve para centralizar todos os processos relacionados ao ponto em cima.
    Desta forma, só se escreve a lógica uma única vez e executa-se quando quisermos.

    Esta classe contém métodos e funções que:

    - Inicia conecção com base de dados;
    - Fecha conecção com base de dados;
    - Executa *queries* SQL na base de dados (com opção de imprimir tabelas);

    Exemplo de inicialização da classe:

    >>> basedados = FerramentasBD()
    """
    
    def __init__(self):
        #Conector para se fazer conecção com base de dados, global para a classe toda
        #Isto é necessário não só para não se repetir código com cada query,
        #mas também para que os métodos desta classe o possam usar.
        self.sqlconnector = None


    def conectarBD(self):
        """
        Inicia a conecção com base de dados.

        Para iniciar a base de dados, primeiro é necessário conectá-la.
        Se a base de dados não existir, ela será criada automaticamente.
        Esta função utiliza o módulo **sqlite** que vem pre-instalado com o Python
        para criar o objeto de conecção **sqlconnector**.

        :param ficheiro: Nome do ficheiro **.bd** da base de dados a ser utilizado
        :type ficheiro: string

        :raise sqlite3.Error: Se ocorrer algum erro durante a conecção

        Exemplo de conecção com base de dados: 

        >>> basedados.conectarBD("bd")
        """

        try:
            self.sqlconnector = sqlite3.connect(f'basedados.db')
        
        except sqlite3.Error:
            print("Ocorreu um erro ao tentar conectar à base de dados.")


    def desconectarBD(self):
        """
        Desconecta base de dados.
        
        É necessário fechar a base de dados para que, caso a aplicação falhe, os dados não serem perdidos.
        Este método fecha e limpa a variável **sqlconnector** da memória.

        :raise sqlite3.Error: Se ocorrer algum erro durante a o desconecção

        Exemplo de fechar conecção:

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
        Após a execução, faz um commit das ações das queries.

        Caso for necessário, esta também chama uma função para imprimir tabelas formatadas.

        :param query: A query para ser executada na base de dados
        :type query: string

        :param imprimir: Se deve ou não imprimir tabelas
        :type imprimir: boolean

        :return: Resultado da *query*
        :rtype: list

        :raise sqlite3.Error: Se ocorrer algum erro durante a criação do cursor ou na execução

        Exemplo de execução de querie com impressão de tabela:
        
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
                        self.imprimir_tabela(cursor.description, cursor.fetchall())
                    
                    resultado = cursor.fetchall()  #Retirar todas as linhas e guardar na variável
                    return resultado
                    
                except sqlite3.Error:
                    print("Ocorreu um erro ao executar commandos SQL.")
            
            else:
                print("Não é possível executar SQL porque cursor não existe.")
            
        else:
            print("Base de dados não está conectada.")


    def imprimir_tabela(self, headers, dados):
        """
        Imprime tabelas de forma formatada.

        Uma vez que o resultado que advém da execução de queries que devolvem tabelas é uma lista com tuples,
        para que o utilizador perceba o que está a ser apresentado, o resultado tem de ser formatado.

        Para tal, este método faz a iteração pelos *headers* (cabeçalhos) e dados para encontrar aquele com maior comprimento.
        Estes comprimentos são depois guardados numa lista para serem usados na construção das colunas da tabela.
        Quando os dados necessários para a construção da tabelas estiverem prontos, são construídas strings para cada linha da tabela,
        que são depois guardados numa lista, prontos para serem impressos.

        Uma limitação do método, é que os header têm de estar no mesmo formato que o módulo **sqlite** fornece em **cursor.description**.

        :param headers: Headers (cabeçalhos) da tabela, cada valor deve estar numa lista/tuple
        :type headers: list

        :param dados: Lista de dados retirados de uma tabela, organizados por linha
        :type dados: list

        Exemplo com dados retirados de queries:

        >>> imprimir_tabela(cursor.description, cursor.fetchall())

        Exemplo com dados externos:

        >>> imprimir_tabela([("Idade"), ("Nome"), ("Contacto")],
                            [(21, "João", 999999999),
                            (23, "Mariana", 888888888)
                            ])
        """

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