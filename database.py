import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="fitpro"
    )


def executar_query(query, params=None):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(query, params or ())
        conexao.commit()
    except Exception as e:
        print("Erro na query:", e)
    finally:
        cursor.close()
        conexao.close()


def buscar_dados(query, params=None):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    try:
        cursor.execute(query, params or ())
        return cursor.fetchall()
    except Exception as e:
        print("Erro na busca:", e)
        return []
    finally:
        cursor.close()
        conexao.close()