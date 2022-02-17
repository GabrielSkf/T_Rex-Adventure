# Aqui criamos a tabela responsavel por armazenar a pontuação
import sqlite3
from sqlite3 import Error
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn,create_table_sql):
    try:
        crs = conn.cursor()
        crs.execute(create_table_sql)
    except Error as e:
        print(e)
        
def main():
    database = r"PONTUACAO.db"
    sql_create_projeto_table = '''CREATE TABLE IF NOT EXISTS Pont(
                                        id         INTEGER PRIMARY KEY,
                                        nome       TEXT NOT NULL,
                                        email      TEXT NOT NULL,
                                        Rank       INTEGER 
    );'''
    # create a database connection
    conn = create_connection(database)
    
    # efetivar a criação das tabelas
    if conn is not None:
        # criar a tabela de projeto
        create_table(conn,sql_create_projeto_table)
        # criar a tabela de tarefa
if __name__ == '__main__':
    main()
