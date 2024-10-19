import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tela_cardapio_salgado
import tela_TipoPedido


def confirmar_pedido(janela,pizzas, janelaIncial):
 

    def centralizando_Janela(janela, largura, altura):
        #Pega o tamanho da tela em pixel 
        largura_tela = janela.winfo_screenwidth() #essa função pergunta para SO do monitor e retorna o valor em largura e altura
        altura_tela = janela.winfo_screenheight()
        #Dide o tamanho e a largura da tela por 2 e subtrais com a divisão dos mesmo valores da janela
        x = (largura_tela // 2) - (largura // 2)
        y = (altura_tela // 2) - (altura // 2)
        #passa o tamanho da tela posicionando ela no eixo x e y
        janela.geometry(f"{largura}x{altura}+{x}+{y}")



  #Função para VOltar para categorias
    def cancelar():
        tela_cardapio_salgado.Pizzas_adicionadas =[]
        janela_confirmar.destroy()
        janela.deiconify()

    def voltar():
        
        janela_confirmar.destroy()
        janela.deiconify()

    def finalizar_pedido():
        itens = tw.get_children()
        valores_tw = []
        for item in itens:
            valores = tw.item(item, "values")
            valores_tw.append(valores)
        if valores_tw == []:
            messagebox.showerror("ERRO", "Adicione ao menos um item")
            janela_confirmar.destroy()
            janela.deiconify()
            tela_cardapio_salgado.Pizzas_adicionadas = []
            
        janela_confirmar.withdraw()
        tela_TipoPedido.abrir_TipoPedido(janela_confirmar, janelaIncial)

    def deletar():
        try:
            #Primeiro eu pego o primeiro item selecionado, depois eu guardo os valores em "valor" ai eu subtraio a qtd e guardo
            #o resultado em "valor1" uso o metodo "item" e atualizo a linha selecionada com o resultado de "valor1"
            itemSelecionado = tw.selection()[0]
            valor =tw.item(itemSelecionado, "values")
            
            valor1 = int(valor[2]) - 1
            tw.item(itemSelecionado, values=(valor[0],valor[1],valor1))   
            #caso o numero for igual a zero ele deleta a linha selecionada          
            if valor1 == 0:
                tw.delete(itemSelecionado)

            #Recalcula o valor total das pizzas e atualiza
            itens = tw.get_children()
            valores_tw = []
            for item in itens:
               valores = tw.item(item, "values")
               valores_tw.append(valores)   
            quantidadeTotal = 0

            for (s,t,q) in valores_tw:
        
                for (trad, doce, bebida) in zip(pizzaSalgadaTrad,pizzDoce,bebidas):
            
                    if s == trad:
                        if t == 'Grande':
                            quantidadeTotal += 42 * int(q)
            
                        elif t == 'Media':
                            quantidadeTotal += 32 * int(q)
            
                        elif t == 'Broto':
                            quantidadeTotal += 18 * int(q)

                    elif s == doce:
                        if t == 'Grande':
                            quantidadeTotal += 38 * int(q)
            
                        elif t == 'Media':
                            quantidadeTotal += 26 * int(q)
            
                        elif t == 'Broto':
                            quantidadeTotal += 18 * int(q)

                    elif s == bebida :
                        if t == '1 LT':
                            quantidadeTotal += 10 * int(q)
            
                        elif t == '2 LT':
                            quantidadeTotal += 15 * int(q)
            
                        elif t == 'LATA':
                            quantidadeTotal += 6 * int(q)
            

            total.configure(text=f'Total: R${quantidadeTotal},00',bd=4, bg= '#c52f49', fg='white'
                    , font = ("Arial Black", 14, 'bold'))
        except:
            messagebox.showinfo('ERRO', "Selecione a Pizza que deseja Deletar!")
  
       
    # Criando a janela principal
    janela_confirmar = tk.Toplevel(janela)
    
    janela_confirmar.title("Confirmar Pedido")
    janela_confirmar.configure(background='#eb4764')
    janela_confirmar.resizable(False, False)
    janela_confirmar.iconbitmap("img\\icon.ico")

    largura_janela = 650
    altura_janela = 600
    centralizando_Janela(janela_confirmar, largura_janela, altura_janela)



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
            if t == 'Grande':
                quantidadeTotal += 42 * int(q)
            
            elif t == 'Media':
                quantidadeTotal += 32 * int(q)
            
            elif t == 'Broto':
                quantidadeTotal += 18 * int(q)

         elif s == doce:
            if t == 'Grande':
                quantidadeTotal += 38 * int(q)
            
            elif t == 'Media':
                quantidadeTotal += 26 * int(q)
            
            elif t == 'Broto':
                quantidadeTotal += 18 * int(q)

        
         elif s == bebida :
            if t == '1 LT':
                quantidadeTotal += 10 * int(q)
            
            elif t == '2 LT':
                quantidadeTotal += 15 * int(q)
            
            elif t == 'LATA':
                quantidadeTotal += 6 * int(q)
            

    total =tk.Label(janela_confirmar, text=f'Total: R${quantidadeTotal},00',bd=4, bg= '#c52f49', fg='white'
                    , font = ("Arial Black", 14, 'bold'))
    total.place(x=250, y=400)



    #Botão Cancelar
    botap_cancelar = tk.Button(janela_confirmar, text="Cancelar", bd=2, bg = '#c52f49' , fg = 'white' 
                            , font = ('verdana', 8, 'bold'), command=cancelar)
    botap_cancelar.place(x=200, y=520)

    botap_deletar = tk.Button(janela_confirmar, text="Deletar", bd=2, bg = '#c52f49' , fg = 'white' 
                            , font = ('verdana', 8, 'bold'), command=deletar)
    botap_deletar.place(x=320, y=520)
    

    botap_voltar = tk.Button(janela_confirmar, text="Voltar", bd=2, bg = '#c52f49' , fg = 'white' 
                            , font = ('verdana', 8, 'bold'), command=voltar)
    botap_voltar.place(x=100, y=520)


    botap_finalizar = tk.Button(janela_confirmar, text="Finalizar Pedido", bd=2, bg = '#c52f49' , fg = 'white' 
                            , font = ('verdana', 8, 'bold'), command=finalizar_pedido)
    botap_finalizar.place(x=440, y=520)


    janela_confirmar.mainloop()
