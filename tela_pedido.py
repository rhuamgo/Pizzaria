import tkinter as tk
from tkinter import PhotoImage


def abrir_pedido(janela_incial):

 def centralizando_Janela(janela, largura, altura):
    #Pega o tamanho da tela em pixel 
    largura_tela = janela.winfo_screenwidth() #essa função pergunta para SO do monitor e retorna o valor em largura e altura
    altura_tela = janela.winfo_screenheight()
    #Dide o tamanho e a largura da tela por 2 e subtrais com a divisão dos mesmo valores da janela
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    #passa o tamanho da tela posicionando ela no eixo x e y
    janela.geometry(f"{largura}x{altura}+{x}+{y}")



 def voltar():
        janela_pedido.destroy()
        janela_incial.deiconify()

 janela_pedido = tk.Toplevel(janela_incial)  
 janela_pedido.title("Pedido")
 janela_pedido.geometry("400x450")
 janela_pedido.configure(background= '#eb4764')
 janela_pedido.resizable(False, False)
 janela_pedido.iconbitmap("img\\icon.ico")

 largura_janela = 450
 altura_janela = 400
 centralizando_Janela(janela_pedido, largura_janela, altura_janela)



   
 #Criando frame da tela de pedidos
 frame1=tk.Frame(janela_pedido, bd = 4, bg = '#c95b6e',
                     highlightbackground= '#c52f49', highlightthickness= 3 )
 frame1.place(relx=0.02, rely=0.02, relwidth= 0.96, relheight = 0.96)

 label = tk.Label(frame1, text="Selecione o Tipo do Pedido!", bg= '#c52f49', fg='white'
                    , font = ('verdana', 8, 'bold'))
 label.pack(padx=10, pady=10)

 #Guardando as imagens de retirada e entrega 
 img_entrega = tk.PhotoImage(file="img\\img_entrega.png")
 img_retire = tk.PhotoImage(file="img\\img_retire.png")

 #Para evitar com que a img seja destruida quando chamamos a fumçãao vamos ligar ela ao atributo da janela criando assim uma referencia a img (transformamos em obj)
 janela_pedido.img_entrega = img_entrega
 janela_pedido.img_retire= img_retire

 botao_entrega = tk.Button(frame1, text="Entrega", image=janela_pedido.img_entrega, compound="top",
                          bd=3, bg="#d72e4c", fg="black", font=("verdana", 8, "bold"))
 botao_entrega.pack(padx=10, pady=10)


 botao_entrega = tk.Button(frame1, text="Retirada", image=janela_pedido.img_retire, compound="top",
                          bd=3, bg="#d72e4c", fg="black", font=("verdana", 8, "bold"))
 botao_entrega.pack(padx=10, pady=10)

    
 botao_voltar = tk.Button(frame1, text="Voltar", bd=2, bg = '#d72e4c' , fg = 'white' 
                            , font = ('verdana', 8, 'bold'), command=voltar)
 botao_voltar.pack(padx=10, pady=10)

 