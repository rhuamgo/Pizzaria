from optparse import Values
import tkinter as tk
from tkinter import messagebox
import tela_confirmar_pedido
import tela_cardapio_salgado



def abrir_cardapio_bebidas(janela_categoria):
 
 #Função para VOltar para categorias
 def voltar():
    janela_bebidas.destroy()
    janela_categoria.deiconify()

#Função para Voltar para tela de categoria mas adicionando os produtos
 def continuar_comprando():
    #atualizando para chamar dentro da função para ela ficar sendo atualizada sempre com o valor atual
    Pizzas_adicionadas = tela_cardapio_salgado.Pizzas_adicionadas

    tamanho = [menu1.get(), menu2.get(), menu3.get(), menu4.get(), menu5.get(), menu6.get(), menu7.get()]


    
    sabores = ['COCA-COLA','GUARANA','FANTA UVA', 'PEPSI', 'SODA', 'CHÁ', 'LIMONADA']

    Quantidade = [int(entry_item1.get()), int(entry_item2.get()), int(entry_item3.get()), int(entry_item4.get()),
                   int(entry_item5.get()), int(entry_item6.get()), int(entry_item7.get())]
    
   
    i = 0
    for item in Quantidade:

      if item > 0:
         
         if tamanho[i] !='Tamanho':


            pizza = [sabores[i], tamanho[i], item]
           
            
            Pizzas_adicionadas.append(pizza)
            
         else:
            messagebox.showinfo("ERRO",'Tamanho não selecionado, Verifique e tente novamente!')
            return
      i +=1

  
    if Pizzas_adicionadas != []:
         print(Pizzas_adicionadas)
         janela_bebidas.destroy()
         janela_categoria.deiconify()
    else:
       messagebox.showinfo("ERRO",'Selecione ao menos uma Pizza antes de Continuar')

#Função para ir para tela de pagamento
 def abri_final():
     #atualizando para chamar dentro da função para ela ficar sendo atualizada sempre com o valor atual
    Pizzas_adicionadas = tela_cardapio_salgado.Pizzas_adicionadas

    tamanho = [menu1.get(), menu2.get(), menu3.get(), menu4.get(), menu5.get(), menu6.get(), menu7.get()]


    
    sabores = ['COCA-COLA','GUARANA','FANTA UVA', 'PEPSI', 'SODA', 'CHÁ', 'LIMONADA']

    Quantidade = [int(entry_item1.get()), int(entry_item2.get()), int(entry_item3.get()), int(entry_item4.get()),
                   int(entry_item5.get()), int(entry_item6.get()), int(entry_item7.get())]
    
    tamanhos = [menu1, menu2, menu3, menu4, menu5, menu6, menu7]
    
    Quantidades = [entry_item1, entry_item2, entry_item3, entry_item4,entry_item5, entry_item6, entry_item7]
   
    
    i = 0
    for item in Quantidade:

      if item > 0:
         
         if tamanho[i] !='Tamanho':



            pizza = [sabores[i], tamanho[i], item]
           
            
            Pizzas_adicionadas.append(pizza)
            
         else:
            messagebox.showinfo("ERRO",'Tamanho não selecionado, Verifique e tente novamente!')
            return
      i +=1

  
    if Pizzas_adicionadas != []:
         for tamanho in tamanhos:
            tamanho.set('Tamanho')
         for quantidade in Quantidades:
            quantidade.configure(values=(0,1,2,3,4,5))
         print(Pizzas_adicionadas)
         janela_bebidas.withdraw()
         tela_confirmar_pedido.confirmar_pedido(janela_bebidas,Pizzas_adicionadas)
    else:
       messagebox.showinfo("ERRO",'Selecione ao menos uma Bebida antes de Continuar')


    
 janela_bebidas = tk.Toplevel(janela_categoria)
 janela_bebidas.title("Cardapio Bebidas")
 janela_bebidas.geometry("650x600")
 janela_bebidas.configure(background= '#eb4764')
 janela_bebidas.resizable(False, False)
 janela_bebidas.iconbitmap("PIZZARIA\\img\\icon.ico")
  
 #Criando frame da tela de pizzas salgadas
 frame=tk.Frame(janela_bebidas, bd = 4, bg = '#c95b6e',
                     highlightbackground= '#c52f49', highlightthickness= 3 )
 frame.place(relx=0.02, rely=0.02, relwidth= 0.96, relheight = 0.96)
 
 #Titulo da pagina
 titulo_label = tk.Label(frame, text="Bebidas", bg= '#c52f49', fg='white'
                    , font = ('Arial Black', 16, "bold",'underline'))
 titulo_label.pack(padx=10, pady=10)
 
  
 #Titulos
 trad_label = tk.Label(frame,text="Bebidas Disponíveis R$12", bg= '#c52f49', fg='white'
                    , font = ('Arial', 12, "bold"))
 trad_label.place(x=220, y= 70)

 sabor_label = tk.Label(frame,text="Sabor", bg= '#c52f49', fg='black'
                    , font = ('Arial', 11, "bold"))
 sabor_label.place(x=160, y= 100)
 
 tamanho_label = tk.Label(frame,text="Tamanho", bg= '#c52f49', fg='black'
                    , font = ('Arial', 11, 'bold'))
 tamanho_label.place(x=260, y= 100)

 quantidade_label = tk.Label(frame,text="Quantidade", bg= '#c52f49', fg='black'
                    , font = ('Arial', 11, 'bold'))
 quantidade_label.place(x=360, y= 100)

 #Sabores das Pizzas
 sabores = ['COCA-COLA','GUARANA','FANTA UVA', 'PEPSI', 'SODA', 'CHÁ', 'LIMONADA']
    
 for idx, sabor in enumerate(sabores):
   item_label = tk.Label(frame, text=sabor, bg='#c95b6e', fg='black', font=('Arial', 9, 'bold'))
   item_label.place(x=150, y=130 + idx * 20) 

 #Menus de Tamanho das pizzas
 menu1 = tk.StringVar()
 menu1.set("Tamanho")  

 menu2 = tk.StringVar()
 menu2.set("Tamanho")  

 menu3 = tk.StringVar()
 menu3.set("Tamanho")  

 menu4 = tk.StringVar()
 menu4.set("Tamanho")  

 menu5 = tk.StringVar()
 menu5.set("Tamanho")  

 menu6 = tk.StringVar()
 menu6.set("Tamanho")  

 menu7 = tk.StringVar()
 menu7.set("Tamanho")

 menu_item1 =tk.OptionMenu(frame, menu1 ,"1 LT", "2 LT", "LATA")
 menu_item1.config(fg="black", bg="#c95b6e", font=('Arial', 9, 'bold'))
 menu_item1["menu"].config(fg="black", bg="#c95b6e")
 menu_item1.place(x=250, y= 130, width=88, height=20) 

 menu_item2 =tk.OptionMenu(frame, menu2 ,"1 LT", "2 LT", "LATA")
 menu_item2.config(fg="black", bg="#c95b6e", font=('Arial', 9, 'bold'))
 menu_item2["menu"].config(fg="black", bg="#c95b6e")
 menu_item2.place(x=250, y=150, width=88, height=20)

 menu_item3 =tk.OptionMenu(frame, menu3 ,"1 LT", "2 LT", "LATA")
 menu_item3.config(fg="black", bg="#c95b6e", font=('Arial', 9, 'bold'))
 menu_item3["menu"].config(fg="black", bg="#c95b6e")
 menu_item3.place(x=250, y=170, width=88, height=20)

 menu_item4 =tk.OptionMenu(frame, menu4 ,"1 LT", "2 LT", "LATA")
 menu_item4.config(fg="black", bg="#c95b6e", font=('Arial', 9, 'bold'))
 menu_item4["menu"].config(fg="black", bg="#c95b6e")
 menu_item4.place(x=250, y=190, width=88, height=20)

 menu_item5 =tk.OptionMenu(frame, menu5 ,"1 LT", "2 LT", "LATA")
 menu_item5.config(fg="black", bg="#c95b6e", font=('Arial', 9, 'bold'))
 menu_item5["menu"].config(fg="black", bg="#c95b6e")
 menu_item5.place(x=250, y=210, width=88, height=20)

 menu_item6 =tk.OptionMenu(frame, menu6 ,"1 LT", "2 LT", "LATA")
 menu_item6.config(fg="black", bg="#c95b6e", font=('Arial', 9, 'bold'))
 menu_item6["menu"].config(fg="black", bg="#c95b6e")
 menu_item6.place(x=250, y=230, width=88, height=20)

 menu_item7 =tk.OptionMenu(frame, menu7 ,"1 LT", "2 LT", "LATA")
 menu_item7.config(fg="black", bg="#c95b6e", font=('Arial', 9, 'bold'))
 menu_item7["menu"].config(fg="black", bg="#c95b6e")
 menu_item7.place(x=250, y=250, width=88, height=20)

