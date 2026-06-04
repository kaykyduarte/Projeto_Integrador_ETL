import mysql.connector
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()


conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conn.cursor()

cursor.execute("""
SELECT
    COUNT(*),
    AVG(daily_social_media_hours),
    AVG(sleep_hours),
    AVG(stress_level),
    AVG(academic_performance)
FROM dados
""") 

resultado = cursor.fetchone()

total_registros = resultado[0]
media_rede = resultado[1]
media_sono = resultado[2]
media_stress = resultado[3]
media_academica = resultado[4]

data_extracao = datetime.now().strftime("%d/%m/%Y")

html = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Dashboard - Impacto das Redes Sociais</title>

    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f4f4f4;
        }}

        h1 {{
            text-align: center;
        }}

        table {{
            width: 70%;
            margin: auto;
            border-collapse: collapse;
            background-color: white;
        }}

        th, td {{
            border: 1px solid black;
            padding: 10px;
            text-align: center;
        }}

        th {{
            background-color: #dddddd;
        }}

        .info {{
            width: 70%;
            margin: 30px auto;
            background-color: white;
            padding: 15px;
            border: 1px solid #ccc;
        }}
    </style>

</head>
<body>

    <h1>Dashboard - Impacto das Redes Sociais nos Adolescentes</h1>

    <table>
        <tr>
            <th>Indicador</th>
            <th>Valor</th>
        </tr>

        <tr>
            <td>Total de Registros</td>
            <td>{total_registros}</td>
        </tr>

        <tr>
            <td>Média de Horas em Redes Sociais</td>
            <td>{media_rede:.2f}</td>
        </tr>

        <tr>
            <td>Média de Horas de Sono</td>
            <td>{media_sono:.2f}</td>
        </tr>

        <tr>
            <td>Média de Estresse</td>
            <td>{media_stress:.2f}</td>
        </tr>

        <tr>
            <td>Média de Desempenho Acadêmico</td>
            <td>{media_academica:.2f}</td>
        </tr>

    </table>

    <div class="info">
        <h3>Fonte dos Dados</h3>
        <p>https://www.kaggle.com/datasets/algozee/teenager-menthal-healy/data</p>

        <h3>Banco de Dados</h3>
        <p>MySQL - Base "projeto"</p>

        <h3>Data de Extração</h3>
        <p>{data_extracao}</p>
    </div>

</body>
</html>
"""

with open('dashboard.html', 'w', encoding='utf-8') as arquivo:
    arquivo.write(html)

print('HTML gerado com sucesso!')