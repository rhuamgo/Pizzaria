import tkinter as tk
from tkinter import PhotoImage, messagebox
import tela_login
import tela_pedido

#Função que chama o modulo login esconde o botão "Entrar", mostra o botão "Pedido" e escode a janela principal
def abrir_login():
    botao_login.place_forget()
    botao_pedido.place(x=310, y=123)
    janela_incial.withdraw()
    tela_login.abrir_login(janela_incial)

#Função que chama modulo pedido e esconde tela principal
def abrir_pedido():
    janela_incial.withdraw()
    tela_pedido.abrir_pedido(janela_incial)

#Configurando janela 
janela_incial = tk.Tk()
janela_incial.title("Home")
janela_incial.geometry("450x500")
janela_incial.configure(background= '#1e3743')
janela_incial.resizable(False, False)
janela_incial.iconbitmap("PIZZARIA\\img\\icon.ico")

#Criando Frame e Impedindo que ele se ajuste automaticamente (estava ficando espaço em branco)
frame_logo = tk.Frame(janela_incial)
frame_logo.pack(side="top", fill="x")
frame_logo.pack_propagate(False)

#Guardando Img do Banner na Variavel
banner_logo = tk.PhotoImage(file="PIZZARIA\\img\\banner.png")

#Ajustando Frame ao tamanho da imagem
frame_logo.config(width=banner_logo.width(), height=banner_logo.height())

#Colcando a Img dentro do Frame
label_banner = tk.Label(frame_logo, image=banner_logo)
label_banner.pack(fill="x", expand=1)

#Criando frame para tela principal que ocupa todo espaço restante
frame_principal = tk.Frame(janela_incial)
frame_principal.pack(fill="both", expand=1)

#Guardando Img da tela inicial
img_tela = tk.PhotoImage(file="PIZZARIA\\img\\tela.png")

#Colocando img dentro do frame da tela inicial
label_tela = tk.Label(frame_principal, image=img_tela)
label_tela.pack(fill="both", expand=True)


botao_login = tk.Button(frame_logo, text="Entrar", bd=2, bg = '#d72e4c', fg='white'
                        , font = ('verdana', 8, 'bold'), command=abrir_login)
botao_login.place(x=250, y=123)

#Inicia escondido e aparece executa a função abrir_login
botao_pedido = tk.Button(frame_logo, text="Pedido", bd=2, bg = '#d72e4c', fg='white'
                        , font = ('verdana', 8, 'bold'), command=abrir_pedido)
botao_pedido.place_forget()


botao_info = tk.Button(frame_logo, text="Conato", bg = '#d72e4c', fg='white'
                        , font = ('verdana', 8, 'bold'))
botao_info.place(x=375, y=123)


janela_incial.mainloop()

