# Projeto Gestão de Recessão de Hotel

Projeto de Universidade utilizando ferramenta Git.
Aplicação de gestão de recessão de hotel.

## Descrição do Projeto

Este trata-se de uma aplicação de linha de commandos (CLI ou Command-Line Interface) para gerir a recessão de um hotel.

De momentos é uma *front end* escrita em Python com uma futura base de dados em SQLite.

## Clonar repositório

Executar comando abaixo num diretório na máquina local, à sua escolha.
Só precisa de ser executado uma vez para criar uma cópia do repositório.

``` git
git clone https://github.com/martimteixeiraa89796/gestao-recessao-hotel.git
```

## Testar/Usar aplicação

1. Instalar [Python](https://www.python.org/);
2. Abrir linha de comandos no diretório do repositório;
3. Iniciar aplicação com o comando: `python main.py`;

O VSCode pode ser utilizado como alternativa ao passo 2 e 3, mas deve instalar a [extensão para Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

## Ramos

- **main:** Ramo para código estável.
- **dev:** Ramo para código em desenvolviemnto.
- **basedados:** Ramo para desenvolvimento relacionado a BDs.
- **test:** Ramo para testes, não deveria ser feito merges com ele.

> [!IMPORTANT]
> Não apagar ramos utilizados, eles vão ser usados para avaliação.

## Fazer *Pull* do repositório (Atualizar/*Download*)

Primeiro fazer ***checkout*** no ramo que queremos:

``` git
git checkout <inserir ramo aqui>
```

Depois fazer ***pull*** do ramo:

``` git
git pull
```

> [!Note]
> Isto faz um ***merge*** automático do ***remote*** com o ***local***, por isso podem surgir casos de conflito que terão de ser resolvidos como nos ***merges*** normais.

## Fazer *Push* do repositório (*Upload*)

Primeiro fazer ***checkout*** no ramo que queremos:

``` git
git checkout <inserir ramo aqui>
```

Depois fazer ***push*** do ramo:

``` git
git push
```

> [!Note]
> Se o ***push*** não funcionar tenta fazer ***pull*** do repositório.
