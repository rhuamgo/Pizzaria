import tkinter as tk
from tkinter import ttk


def confirmar_pedido(janela_salgado,pizzas):

    # Criando a janela principal
    janela_confirmar = tk.Toplevel(janela_salgado)
    janela_confirmar.title("Confirmar Pedido")
    janela_confirmar.geometry("650x600")
    janela_confirmar.configure(background='#eb4764')
    janela_confirmar.resizable(False, False)
    janela_confirmar.iconbitmap("PIZZARIA\\img\\icon.ico")

    lista = pizzas
    
    # Definindo o estilo personalizado para o Treeview
    estilo = ttk.Style()
    estilo.theme_use('default') 
    estilo.configure("Treeview",
                     background="#c95b6e",
                     foreground="black",
                     rowheight=25,
                     fieldbackground="#c95b6e")

    estilo.configure("Treeview.Heading",
                     background="#d72e4c",
                     foreground="white",
                     font=('verdana', 10, 'bold'))
    
    titulo_label = tk.Label(janela_confirmar, text="Itens Adicionados", bg= '#c52f49', fg='white'
                    , font = ('verdana', 14, "bold"))
    titulo_label.pack(padx=20, pady=20)

    # Criando o Treeview
    tw = ttk.Treeview(janela_confirmar, columns=('Sabor', 'Tamanho', 'Quantidade'), show='headings')
    
    # Configurando as colunas
    tw.column('Sabor', minwidth=0, width=110)
    tw.column('Tamanho', minwidth=0, width=70, anchor='center')
    tw.column('Quantidade', minwidth=0, width=90, anchor='center')
    
    # Definindo os títulos das colunas
    tw.heading('Sabor', text='Sabores')
    tw.heading('Tamanho', text='Tamanho')
    tw.heading('Quantidade', text='Quantidade')
    tw.pack(padx=20, pady=20)
    
    # Inserindo os valores no Treeview
    for (sabor, tamanho, quantidade) in lista:
        tw.insert("", "end", values=(sabor, tamanho, quantidade))


