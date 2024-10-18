import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tela_cardapio_salgado


def confirmar_pedido(janela,pizzas):

  #Função para VOltar para categorias
    def voltar():
        tela_cardapio_salgado.Pizzas_adicionadas =[]
        janela_confirmar.destroy()
        janela.deiconify()
    def deletar():
        try:
            itemSelecionado = tw.selection()[0]
            tw.delete(itemSelecionado)



            #Recalcula o valor total das pizzas e atualiza
            itens = tw.get_children()
            valores_tw = []
            for item in itens:
               valores = tw.item(item, "values")
               valores_tw.append(valores)   
            quantidadeTotal = 0

            for (s,t,q) in valores_tw:
       
              for (trad, esp, doce, bebida) in zip(pizzaSalgadaTrad,pizzDoce,bebidas):
            
               if s == trad:
                 quantidadeTotal += 25 * int(q)

               elif s == esp:
                quantidadeTotal += 42 * int(q)

               elif s == doce:

                quantidadeTotal += 30 * int(q)
         
               elif s == bebida :
                quantidadeTotal += 12 * int(q)
            total.configure(text=f'R${quantidadeTotal}')
        except:
            messagebox.showinfo('ERRO', "Selecione a Pizza que deseja Deletar!")
  
       
    # Criando a janela principal
    janela_confirmar = tk.Toplevel(janela)
    
    janela_confirmar.title("Confirmar Pedido")
    janela_confirmar.geometry("650x600")
    janela_confirmar.configure(background='#eb4764')
    janela_confirmar.resizable(False, False)
    janela_confirmar.iconbitmap("img\\icon.ico")

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

    #Botão Cancelar
    botap_cancelar = tk.Button(janela_confirmar, text="Cancelar", bd=2, bg = '#c52f49' , fg = 'white' 
                            , font = ('verdana', 8, 'bold'), command=voltar)
    botap_cancelar.place(x=100, y=520)

    botap_deletar = tk.Button(janela_confirmar, text="Deletar", bd=2, bg = '#c52f49' , fg = 'white' 
                            , font = ('verdana', 8, 'bold'), command=deletar)
    botap_deletar.place(x=200, y=520)
    

    #Pega as informações do Treeview, transforma em valores e guarda no array "valores_tw"
    itens = tw.get_children()
    valores_tw = []
    quantidadeTotal = 0
    for item in itens:
        valores = tw.item(item, "values")
        valores_tw.append(valores)
       
    pizzaSalgadaTrad = ['CALABRESA','TRADICIONAL','LA CASA', 'FRANGO', 'LOMBO', 'PALMITO', 'PEPERONE']
    
    
    pizzDoce = ['M&Ms','BANANA SHOW','BRIGADEIRO', 'OREO', 'OURO BRANCO', 'PRESTIGIO', 'GOIABADA']

    bebidas = ['COCA-COLA','GUARANA','FANTA UVA', 'PEPSI', 'SODA', 'CHÁ', 'LIMONADA']

    #Pega os valores da rotina de cima e as listas de cima, usa o zip para pegar todos os Arrays de cima com os sabores e itens 
    for (s,t,q) in valores_tw:
        
        for (trad, doce, bebida) in zip(pizzaSalgadaTrad,pizzDoce,bebidas):
            
         if s == trad:
            quantidadeTotal += 25 * int(q)

         elif s == doce:

            quantidadeTotal += 30 * int(q)
        
         elif s == bebida :
            quantidadeTotal += 12 * int(q)

    total =tk.Label(janela_confirmar, text=f'R${quantidadeTotal}',bd=4, bg= '#c52f49', fg='white'
                    , font = ("Arial Black", 14, 'bold'))
    total.place(x=250, y=400)


    janela_confirmar.mainloop()
