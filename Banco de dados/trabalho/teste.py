import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

# Criando o Frame
frame = tk.Frame(root, bg='lightcoral', width=200, height=100)
frame.place(relx=0.5, rely=0.5, anchor='center')  # Centraliza o Frame

label = tk.Label(frame, text="Hello World")
label.pack()

root.mainloop()
