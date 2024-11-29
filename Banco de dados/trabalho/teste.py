import tkinter as tk
from tkinter import ttk

def adicionar_dado():
    # Captura os dados da Entry
    nome = entry_nome.get()
    idade = entry_idade.get()
    
    # Adiciona os dados na tabela
    treeview.insert("", "end", values=(nome, idade))
    
    # Limpa os campos de entrada após a inserção
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)

# Cria a janela principal
root = tk.Tk()
root.title("Exemplo de Tabela Tkinter")

# Cria os campos de entrada (Entry)
label_nome = tk.Label(root, text="Nome:")
label_nome.grid(row=0, column=0, padx=10, pady=10)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

label_idade = tk.Label(root, text="Idade:")
label_idade.grid(row=1, column=0, padx=10, pady=10)
entry_idade = tk.Entry(root)
entry_idade.grid(row=1, column=1, padx=10, pady=10)

# Botão para adicionar dados
botao_adicionar = tk.Button(root, text="Adicionar", command=adicionar_dado)
botao_adicionar.grid(row=2, column=0, columnspan=2, pady=10)

# Cria a tabela (Treeview)
colunas = ("Nome", "Idade")
treeview = ttk.Treeview(root, columns=colunas, show="headings")
treeview.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Configura os cabeçalhos da tabela
treeview.heading("Nome", text="Nome")
treeview.heading("Idade", text="Idade")

# Inicia o loop da interface gráfica
root.mainloop()
