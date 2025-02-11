import tkinter as tk
import sqlite3
import csv
from crud import *
from crud import Database

# Função para gerar o CSV a partir da consulta SQL
def gerar_csv():
    # Conectar ao banco de dados SQLite
    database = Database()
    conexao = database.conectar()
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

        # Mensagem de sucesso
        label_status.config(text="Relatório CSV gerado com sucesso!", fg="green")
    else:
        label_status.config(text="Nenhum dado encontrado.", fg="red")

# Criando a janela principal
root = tk.Tk()
root.title("Gerar Relatório CSV")
root.geometry("300x200")

# Label para mostrar status
label_status = tk.Label(root, text="", font=("Arial", 10))
label_status.pack(pady=20)

# Botão para gerar o relatório CSV
botao_gerar_csv = tk.Button(root, text="Gerar Relatório CSV", command=gerar_csv)
botao_gerar_csv.pack(pady=10)

# Rodando a aplicação
root.mainloop()