#Caixa de Quantidades
 entry_item1 = tk.Spinbox(frame,values=(0,1,2,3,4,5) ,bg="#a95b6e", fg='black')
 entry_item1.place(x=380, y= 130, width=40, height=18)

 entry_item2 = tk.Spinbox(frame,values=(0,1,2,3,4,5) ,bg="#a95b6e", fg='black')
 entry_item2.place(x=380, y= 150, width=40, height=18)

 entry_item3 = tk.Spinbox(frame,values=(0,1,2,3,4,5) ,bg="#a95b6e", fg='black')
 entry_item3.place(x=380, y= 170, width=40, height=18)

 entry_item4 = tk.Spinbox(frame,values=(0,1,2,3,4,5) ,bg="#a95b6e", fg='black')
 entry_item4.place(x=380, y= 190, width=40, height=18)

 entry_item5 = tk.Spinbox(frame,values=(0,1,2,3,4,5) ,bg="#a95b6e", fg='black')
 entry_item5.place(x=380, y= 210, width=40, height=18)

 entry_item6 = tk.Spinbox(frame,values=(0,1,2,3,4,5) ,bg="#a95b6e", fg='black')
 entry_item6.place(x=380, y= 230, width=40, height=18)

 entry_item7 = tk.Spinbox(frame,values=(0,1,2,3,4,5) ,bg="#a95b6e", fg='black')
 entry_item7.place(x=380, y= 250, width=40, height=18)

#Botão Cancelar
 botap_cancelar = tk.Button(frame, text="Voltar", bd=2, bg = '#c52f49' , fg = 'white' 
                            , font = ('verdana', 8, 'bold'), command=voltar)
 botap_cancelar.place(x=100, y=520)

#Botão De finalizar Pedido
 botao_finalizar_pedido = tk.Button(frame, text="Finalizar Pedido", bd=2, bg = '#c52f49' , fg = 'white' 
                            , font = ('verdana', 8, 'bold'), command=abri_final)
 botao_finalizar_pedido.place(x=450, y=520)

#Botão de Continuar Comprando
 botao_continuar_comprando = tk.Button(frame, text="Continuar Comprando", bd=2, bg = '#c52f49' , fg = 'white' 
                            , font = ('verdana', 8, 'bold'), command=continuar_comprando)
 botao_continuar_comprando.place(x=230, y=520)

