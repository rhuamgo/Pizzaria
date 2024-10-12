import tkinter as tk
from tkinter import messagebox
import tela_pedido

def janela_pedido():
    user = str(campo_login.get())
    password = str(campo_senha.get())

    if user == 'admin' and password == 'admin':
    #Escondendo tela de login
        janela.withdraw()  
        tela_pedido.abrir_janela() 
    else:
         messagebox.showerror("Erro", "Usuario ou Senha incorreto!")


janela = tk.Tk()
janela.title("Login")
janela.geometry("300x200")

label_login = tk.Label(janela, text="Login: ")
label_login.grid(row=0, column=0, padx=10, pady=10, sticky="e")

campo_login = tk.Entry(janela)
campo_login.grid(row=0, column=1, padx=10, pady=10)

label_senha = tk.Label(janela, text="Senha: ")
label_senha.grid(row=1, column=0, padx=10, pady=10, sticky="e")

campo_senha = tk.Entry(janela, show="*")
campo_senha.grid(row=1, column=1, padx=10, pady=10)

#Chamando uma função na propria pg que esconde a tela atual e executa a função para abrir a outra janela de pedidos
botao_entrar = tk.Button(janela, text="Entrar", command=janela_pedido)
botao_entrar.grid(row=2, column=0, columnspan=2, pady=10)


janela.mainloop()