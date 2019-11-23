import sqlite3
import atexit

def get_connection():
    global con
    if not con:
        con = sqlite3.connect('biblia.db')
    atexit.register(close_connection, con)
    return con

def close_connection(some_con):
    some_con.commit()
    some_con.close()
     
def create_database(cursor):
    # criando a tabela (schema) - livros
    cursor.execute("""
    CREATE TABLE if not exists livros (
            id INTEGER NOT NULL PRIMARY KEY,
            nome TEXT NOT NULL
    );
    """)
 
    # criando a tabela (schema) - lista_livros
    cursor.execute("""
    CREATE TABLE if not exists lista_livros (
            id INTEGER NOT NULL PRIMARY KEY,
            livro TEXT NOT NULL,
            testamento INTEGER NOT NULL,
            total INTEGER
    );
    """)
 
    # criando a tabela (schema) - versiculos
    cursor.execute("""
    CREATE TABLE if not exists versiculos (
            id_livro INTEGER NOT NULL,
            id_capitulo INTEGER NOT NULL,
            id_versiculo INTEGER NOT NULL,
            texto TEXT NOT NULL,
            PRIMARY KEY (id_livro, id_capitulo, id_versiculo)
    );
    """)
 