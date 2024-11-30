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
       
        if usuario == i[1] and senha == i[2]:
            if usuario == 'admin':
                messagebox.showinfo("Login Bem-sucedido", "Bem-vindo, " + usuario + "!")
                telaAdm(root, telaLogin)
                break
                # Fecha a tela de login
            else:
                messagebox.showinfo("Login Bem-sucedido", "Bem-vindo, " + usuario + "!")
                telaVendedor()
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

def telaVendedor(root, telaLogin):
    telaVendedor = tk.Frame(root,bg='lightblue')
    

    titulo = tk.Label(telaVendedor, text="Tela do Vendedor!", font=("Arial", 14))
    titulo.pack(pady=20)


    botao_sair = tk.Button(telaVendedor, text="Sair", command=telaVendedor.destroy)
    botao_sair.pack(pady=20)

    telaVendedor.pack()


def telaCadastrar(root, telaAdm):
    telaAdm.pack_forget()
    telaCadastrar = tk.Frame(root,bg='lightblue')
    
    titulo = tk.Label(telaCadastrar, text="Tela de Cadastro!", font=("Arial", 14))
    titulo.pack(pady=20)
    
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

    botao_sair = tk.Button(telaCadastrar, text="Sair", command= lambda: fecharTela(telaCadastrar, telaAdm))
    botao_sair.pack(pady=20)


    telaCadastrar.pack()

def cadastrar(a, b):
   
    cadastro = database.cadastrarUsuario(conexao, a.get(), b.get())
    a.delete(0, tk.END)
    b.delete(0, tk.END)

    


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
