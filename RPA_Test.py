import psycopg2
from psycopg2 import Error
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time

try:
    connection = psycopg2.connect(user="avnadmin",
                                    password="AVNS_I2YSg3hf2GFrMM8X7eZ",
                                    host="pg-126b320f-ncgaloni-ec04.d.aivencloud.com",
                                    port="21577",
                                    database="dbCotacoes")
    cursor = connection.cursor()

    cursor.execute('CALL inserir_cotacao_dolar('09/23/2024', '19:08', '5.44')', (data, hora, cotacao_dolar))
    connection.commit()
    print("Dados inseridos com sucesso!")

except (Exception, Error) as error:
    print("Erro ao inserir os dados:", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Conexão encerrada.")
