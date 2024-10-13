import tkinter as tk
from tkinter import PhotoImage


def abrir_pedido(janela_incial):
 def voltar():
        janela_pedido.destroy()
        janela_incial.deiconify()

 janela_pedido = tk.Toplevel(janela_incial)  
 janela_pedido.title("Pedido")
 janela_pedido.geometry("400x450")
 janela_pedido.configure(background= '#eb4764')
 janela_pedido.resizable(False, False)
 janela_pedido.iconbitmap("PIZZARIA\\img\\icon.ico")

   
 #Criando frame da tela de pedidos
 frame1=tk.Frame(janela_pedido, bd = 4, bg = '#c95b6e',
                     highlightbackground= '#c52f49', highlightthickness= 3 )
 frame1.place(relx=0.02, rely=0.02, relwidth= 0.96, relheight = 0.96)

 label = tk.Label(frame1, text="Selecione o Tipo do Pedido!", bg= '#c52f49', fg='white'
                    , font = ('verdana', 8, 'bold'))
 label.pack(padx=10, pady=10)

 #Guardando as imagens de retirada e entrega 
 img_entrega = tk.PhotoImage(file="PIZZARIA\\img\\img_entrega.png")
 img_retire = tk.PhotoImage(file="PIZZARIA\\img\\img_retire.png")

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

 