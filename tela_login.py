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
janela.geometry("400x400")

label_login = tk.Label(janela, text="Login: ")
label_login.place(x=110, y=140)

campo_login = tk.Entry(janela)
campo_login.place(x=150, y=140)

label_senha = tk.Label(janela, text="Senha: ")
label_senha.place(x=110, y=170)

campo_senha = tk.Entry(janela, show="*")
campo_senha.place(x=150, y=170)

#Chamando uma função na propria pg que esconde a tela atual e executa a função para abrir a outra janela de pedidos
botao_entrar = tk.Button(janela, text="Entrar", command=janela_pedido)
botao_entrar.place(x=150, y=200)

janela.mainloop()