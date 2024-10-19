
import tkinter as tk
from tkinter import END, messagebox



def abrir_login(janela_incial):
 #Função para fazedr a janela inciial iniicar no meio
 def centralizando_Janela(janela, largura, altura):
    #Pega o tamanho da tela em pixel 
    largura_tela = janela.winfo_screenwidth() #essa função pergunta para SO do monitor e retorna o valor em largura e altura
    altura_tela = janela.winfo_screenheight()
    #Dide o tamanho e a largura da tela por 2 e subtrais com a divisão dos mesmo valores da janela
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    #passa o tamanho da tela posicionando ela no eixo x e y
    janela.geometry(f"{largura}x{altura}+{x}+{y}")
  
 def verificar_usuario():
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

 janela.resizable(False, False)

 janela.configure(background= '#eb4764')
 janela.iconbitmap("img\\icon.ico")


 largura_janela = 450
 altura_janela = 500
 centralizando_Janela(janela, largura_janela, altura_janela)


 janela_frame=tk.Frame(janela, bd = 3, bg = '#c95b6e',
                     highlightbackground= '#c52f49', highlightthickness= 3 )
 janela_frame.place(relx=0.02, rely=0.02, relwidth= 0.96, relheight = 0.96)

 label_login = tk.Label(janela_frame, text="LOGIN", bd=2, bg = '#d72e4c' , fg = 'white' 
                            , font = ('verdana', 10, 'bold'))
 label_login.place(x=190, y=140)

 campo_login = tk.Entry(janela_frame, width=20,font=('Arial', 10) )
 campo_login.place(x=140, y=170)


 campo_senha = tk.Entry(janela_frame,width=20, show="*", font=('Arial', 10))
 campo_senha.place(x=140, y=200)


   
 botao_entrar = tk.Button(janela_frame, text="Entrar", bd=2, bg = '#d72e4c' , fg = 'white' 
                            , font = ('verdana', 8, 'bold'),width=10 , command=verificar_usuario)
 botao_entrar.place(x=170, y=245)
 
