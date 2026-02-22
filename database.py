import psycopg2
import os

# ========= CONEXAO COM O BANCO DE DADOS =========
try:
    conexao = psycopg2.connect(
        dbname="to_do_list_db",
        user="postgres",
        password= os.getenv("DB_SENHA"),
        host="localhost",
        port="5432"
    )

    conexao_cursor = conexao.cursor() #cursor -> executa comandos SQL
    print("\n+----------------------------------+\n")
    print("| Conexão realizada com sucesso! |")
    print("\n+----------------------------------+\n")

except Exception as erro:
    print("\n+----------------------------------+\n")
    print("Erro ao conectar:", erro)
    print("\n+----------------------------------+\n")
