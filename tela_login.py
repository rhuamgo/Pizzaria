
import tkinter as tk
from tkinter import messagebox



def abrir_login(janela_incial):
 
    
 def janela_pedido():
        user = str(campo_login.get())
        password = str(campo_senha.get())

        if user == 'admin' and password == 'admin':
           
            janela.destroy()
            janela_incial.deiconify()
            
        
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")

 #Configurando e Estilizando Janela de Login
 janela = tk.Toplevel(janela_incial)
 janela.title("Login")
 janela.geometry("300x350")
 janela.resizable(True, True)
 janela.maxsize(width= 350, height = 250)
 janela.minsize(width = 200, height = 200)
 janela.configure(background= '#eb4764')
 janela.iconbitmap("img\\icon.ico")


 janela_frame=tk.Frame(janela, bd = 3, bg = '#c95b6e',
                     highlightbackground= '#c52f49', highlightthickness= 3 )
 janela_frame.place(relx=0.02, rely=0.02, relwidth= 0.96, relheight = 0.96)

 label_login = tk.Label(janela_frame, text="LOGIN", bd=2, bg = '#d72e4c' , fg = 'white' 
                            , font = ('verdana', 8, 'bold'))
 label_login.pack(padx=10, pady=10)

 campo_login = tk.Entry(janela_frame)
 campo_login.pack(padx=10, pady=10)

 campo_senha = tk.Entry(janela_frame, show="*")
 campo_senha.pack(padx=10)

   
 botao_entrar = tk.Button(janela_frame, text="Entrar", bd=2, bg = '#d72e4c' , fg = 'white' 
                            , font = ('verdana', 8, 'bold') , command=janela_pedido)
 botao_entrar.pack(padx=10, pady=10)
 
