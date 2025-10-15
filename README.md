\# Sistema de Cadastro de Candidatas



Sistema simples para cadastrar e listar candidatas usando Python e SQL Server.



\## O que faz



\- Cadastra candidatas com nome e clube

\- Lista todas as candidatas registradas

\- Armazena os dados em um banco SQL Server local



\## Requisitos



\- Python 3.6 ou superior

\- SQL Server instalado localmente

\- ODBC Driver 17 for SQL Server

\- Biblioteca `pyodbc`



\## Instalação



1\. Instale a biblioteca necessária:



```bash

pip install pyodbc

```



2\. Certifique-se de que o SQL Server está rodando na sua máquina



3\. O banco de dados `CandidatasDB` será criado automaticamente na primeira execução



\## Como usar



Execute o programa:



```bash

python main.py

```



O sistema mostra um menu com 3 opções:



1\. \*\*Inserir Nova Candidata\*\* - cadastra uma nova candidata informando nome e clube

2\. \*\*Listar Todas as Candidatas\*\* - mostra todas as candidatas cadastradas

3\. \*\*Sair\*\* - encerra o programa



\## Estrutura do projeto



```

├── database.py    # Conexão com banco e funções SQL

├── main.py        # Interface do sistema e menu principal

└── README.md      # Este arquivo

```



\## Configuração do banco



Se precisar alterar as configurações de conexão, edite as variáveis no arquivo `database.py`:



\- `SERVER\_NAME` - nome do servidor (padrão: localhost)

\- `DATABASE\_NAME` - nome do banco (padrão: CandidatasDB)



\## Observações



\- A tabela é criada automaticamente na primeira execução

\- Os campos de imagem (ImagemCandidata e ImagemClube) estão preparados mas não são utilizados ainda

