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
                database = 'Sistema'
            )

            if conexao.is_connected():
                print("Conexão bem-sucedida!")
                return conexao

        except Error as e:
            print(f"Erro ao conectar: {e}")
            return None
        
    def cadastrarProduto(self,conexao,nome, descricao, estoque, valor):
        try:
            cursor = conexao.cursor()
            query = "INSERT INTO Produtos(nome, descricao, estoque, valor) VALUES (%s,%s,%s,%s)"
            valores = (nome, descricao, estoque,valor)
            cursor.execute(query,valores)
            conexao.commit()
            print("Produto INSERIDO!")
            return True
            
        
        except Error as e:
            print(f"Erro ao inserir: {e}")
            return False

    def cadastrarUsuario(self, conexao, nome, login, senha):
        try:
            cursor = conexao.cursor()
            query = "INSERT INTO usuarios(nome, login, senha) VALUES (%s,%s,%s)"
            valores = (nome, login, senha)
            cursor.execute(query,valores)
            conexao.commit()
            print("USUARIO INSERIDO!")
            return True
            
        
        except Error as e:
            print(f"Erro ao inserir: {e}")
            return False
    
    def realizarVenda(self, conexao, idVendedor, nomeCliente, cpf, endereco, formaPagamento, idProduto, entrada, quantidadeParcelas, quantidade):
        try:
            cursor = conexao.cursor()
            query = "INSERT INTO Vendas(idVendedor, nomeCliente, cpf, endereco, formaPagamento, idProduto, entrada, quantidadeParcelas, quantidade) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            valores = (idVendedor, nomeCliente, cpf, endereco, formaPagamento, idProduto, entrada, quantidadeParcelas, quantidade)
            cursor.execute(query,valores)
            conexao.commit()
            print("Venda inserida!")
            return True
        
        except Error as e:
            print(f"Erro ao inserir: {e}")
            return False


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

    def relatorio(self,conexao):
        try:
            cursor = conexao.cursor()
            query = "SELECT u.nome as Vendedor, v.nomeCliente as Cliente, p.nome as Produto, v.valorTotal as Total, v.dataVenda as DataVenda FROM Vendas v JOIN Usuarios u ON u.id = v.idVendedor JOIN Produtos p ON p.id = v.idProduto"
            cursor.execute(query)
            resultados = cursor.fetchall()
            return resultados
        
        except Error as e:
            print(f"Erro ao inserir: {e}")


# database = Database()
# conexao = database.conectar()
# database.relatorio(conexao)