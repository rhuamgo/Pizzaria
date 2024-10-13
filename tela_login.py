
import tkinter as tk
from tkinter import messagebox
import tela_pedido

def janela_pedido():
    user = str(campo_login.get())
    password = str(campo_senha.get())

    if user == 'admin' and password == 'admin':
        #Fechando Janela de Login e abrindo Janela de pedido
        janela.destroy()
        tela_pedido.abrir_janela() 
      
    else:
         messagebox.showerror("Erro", "Usuário ou senha incorretos!")

#Configurando e Estilizando Janela de Login
janela = tk.Tk()
janela.title("Login")
janela.geometry("300x200")
janela.configure(background= '#1e3743')
janela.resizable(True, True)
janela.maxsize(width= 350, height = 250)
janela.minsize(width = 200, height = 200)
janela.iconbitmap("PIZZARIA\img\icon.ico")

label_login = tk.Label(janela, text="LOGIN", bd=2, bg = '#107DB2' , fg = 'white' 
                         , font = ('verdana', 8, 'bold'))
label_login.pack(padx=10, pady=10)

campo_login = tk.Entry(janela)
campo_login.pack(padx=10, pady=10)

campo_senha = tk.Entry(janela, show="*")
campo_senha.pack(padx=10, pady=10)

#Chamando uma função na propria pg que esconde a tela atual e executa a função para abrir a outra janela de pedidos
botao_entrar = tk.Button(janela, text="Entrar", bd=2, bg = '#107DB2' , fg = 'white' 
                         , font = ('verdana', 8, 'bold') , command=janela_pedido)
botao_entrar.pack(padx=10, pady=10)


janela.mainloop()