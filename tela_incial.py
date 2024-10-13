import tkinter as tk
from tkinter import PhotoImage, messagebox

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
banner_logo = tk.PhotoImage(file="PIZZARIA\\img\\banner2.png")

#Ajustando Frame ao tamanho da imagem
frame_logo.config(width=banner_logo.width(), height=banner_logo.height())

#Colcoando a Img dentro do Frame
label_banner = tk.Label(frame_logo, image=banner_logo)
label_banner.pack(fill="x", expand=1)

frame_principal = tk.Frame(janela_incial)
frame_principal.pack(fill="both", expand=1)

img_tela = tk.PhotoImage(file="PIZZARIA\\img\\tela.png")

label_tela = tk.Label(frame_principal, image=img_tela)
label_tela.pack(fill="both", expand=True)

janela_incial.mainloop()