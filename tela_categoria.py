import tkinter as tk

def abrir_categoria(janela_incial):
 def voltar():
    janela_categoria.destroy()
    janela_incial.deiconify()
 
 janela_categoria = tk.Toplevel(janela_incial)
 janela_categoria.title("Categorias")
 janela_categoria.geometry("600x250")
 janela_categoria.configure(background= '#eb4764')
 janela_categoria.resizable(False, False)
 janela_categoria.iconbitmap("PIZZARIA\\img\\icon.ico")

 #Criando frame da tela de categoria
 frame1=tk.Frame(janela_categoria, bd = 4, bg = '#c95b6e',
                     highlightbackground= '#c52f49', highlightthickness= 3 )
 frame1.place(relx=0.02, rely=0.02, relwidth= 0.96, relheight = 0.96)

 label = tk.Label(frame1, text="Escolha uma Categoria", bg= '#c52f49', fg='white'
                    , font = ('verdana', 8, 'bold'))
 label.pack(padx=10, pady=10)

 img_salgada = tk.PhotoImage(file="PIZZARIA\\img\\pizza_salgada.png")
 janela_categoria.img_salgada = img_salgada

 img_doce = tk.PhotoImage(file="PIZZARIA\\img\\pizza_doce.png")
 janela_categoria.img_doce = img_doce

 img_bebidas = tk.PhotoImage(file="PIZZARIA\\img\\bebidas.png")
 janela_categoria.img_bebidas = img_bebidas
 
 

 botao_entrega = tk.Button(frame1, text="Pizzas Salgadas", image=janela_categoria.img_salgada, compound="top",
                          bd=3, bg="#d72e4c", fg="black", font=("verdana", 8, "bold"))
 botao_entrega.place(x=50, y=65)

 botao_entrega = tk.Button(frame1, text="Pizzas Doces", image=janela_categoria.img_doce, compound="top",
                          bd=3, bg="#d72e4c", fg="black", font=("verdana", 8, "bold"))
 botao_entrega.place(x=200, y=65)

 botao_entrega = tk.Button(frame1, text="Bebidas", image=janela_categoria.img_bebidas, compound="top",
                          bd=3, bg="#d72e4c", fg="black", font=("verdana", 8, "bold"))
 botao_entrega.place(x=350, y=65)


 #BOTÃO PARA RETORNAR A TELA DE PEDIDOS
 botao_voltar = tk.Button(frame1, text="Voltar", bd=2, bg = '#d72e4c' , fg = 'white' 
                            , font = ('verdana', 8, 'bold'), command=voltar)
 botao_voltar.place(x=250, y=200)

 janela_categoria.mainloop()
