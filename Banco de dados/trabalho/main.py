import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
from crud import *
from crud import Database

database = Database()
conexao = database.conectar()



# Função para verificar o login
def verificar_login(root, telaLogin):
    
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    
    usuarios = database.getUsuarios(conexao)
    # Credenciais de exemplo

    for i in usuarios:
       
        if usuario == i[2] and senha == i[3]:
            if usuario == 'admin':
                messagebox.showinfo("Login Bem-sucedido", "Bem-vindo, " + usuario + "!")
                telaAdm(root, telaLogin)
                break
                # Fecha a tela de login
            else:
                messagebox.showinfo("Login Bem-sucedido", "Bem-vindo, " + usuario + "!")
                telaVendedor(root, telaLogin, i[0])
                break
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos!")

    entry_usuario.delete(0, tk.END)
    entry_senha.delete(0, tk.END)
    

# Função para abrir a tela interna após login bem-sucedido
def telaAdm(root, telaLogin):
    
    telaLogin.pack_forget()
    telaAdm = tk.Frame(root,bg='lightblue')
    

    titulo = tk.Label(telaAdm, text="Tela do Administrador!", font=("Arial", 14))
    titulo.pack(pady=20)

    botao_cadastrar = tk.Button(telaAdm, text="Cadastrar Vendedor", command= lambda: telaCadastrar(root, telaAdm))
    botao_cadastrar.pack(pady=20)

    botao_gerarCsv = tk.Button(telaAdm, text="Gerar Relatório", command= lambda: gerarCsv())
    botao_gerarCsv.pack(pady=20)

    botao_sair = tk.Button(telaAdm, text="Sair", command= lambda: fecharTela(telaAdm, telaLogin))
    botao_sair.pack(pady=20)

    telaAdm.pack()

def fecharTela(a, b):
    a.pack_forget()  # Esconde a tela atual
    b.pack()

def telaVendedor(root, telaLogin, idVendedor):
    telaLogin.pack_forget()
    telaVendedor = tk.Frame(root,bg='lightblue')
    

    titulo = tk.Label(telaVendedor, text="Tela do Vendedor!", font=("Arial", 14))
    titulo.pack(pady=20)

    botao_realizarVenda = tk.Button(telaVendedor, text="Realizar Venda", command= lambda: telaVenda(root, telaVendedor, idVendedor))
    botao_realizarVenda.pack(pady=20)

    botao_cadastrarProtudo = tk.Button(telaVendedor, text="Cadastrar Produto", command= lambda: telaProduto(root, telaVendedor))
    botao_cadastrarProtudo.pack(pady=20)

    botao_sair = tk.Button(telaVendedor, text="Sair", command= lambda: fecharTela(telaVendedor, telaLogin))
    botao_sair.pack(pady=20)

    telaVendedor.pack()

def telaProduto(root, telaVendedor):
    telaVendedor.pack_forget()
    telaProduto = tk.Frame(root, bg='lightblue')
    
    titulo = tk.Label(telaProduto, text="Cadastrar Produto!", font=("Arial", 14))
    titulo.pack(pady=20)

    label_nomeProduto = tk.Label(telaProduto, text="Nome do produto:")
    label_nomeProduto.pack(pady=5)
    entry_nomeProduto = tk.Entry(telaProduto)
    entry_nomeProduto.pack(pady=5)

    label_descricao = tk.Label(telaProduto, text="Descrição:")
    label_descricao.pack(pady=5)
    entry_descricao = tk.Entry(telaProduto)
    entry_descricao.pack(pady=5)

    label_estoque = tk.Label(telaProduto, text="Estoque:")
    label_estoque.pack(pady=5)
    entry_estoque = tk.Entry(telaProduto)
    entry_estoque.pack(pady=5)

    label_valor = tk.Label(telaProduto, text="Valor:")
    label_valor.pack(pady=5)
    entry_valor = tk.Entry(telaProduto)
    entry_valor.pack(pady=5)

    botao_cadastrarProduto = tk.Button(telaProduto, text="Cadastrar", command=lambda: cadastrarProduto(entry_nomeProduto, entry_descricao, entry_estoque, entry_valor))
    botao_cadastrarProduto.pack(pady=20)

    botao_sair = tk.Button(telaProduto, text="Sair", command= lambda: fecharTela(telaProduto, telaVendedor))
    botao_sair.pack(pady=20)

    telaProduto.pack()
    

