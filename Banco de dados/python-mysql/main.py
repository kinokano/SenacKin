import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexao = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'escola'
        )

        if conexao.is_connected():
            print("Conexão bem-sucedida!")
            return conexao

    except Error as e:
        print(f"Erro ao conectar: {e}")
        return None
    
def inserir_dados(conexao, nome, idade, curso):
    try:
        cursor = conexao.cursor()
        query = "INSERT INTO alunos (nome,idade,curso) VALUES (%s,%s,%s)"
        valores = (nome,idade,curso)
        cursor.execute(query,valores)
        conexao.commit()
        print("Dados inseridos com sucesso!")
    
    except Error as e:
        print(f"Erro ao inserir: {e}")

def selecionar_dados(conexao):
    try:
        cursor = conexao.cursor()
        query = "SELECT * FROM alunos"
        cursor.execute(query)
        resultados = cursor.fetchall()

        for i in resultados:
            print(i)
    
    except Error as e:
        print(f"Erro ao inserir: {e}")

def atualizar_dados(conexao, nome, novo_curso):
    try:
        cursor = conexao.cursor()
        query = "UPDATE alunos SET curso = %s WHERE nome = %s"
        valores = (novo_curso, nome)
        cursor.execute(query,valores)
        conexao.commit()
        print("Dados atualizados com sucesso!")
    
    except Error as e:
        print(f"Erro ao inserir: {e}")

def deletar_usuario(conexao, nome):
    try:
        cursor = conexao.cursor()
        query = "DELETE FROM alunos WHERE nome = %s"
        valores = (nome,)
        cursor.execute(query,valores)
        conexao.commit()
        print("Dados deletados com sucesso!")
    
    except Error as e:
        print(f"Erro ao inserir: {e}")

con = conectar()
nome = 'Kin'
idade = 23
curso = 'TADS'


# inserir_dados(con, nome, idade, curso)
#atualizar_dados(con, 'Kin', 'CC')
deletar_usuario(con, nome)
selecionar_dados(con)
