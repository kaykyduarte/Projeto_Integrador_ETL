# Projeto_Integrador_ETL

1. DESCRIÇÃO DO PROJETO

Este projeto tem como objetivo analisar dados relacionados ao impacto das redes sociais na saúde mental de adolescentes utilizando Python e MySQL.

O processo consiste em:

- Importar os dados de um arquivo CSV.
- Armazenar os dados em uma tabela MySQL.
- Realizar consultas para gerar indicadores.
- Criar um dashboard em HTML contendo informações estatísticas extraídas do banco de dados.

Os indicadores apresentados incluem:

- Total de registros analisados.
- Média de horas diárias em redes sociais.
- Média de horas de sono.
- Média do nível de estresse.
- Média do desempenho acadêmico.

--------------------------------------------------

2. FONTE DOS DADOS

Dataset utilizado:

Teen Mental Health Dataset

Fonte:
Kaggle - Plataforma de Ciência de Dados (Data Science) e Machine Learning 
Ele abriga milhares de conjuntos de dados reais e gratuitos sobre absolutamente tudo: finanças, comportamento de usuários, medicina, esportes, e-commerce e tweets.


Tema:
Relação entre uso de redes sociais, sono, atividade física, estresse e desempenho acadêmico em adolescentes.

--------------------------------------------------

3. TECNOLOGIAS UTILIZADAS

- Python 3
- MySQL Server
- MySQL Connector Python
- HTML
- CSV

5. CRIAÇÃO DO BANCO DE DADOS

Executar no MySQL:

CREATE DATABASE projeto;

--------------------------------------------------

6. INSTALAÇÃO DAS DEPENDÊNCIAS

No terminal, executar:

pip install mysql-connector-python

--------------------------------------------------

7. CONFIGURAÇÃO DA CONEXÃO

No arquivo main.py, configurar:

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SUA_SENHA",
    database="projeto"
)

Substituir SUA_SENHA pela senha configurada no MySQL.

8. COMO EXECUTAR

1. Iniciar o MySQL Server.
2. Criar o banco de dados "projeto".
3. Colocar o arquivo CSV no caminho configurado.
4. Executar:

 main.py

9. AUTOR

Nome: Kayky Duarte Del Bosque

Curso: Inteligência Artificial e Dados