def telaVenda(root, telaVendedor, idVendedor):
    telaVendedor.pack_forget()
    telaVenda = tk.Frame(root, bg='lightblue')
    
    titulo = tk.Label(telaVenda, text="Tela de venda!", font=("Arial", 14))
    titulo.pack(pady=20)
    
    label_nomeCliente = tk.Label(telaVenda, text="Nome Cliente:")
    label_nomeCliente.pack(pady=5)
    entry_nomeCliente = tk.Entry(telaVenda)
    entry_nomeCliente.pack(pady=5)

    label_cpf = tk.Label(telaVenda, text="CPF:")
    label_cpf.pack(pady=5)
    entry_cpf = tk.Entry(telaVenda)
    entry_cpf.pack(pady=5)

    label_endereco =  tk.Label(telaVenda, text="Endereço:")
    label_endereco.pack(pady=5)
    entry_endereco = tk.Entry(telaVenda)
    entry_endereco.pack(pady=5)
    
    label_formaPagamento = tk.Label(telaVenda, text="Forma de pagamento:")
    label_formaPagamento.pack(pady=20)

    opcoes = ['à vista', 'parcelado']
    formaPagamento = ttk.Combobox(telaVenda, values=opcoes)
    formaPagamento.set("")  # Definir a opção padrão
    formaPagamento.pack()
    
    label_idProduto =  tk.Label(telaVenda, text="ID do produto:")
    label_idProduto.pack(pady=5)
    entry_idProduto = tk.Entry(telaVenda)
    entry_idProduto.pack(pady=5)

    label_entrada =  tk.Label(telaVenda, text="Entrada:")
    label_entrada.pack(pady=5)
    entry_entrada = tk.Entry(telaVenda)
    entry_entrada.pack(pady=5)

    label_qtdParcelas =  tk.Label(telaVenda, text="Quantidade de parcelas:")
    label_qtdParcelas.pack(pady=5)
    entry_qtdParcelas = tk.Entry(telaVenda)
    entry_qtdParcelas.pack(pady=5)

    label_qtdProduto =  tk.Label(telaVenda, text="Quantidade do produto:")
    label_qtdProduto.pack(pady=5)
    entry_qtdProduto = tk.Entry(telaVenda)
    entry_qtdProduto.pack(pady=5)

    botao_realizarVenda = tk.Button(telaVenda, text="Cadastrar", command=lambda: realizarVenda(idVendedor, entry_nomeCliente, entry_cpf, entry_endereco, formaPagamento, entry_idProduto, entry_entrada, entry_qtdParcelas, entry_qtdProduto))
    botao_realizarVenda.pack(pady=20)

    botao_sair = tk.Button(telaVenda, text="Sair", command= lambda: fecharTela(telaVenda, telaVendedor))
    botao_sair.pack(pady=20)

    telaVenda.pack()

def realizarVenda(idVendedor, nomeCliente, cpf, endereco, formaPagamento, idProduto, entrada, quantidadeParcelas, quantidade):
    venda = database.realizarVenda(conexao, idVendedor, nomeCliente.get(), cpf.get(), endereco.get(), formaPagamento.get(), idProduto.get(), entrada.get(), 
                                   quantidadeParcelas.get(), quantidade.get())
    
    nomeCliente.delete(0, tk.END) 
    cpf.delete(0, tk.END) 
    endereco.delete(0, tk.END)
    formaPagamento.delete(0, tk.END)
    idProduto.delete(0, tk.END)
    entrada.delete(0, tk.END)
    quantidadeParcelas.delete(0, tk.END)
    quantidade.delete(0, tk.END)
    
def telaCadastrar(root, telaAdm):
    telaAdm.pack_forget()
    telaCadastrar = tk.Frame(root,bg='lightblue')
    
    titulo = tk.Label(telaCadastrar, text="Tela de Cadastro!", font=("Arial", 14))
    titulo.pack(pady=20)
    
    label_name = tk.Label(telaCadastrar, text="Nome:")
    label_name.pack(pady=5)
    entry_name = tk.Entry(telaCadastrar)
    entry_name.pack(pady=5)


    label_user = tk.Label(telaCadastrar, text="Username:")
    label_user.pack(pady=5)
    entry_user = tk.Entry(telaCadastrar)
    entry_user.pack(pady=5)

    # Rótulo e entrada para a senha
    label_password = tk.Label(telaCadastrar, text="Senha:")
    label_password.pack(pady=5)
    entry_password = tk.Entry(telaCadastrar, show="*")
    entry_password.pack(pady=5)
    botao_cadastrar = tk.Button(telaCadastrar, text="Cadastrar", command=lambda: cadastrarUsuario(entry_name, entry_user, entry_password))
    botao_cadastrar.pack(pady=20)

    botao_sair = tk.Button(telaCadastrar, text="Sair", command= lambda: fecharTela(telaCadastrar, telaAdm))
    botao_sair.pack(pady=20)


    telaCadastrar.pack()   

def cadastrarUsuario(nome, user, password):
   
    cadastro = database.cadastrarUsuario(conexao, nome.get(), user.get(), password.get())
    nome.delete(0, tk.END)
    user.delete(0, tk.END)
    password.delete(0, tk.END)

def cadastrarProduto(nome, descricao, estoque, valor):
    cadastrarP = database.cadastrarProduto(conexao, nome.get(), descricao.get(), estoque.get(), valor.get())
    nome.delete(0, tk.END)
    descricao.delete(0, tk.END)
    estoque.delete(0, tk.END)
    valor.delete(0, tk.END)


def gerarCsv():
    # Conectar ao banco de dados SQLite
    resultados = database.relatorio(conexao)

    if resultados:
        # Abrir o arquivo CSV em modo de escrita
        with open('relatorio_clientes.csv', mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=',')  # Usando vírgula como delimitador
            
            # Escreve o cabeçalho (somente uma vez)
            writer.writerow(["Nome Vendedor", "Nome cliente", "Produto", "Total", "Data"])
            
            # Escreve os dados da consulta no CSV
            for linha in resultados:
                writer.writerow(linha)
        
        print("Relatório gerado!")
    else:
        print("Erro ao gerar relatório!")


# Janela de login
root = tk.Tk()
root.geometry("500x700")
root.configure(bg='lightblue')

telaLogin = tk.Frame(root,bg='lightblue')

# Rótulo e entrada para o nome de usuário
label_usuario = tk.Label(telaLogin, text="Usuário:")
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(telaLogin)
entry_usuario.pack(pady=5)
label_usuario.pack()
# Rótulo e entrada para a senha
label_senha = tk.Label(telaLogin, text="Senha:")
label_senha.pack(pady=5)
entry_senha = tk.Entry(telaLogin, show="*")
entry_senha.pack(pady=5)

# Botão de login
botao_login = tk.Button(telaLogin, text="Entrar", command= lambda: verificar_login(root, telaLogin))
botao_login.pack(pady=20)

botao_sair = tk.Button(telaLogin, text="Sair", command=root.destroy)
botao_sair.pack(pady=20)

telaLogin.pack()

# Iniciar a interface gráfica de login
root.mainloop()
