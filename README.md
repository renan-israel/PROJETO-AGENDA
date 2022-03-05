# PROJETO AGENDAÍ
 Projeto de gestão de salão de beleza

**Trajeto de experiência:**

Meu objetivo ao criar o projeto AGENDAÍ em python foi de consolidação da aprendizagem desta linguagem de programação e também de todas as etapas que envolvem um projeto original e do zero que visa solucionar um problema do mundo real, como sua detecção, formulação e implementação.

O problema encontrado foi na gestão de um salão de beleza que realiza todos os seus processos de forma manual.

A partir de então planejei todos os processos feitos dentro do salão de beleza que podem ser sistematizados com a programação.

Os processos envolvem:

cadastro de clientes e funcionários;
agendamento de clientes;
visualização da agenda pelos funcionários e chefia;

Objetiva diminuir o trabalho da recepcionista e chefia deixando tudo quanto possível a cargo do programa.

**Explicação do programa:**

Encontra-se em dois 2 arquivos python, funções_e_variáveis (armazena as funções e variáveis) e sistema (ordenação e apresentação do arquivo funcoes_e_variaveis) e num arquivo de banco de dados MySQL.

Possui 2 partes: 1 - Cadastro de cliente e agendamento (interação com o usuário cliente) 2 - Edição de clientes e agendamos (interação com o funcionário)

1 - Capta e valida os dados do cliente e do agendamento inseridos de forma guiada por ele próprio e envia para o banco de dados.

2 - Através do menu é possível manipular todos os clientes e agendamentos realizados.

**Estrutura do banco de dados:**

Ver diagrama (em jpg) anexo.

**Intruções:**

Necessário instalar:
- MySQL (sugiro workbench, https://dev.mysql.com/downloads/workbench/ )
- Python (pycharm, vscode....)
- Bibliotecas Python:
from datetime import *
import mysql.connector
from mysql.connector import Error
