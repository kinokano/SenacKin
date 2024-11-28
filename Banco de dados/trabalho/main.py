import tkinter as tk
from tkinter import messagebox
from crud import *
from crud import Database

database = Database()
conexao = database.conectar()
usuarios = database.getUsuarios(conexao)

# Função para verificar o login
def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    
    # Credenciais de exemplo
    for i in usuarios:
       
        if usuario == i[1] and senha == i[2]:
            if usuario == 'admin':
                messagebox.showinfo("Login Bem-sucedido", "Bem-vindo, " + usuario + "!")
                root.destroy() 
                telaAdm()
                # Fecha a tela de login
            else:
                messagebox.showinfo("Login Bem-sucedido", "Bem-vindo, " + usuario + "!")
                root.destroy() 
                telaVendedor()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")

# Função para abrir a tela interna após login bem-sucedido
def telaAdm():
    tela_Adm = tk.Tk()
    tela_Adm.title("Tela Interna")
    tela_Adm.geometry("400x300")

    label_bem_vindo = tk.Label(tela_Adm, text="Bem-vindo à tela interna!", font=("Arial", 14))
    label_bem_vindo.pack(pady=20)

    botao_cadastrar = tk.Button(tela_Adm, text="Cadastrar Vendedor", command=telaCadastrar)
    botao_cadastrar.pack(pady=20)

    botao_sair = tk.Button(tela_Adm, text="Sair", command=tela_Adm.quit)
    botao_sair.pack(pady=20)

    tela_Adm.mainloop()


def telaCadastrar():
    telaCadastrar = tk.Tk()
    telaCadastrar.title("Cadastrar Vendedor")
    telaCadastrar.geometry("400x300")

    label_usuario = tk.Label(telaCadastrar, text="Usuário:")
    label_usuario.pack(pady=5)
    entrada_usuario = tk.Entry(telaCadastrar)
    entrada_usuario.pack(pady=5)

    # Rótulo e entrada para a senha
    label_senha = tk.Label(telaCadastrar, text="Senha:")
    label_senha.pack(pady=5)
    entrada_senha = tk.Entry(telaCadastrar, show="*")
    entrada_senha.pack(pady=5)


    botao_cadastrar = tk.Button(telaCadastrar, text="Cadastrar", command=cadastrar)
    botao_cadastrar.pack(pady=20)

    telaCadastrar.mainloop()

def cadastrar():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    database.cadastrarUsuario(conexao, usuario, senha)


def telaVendedor():
    tela_interna = tk.Tk()
    tela_interna.title("Tela Interna")
    tela_interna.geometry("400x300")

    label_bem_vindo = tk.Label(tela_interna, text="Bem-vindo à tela interna!", font=("Arial", 14))
    label_bem_vindo.pack(pady=20)

    botao_sair = tk.Button(tela_interna, text="Sair", command=tela_interna.quit)
    botao_sair.pack(pady=20)

    tela_interna.mainloop()

# Janela de login
root = tk.Tk()
root.title("Tela de Login")
root.geometry("300x200")

# Rótulo e entrada para o nome de usuário
label_usuario = tk.Label(root, text="Usuário:")
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(root)
entry_usuario.pack(pady=5)

# Rótulo e entrada para a senha
label_senha = tk.Label(root, text="Senha:")
label_senha.pack(pady=5)
entry_senha = tk.Entry(root, show="*")
entry_senha.pack(pady=5)

# Botão de login
botao_login = tk.Button(root, text="Entrar", command=verificar_login)
botao_login.pack(pady=20)

# Iniciar a interface gráfica de login
root.mainloop()
