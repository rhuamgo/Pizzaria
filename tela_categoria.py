import tkinter as tk
from tkinter import messagebox
import tela_cardapio_salgado
import tela_cardapio_doce
import tela_cardapio_bebidas
import tela_confirmar_pedido

def abrir_categoria(janela_incial):
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
    janela_categoria.destroy()
    janela_incial.deiconify()
 
 def cardapio_salgado():
      janela_categoria.withdraw()
      tela_cardapio_salgado.abrir_cardapio_salgado(janela_categoria)
 
 def cardapio_doce():
      janela_categoria.withdraw()
      tela_cardapio_doce.abrir_cardapio_doce(janela_categoria)

 def cardapio_bebida():
      janela_categoria.withdraw()
      tela_cardapio_bebidas.abrir_cardapio_bebidas(janela_categoria)

 def confirmarPedido():
     Pizzas_adicionadas = tela_cardapio_salgado.Pizzas_adicionadas
     if Pizzas_adicionadas != []:
         
         print(Pizzas_adicionadas)
         janela_categoria.withdraw()
         tela_confirmar_pedido.confirmar_pedido(janela_categoria,Pizzas_adicionadas)
     else:
          messagebox.showinfo("ERRO",'Selecione ao menos um item antes de Continuar')


 janela_categoria = tk.Toplevel(janela_incial)
 janela_categoria.title("Categorias")
 janela_categoria.configure(background= '#eb4764')
 janela_categoria.resizable(False, False)
 janela_categoria.iconbitmap("img\\icon.ico")

 largura_janela = 600
 altura_janela = 250
 centralizando_Janela(janela_categoria, largura_janela, altura_janela)



 #Criando frame da tela de categoria
 frame1=tk.Frame(janela_categoria, bd = 4, bg = '#c95b6e',
                     highlightbackground= '#c52f49', highlightthickness= 3 )
 frame1.place(relx=0.02, rely=0.02, relwidth= 0.96, relheight = 0.96)

 label = tk.Label(frame1, text="Escolha uma Categoria", bg= '#c52f49', fg='white'
                    , font = ('verdana', 8, 'bold'))
 label.pack(padx=10, pady=10)

 img_salgada = tk.PhotoImage(file="img\\pizza_salgada.png")
 janela_categoria.img_salgada = img_salgada

 img_doce = tk.PhotoImage(file="img\\pizza_doce.png")
 janela_categoria.img_doce = img_doce

 img_bebidas = tk.PhotoImage(file="img\\bebidas.png")
 janela_categoria.img_bebidas = img_bebidas
 
 

 botao_entrega = tk.Button(frame1, text="Pizzas Salgadas", image=janela_categoria.img_salgada, compound="top",
                          bd=3, bg="#d72e4c", fg="black", font=("verdana", 8, "bold"), command=cardapio_salgado)
 botao_entrega.place(x=50, y=65)

 botao_entrega = tk.Button(frame1, text="Pizzas Doces", image=janela_categoria.img_doce, compound="top",
                          bd=3, bg="#d72e4c", fg="black", font=("verdana", 8, "bold"), command=cardapio_doce)
 botao_entrega.place(x=200, y=65)

 botao_entrega = tk.Button(frame1, text="Bebidas", image=janela_categoria.img_bebidas, compound="top",
                          bd=3, bg="#d72e4c", fg="black", font=("verdana", 8, "bold"), command=cardapio_bebida)
 botao_entrega.place(x=350, y=65)

 botao_confirmarPedido = tk.Button(frame1, text="Confirmar Pedido", bd=2, bg = '#d72e4c' , fg = 'white' 
                            , font = ('verdana', 8, 'bold'), command=confirmarPedido) 
 botao_confirmarPedido.place(x=250, y=200)

 #BOTÃO PARA RETORNAR A TELA DE PEDIDOS
 botao_voltar = tk.Button(frame1, text="Voltar", bd=2, bg = '#d72e4c' , fg = 'white' 
                            , font = ('verdana', 8, 'bold'), command=voltar)
 botao_voltar.place(x=150, y=200)

 janela_categoria.mainloop()
