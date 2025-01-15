import tkinter as tk
from tkinter import messagebox
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

    botao_sair = tk.Button(telaVendedor, text="Sair", command= lambda: fecharTela(telaVendedor, telaLogin))
    botao_sair.pack(pady=20)

    telaVendedor.pack()

def telaVenda(root, telaVendedor, idVendedor):
    telaVendedor.pack_forget()
    telaVenda = tk.Frame(root, bg='lightblue')
    
    titulo = tk.Label(telaVenda, text="Tela de venda!", font=("Arial", 14))
    titulo.pack(pady=20)
    
    label_nomeCliente = tk.Label(telaVenda, text="Nome Cliente:")
    label_nomeCliente.pack(pady=5)
    entry_nomeCliente = tk.Entry(telaVenda)
    entry_nomeCliente.pack(pady=5)

    botao_realizarVenda = tk.Button(telaVenda, text="Cadastrar", command=lambda: realizarVenda(idVendedor, entry_user, entry_password))
    botao_realizarVenda.pack(pady=20)

    botao_sair = tk.Button(telaVenda, text="Sair", command= lambda: fecharTela(telaVenda, telaVendedor))
    botao_sair.pack(pady=20)

    telaVenda.pack()
    
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

def realizarVenda(idVendedor, nomeCliente, cpf, endereco, formaPagamento, idProduto, entrada, quantidadeParcelas, quantidade):
    
    cadastro = database.realizarVenda(conexao, idVendedor.get(), nomeCliente.get(), cpf.get(), endereco.get(), formaPagamento.get(), idProduto.get(), entrada.get(), quantidadeParcelas.get(), quantidade.get())
    idVendedor.delete(0, tk.END)
    nomeCliente.delete(0, tk.END)
    cpf.delete(0, tk.END)
    endereco.delete(0, tk.END)
    formaPagamento.delete(0, tk.END)
    idProduto.delete(0, tk.END)
    entrada.delete(0, tk.END)
    quantidadeParcelas.delete(0, tk.END)
    quantidade.delete(0, tk.END)

# Janela de login
root = tk.Tk()
root.geometry("500x500")
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
