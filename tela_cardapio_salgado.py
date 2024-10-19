from optparse import Values
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tela_confirmar_pedido



Pizzas_adicionadas = []
def abrir_cardapio_salgado(janela_categoria):
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
 def voltar():
    janela_salgado.destroy()
    janela_categoria.deiconify()

#Função para Voltar para tela de categoria mas adicionando os produtos
 def continuar_comprando():


    tamanho = [menu1.get(), menu2.get(), menu3.get(), menu4.get(), menu5.get(), menu6.get(), menu7.get()]


    
    sabores = ['CALABRESA','TRADICIONAL','LA CASA', 'FRANGO', 'LOMBO', 'PALMITO', 'PEPERONE']

    Quantidade = [entry_item1.get(), entry_item2.get(), entry_item3.get(), entry_item4.get(),
                   entry_item5.get(), entry_item6.get(), entry_item7.get()]
    i = 0
    for item in Quantidade:
      try:
         item =int(item)
         if item > 0:
            
            if tamanho[i] !='Tamanho':
              

               pizza = [sabores[i], tamanho[i], item]
           
            
               Pizzas_adicionadas.append(pizza)
            
            else:
                messagebox.showinfo("ERRO",'Tamanho não selecionado, Verifique e tente novamente!')
                return
         i +=1

  
      except:
          messagebox.showerror("ERRO", "Informe um valor Valido")
          return
      
    if Pizzas_adicionadas != []:
         print(Pizzas_adicionadas)
         janela_salgado.destroy()
         janela_categoria.deiconify()
         
    else:
       messagebox.showinfo("ERRO",'Selecione ao menos uma Pizza antes de Continuar')


 janela_salgado = tk.Toplevel(janela_categoria)
 janela_salgado.title("Cardapio Pizzas Salgadas")
 janela_salgado.configure(background= '#eb4764')
 janela_salgado.resizable(False, False)
 janela_salgado.iconbitmap("img\\icon.ico")
  
 largura_janela = 650
 altura_janela = 600
 centralizando_Janela(janela_salgado, largura_janela, altura_janela)



 #Criando frame da tela de pizzas salgadas
 frame=tk.Frame(janela_salgado, bd = 4, bg = '#c95b6e',
                     highlightbackground= '#c52f49', highlightthickness= 3 )
 frame.place(relx=0.02, rely=0.02, relwidth= 0.96, relheight = 0.96)
 
 #Titulo da pagina
 titulo_label = tk.Label(frame, text="Pizzas Salgadas", bg= '#c52f49', fg='white'
                    , font = ('Arial Black', 16, "bold",'underline'))
 titulo_label.pack(padx=10, pady=10)
 
  
 #Titulos
 trad_label = tk.Label(frame,text="Pizzas Tradicionais", bg= '#c52f49', fg='white'
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
 sabores = ["CALABRESA", "TRADICIONAL", "LA CASA", "FRANGO", "LOMBO", "PALMITO", "PEPERONE",]
    
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

 menu_item1 =tk.OptionMenu(frame, menu1 ,"Grande", "Media", "Broto")
 menu_item1.config(fg="black", bg="#c95b6e", font=('Arial', 10, 'bold'))
 menu_item1["menu"].config(fg="black", bg="#c95b6e")
 menu_item1.place(x=250, y= 130, width=94, height=22) 

 menu_item2 =tk.OptionMenu(frame, menu2 ,"Grande", "Media", "Broto")
 menu_item2.config(fg="black", bg="#c95b6e", font=('Arial', 10, 'bold'))
 menu_item2["menu"].config(fg="black", bg="#c95b6e")
 menu_item2.place(x=250, y=150, width=94, height=22)

 menu_item3 =tk.OptionMenu(frame, menu3 ,"Grande", "Media", "Broto")
 menu_item3.config(fg="black", bg="#c95b6e", font=('Arial', 10, 'bold'))
 menu_item3["menu"].config(fg="black", bg="#c95b6e")
 menu_item3.place(x=250, y=170, width=94, height=22)

 menu_item4 =tk.OptionMenu(frame, menu4 ,"Grande", "Media", "Broto")
 menu_item4.config(fg="black", bg="#c95b6e", font=('Arial', 10, 'bold'))
 menu_item4["menu"].config(fg="black", bg="#c95b6e")
 menu_item4.place(x=250, y=190, width=94, height=22)

 menu_item5 =tk.OptionMenu(frame, menu5 ,"Grande", "Media", "Broto")
 menu_item5.config(fg="black", bg="#c95b6e", font=('Arial', 10, 'bold'))
 menu_item5["menu"].config(fg="black", bg="#c95b6e")
 menu_item5.place(x=250, y=210, width=94, height=22)

 menu_item6 =tk.OptionMenu(frame, menu6 ,"Grande", "Media", "Broto")
 menu_item6.config(fg="black", bg="#c95b6e", font=('Arial', 10, 'bold'))
 menu_item6["menu"].config(fg="black", bg="#c95b6e")
 menu_item6.place(x=250, y=230, width=94, height=22)

 menu_item7 =tk.OptionMenu(frame, menu7 ,"Grande", "Media", "Broto")
 menu_item7.config(fg="black", bg="#c95b6e", font=('Arial', 10, 'bold'))
 menu_item7["menu"].config(fg="black", bg="#c95b6e")
 menu_item7.place(x=250, y=250, width=94, height=22)

#Caixa de Quantidades
 entry_item1 = tk.Spinbox(frame,values=(0,1,2,3,4,5) ,bg="#a95b6e", fg='black', font=('Arial', 11))
 entry_item1.place(x=380, y= 130, width=40, height=20)

 entry_item2 = tk.Spinbox(frame,values=(0,1,2,3,4,5) ,bg="#a95b6e", fg='black', font=('Arial', 11))
 entry_item2.place(x=380, y= 150, width=40, height=20)

 entry_item3 = tk.Spinbox(frame,values=(0,1,2,3,4,5) ,bg="#a95b6e", fg='black', font=('Arial', 11))
 entry_item3.place(x=380, y= 170, width=40, height=20)

 entry_item4 = tk.Spinbox(frame,values=(0,1,2,3,4,5) ,bg="#a95b6e", fg='black', font=('Arial', 11))
 entry_item4.place(x=380, y= 190, width=40, height=20)

 entry_item5 = tk.Spinbox(frame,values=(0,1,2,3,4,5) ,bg="#a95b6e", fg='black', font=('Arial', 11))
 entry_item5.place(x=380, y= 210, width=40, height=20)

 entry_item6 = tk.Spinbox(frame,values=(0,1,2,3,4,5) ,bg="#a95b6e", fg='black', font=('Arial', 11))
 entry_item6.place(x=380, y= 230, width=40, height=20)

 entry_item7 = tk.Spinbox(frame,values=(0,1,2,3,4,5) ,bg="#a95b6e", fg='black', font=('Arial', 11))
 entry_item7.place(x=380, y= 250, width=40, height=20)


 #Titulos dos Sabores Especiais
 #Criando minha teabela de preços
 especial_label = tk.Label(frame,text="Tabela de Preços", bg= '#c52f49', fg='white'
                    , font = ('Arial', 12, "bold"))
 especial_label.place(x=220, y= 315)

 #Criando e estilizando 
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

#Função que bloqueia o selecionado do TreeView   
 def block_selection(event):
    tw.selection_remove(tw.selection())
 lista = [['Grande', 'R$ 42,00' ], ['Media', 'R$ 32,00'], ['Broto', 'R$ 18,00']]

 tw = ttk.Treeview(frame, columns=('Tamanhos', 'Valores'), show='headings', height=3)
    
    # Configurando as colunas
 tw.column('Tamanhos', minwidth=0, width=110, anchor='center')
 tw.column('Valores', minwidth=0, width=70, anchor='center')

 
    # Definindo os títulos das colunas
 tw.heading('Tamanhos', text='Tamanhos')
 tw.heading('Valores', text='Valores')
 tw.place(x=200, y=355)

 for (tamanho, valor) in lista:
        tw.insert("", "end", values=(tamanho, valor))
 
 #Pega o evento selecionar do Treeview e cham função que bloqueia ele 
 tw.bind("<<TreeviewSelect>>", block_selection)

#Botão Cancelar
 botap_cancelar = tk.Button(frame, text="Voltar", bd=2, bg = '#c52f49' , fg = 'white' 
                            , font = ('verdana', 8, 'bold'), command=voltar)
 botap_cancelar.place(x=200, y=520)

#Botão de Continuar Comprando
 botao_continuar_comprando = tk.Button(frame, text="Continuar Comprando", bd=2, bg = '#c52f49' , fg = 'white' 
                            , font = ('verdana', 8, 'bold'), command=continuar_comprando)
 botao_continuar_comprando.place(x=300, y=520)

