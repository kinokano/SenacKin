import tkinter as tk
from tkinter import messagebox
from crud import *
from crud import Database

database = Database()
conexao = database.conectar()



# Função para verificar o login
def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    usuarios = database.getUsuarios(conexao)
    # Credenciais de exemplo
    for i in usuarios:
       
        if usuario == i[1] and senha == i[2]:
            if usuario == 'admin':
                messagebox.showinfo("Login Bem-sucedido", "Bem-vindo, " + usuario + "!")
                
                telaAdm()
                break
                # Fecha a tela de login
            else:
                messagebox.showinfo("Login Bem-sucedido", "Bem-vindo, " + usuario + "!")
                telaVendedor()
                break
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos!")
            

# Função para abrir a tela interna após login bem-sucedido
def telaAdm():
    tela_Adm = tk.Tk()
    tela_Adm.title("Tela Interna")
    tela_Adm.geometry("400x300")

    label_bem_vindo = tk.Label(tela_Adm, text="Bem-vindo à tela do Administrador!", font=("Arial", 14))
    label_bem_vindo.pack(pady=20)

    botao_cadastrar = tk.Button(tela_Adm, text="Cadastrar Vendedor", command=telaCadastrar)
    botao_cadastrar.pack(pady=20)

    botao_sair = tk.Button(tela_Adm, text="Sair", command=tela_Adm.destroy)
    botao_sair.pack(pady=20)

    tela_Adm.mainloop()

def telaVendedor():
    telaVendedor = tk.Tk()
    telaVendedor.title("Tela do Vendedor")
    telaVendedor.geometry("400x300")

    label_bem_vindo = tk.Label(telaVendedor, text="Bem-vindo à tela do Vendedor!", font=("Arial", 14))
    label_bem_vindo.pack(pady=20)


    botao_sair = tk.Button(telaVendedor, text="Sair", command=telaVendedor.destroy)
    botao_sair.pack(pady=20)

    telaVendedor.mainloop()


def telaCadastrar():
    telaCadastrar = tk.Tk()
    telaCadastrar.title("Cadastrar Vendedor")
    telaCadastrar.geometry("400x300")

    label_user = tk.Label(telaCadastrar, text="Usuário:")
    label_user.pack(pady=5)
    entry_user = tk.Entry(telaCadastrar)
    entry_user.pack(pady=5)

    # Rótulo e entrada para a senha
    label_password = tk.Label(telaCadastrar, text="Senha:")
    label_password.pack(pady=5)
    entry_password = tk.Entry(telaCadastrar, show="*")
    entry_password.pack(pady=5)
    botao_cadastrar = tk.Button(telaCadastrar, text="Cadastrar", command=lambda: cadastrar(entry_user, entry_password))
    botao_cadastrar.pack(pady=20)

    botao_sair = tk.Button(telaCadastrar, text="Sair", command=telaCadastrar.destroy)
    botao_sair.pack(pady=20)


    telaCadastrar.mainloop()

def cadastrar(a, b):
   
    cadastro = database.cadastrarUsuario(conexao, a.get(), b.get())
    a.delete(0, tk.END)
    b.delete(0, tk.END)

    


# Janela de login
root = tk.Tk()
root.title("Tela de Login")
root.geometry("300x300")

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

botao_sair = tk.Button(root, text="Sair", command=root.destroy)
botao_sair.pack(pady=20)
# Iniciar a interface gráfica de login
root.mainloop()
