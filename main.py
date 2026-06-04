import csv
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS dados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    physical_activity FLOAT,
    screen_time_before_sleep FLOAT,
    sleep_hours INT,
    daily_social_media_hours FLOAT,
    stress_level INT,
    academic_performance FLOAT
)
""")


with open('c:/datalake/gold/Teen_Mental_Health_Dataset.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for linha in reader:
        cursor.execute("""
            INSERT INTO dados (
                physical_activity,
                screen_time_before_sleep,
                sleep_hours,
                daily_social_media_hours,
                stress_level,
                academic_performance
            ) VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            float(linha['physical_activity']),
            float(linha['screen_time_before_sleep']),
            float(linha['sleep_hours']),
            float(linha['daily_social_media_hours']),
            int(linha['stress_level']),
            float(linha['academic_performance'])
        ))

conn.commit()

print("Dados inseridos com sucesso!")