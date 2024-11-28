import mysql.connector
from mysql.connector import Error

class Database:
    
    def __init__(self) -> None:
        pass

    def conectar(self):
        try:
            conexao = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = '',
                database = 'TrabalhoT31'
            )

            if conexao.is_connected():
                print("Conexão bem-sucedida!")
                return conexao

        except Error as e:
            print(f"Erro ao conectar: {e}")
            return None
        
    def cadastrarUsuario(self, conexao, nome, senha):
        try:
            cursor = conexao.cursor()
            query = "INSERT INTO usuarios(nome, senha) VALUES (%s,%s)"
            valores = (nome,senha)
            cursor.execute(query,valores)
            conexao.commit()
            print("Dados inseridos com sucesso!")
        
        except Error as e:
            print(f"Erro ao inserir: {e}")

    def getUsuarios(self, conexao):
        try:
            cursor = conexao.cursor()
            query = "SELECT * FROM usuarios"
            cursor.execute(query)
            resultados = cursor.fetchall()
            return resultados
        
        except Error as e:
            print(f"Erro ao inserir: {e}")

    def atualizar_dados(self, conexao, nome, novo_curso):
        try:
            cursor = conexao.cursor()
            query = "UPDATE alunos SET curso = %s WHERE nome = %s"
            valores = (novo_curso, nome)
            cursor.execute(query,valores)
            conexao.commit()
            print("Dados atualizados com sucesso!")
        
        except Error as e:
            print(f"Erro ao inserir: {e}")

    def deletar_usuario(self, conexao, nome):
        try:
            cursor = conexao.cursor()
            query = "DELETE FROM alunos WHERE nome = %s"
            valores = (nome,)
            cursor.execute(query,valores)
            conexao.commit()
            print("Dados deletados com sucesso!")
        
        except Error as e:
            print(f"Erro ao inserir: {e}")

# teste = conectar()
# cadastrarUsuario(teste,"admin","admin")
