from optparse import Values
import tkinter as tk

def abrir_cardapio_salgado(janela_categoria):
 def voltar():
    janela_salgado.destroy()
    janela_categoria.deiconify()

    
 janela_salgado = tk.Toplevel(janela_categoria)
 janela_salgado.title("Cardapio Pizzas Salgadas")
 janela_salgado.geometry("650x600")
 janela_salgado.configure(background= '#eb4764')
 janela_salgado.resizable(False, False)
 janela_salgado.iconbitmap("PIZZARIA\\img\\icon.ico")
  
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

 #Itens
 item1_label = tk.Label(frame,text="CALABRESA", bg= '#c95b6e', fg='black'
                    , font = ('Arial', 9, 'bold'))
 item1_label.place(x=150, y= 130)

 item2_label = tk.Label(frame,text="TRADICIONAL", bg= '#c95b6e', fg='black'
                    , font = ('Arial', 9, 'bold'))
 item2_label.place(x=150, y= 150)

 item3_label = tk.Label(frame,text="LA CASA", bg= '#c95b6e', fg='black'
                    , font = ('Arial', 9, 'bold'))
 item3_label.place(x=150, y= 170)

 item4_label = tk.Label(frame,text="FRANGO", bg= '#c95b6e', fg='black'
                    , font = ('Arial', 9, 'bold'))
 item4_label.place(x=150, y= 190)

 item5_label = tk.Label(frame,text="LOMBO", bg= '#c95b6e', fg='black'
                    , font = ('Arial', 9, 'bold'))
 item5_label.place(x=150, y= 210)

 item6_label = tk.Label(frame,text="PALMITO", bg= '#c95b6e', fg='black'
                    , font = ('Arial', 9, 'bold'))
 item6_label.place(x=150, y= 230)

 item7_label = tk.Label(frame,text="PEPERONE", bg= '#c95b6e', fg='black'
                    , font = ('Arial', 9, 'bold'))
 item7_label.place(x=150, y= 250)



 #Menus de Quantidade
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
 menu_item1.config(fg="black", bg="#c95b6e", font=('Arial', 9, 'bold'))
 menu_item1["menu"].config(fg="black", bg="#c95b6e")
 menu_item1.place(x=250, y= 130, width=88, height=20) 

 menu_item2 =tk.OptionMenu(frame, menu2 ,"Grande", "Media", "Broto")
 menu_item2.config(fg="black", bg="#c95b6e", font=('Arial', 9, 'bold'))
 menu_item2["menu"].config(fg="black", bg="#c95b6e")
 menu_item2.place(x=250, y=150, width=88, height=20)

 menu_item3 =tk.OptionMenu(frame, menu3 ,"Grande", "Media", "Broto")
 menu_item3.config(fg="black", bg="#c95b6e", font=('Arial', 9, 'bold'))
 menu_item3["menu"].config(fg="black", bg="#c95b6e")
 menu_item3.place(x=250, y=170, width=88, height=20)

 menu_item4 =tk.OptionMenu(frame, menu4 ,"Grande", "Media", "Broto")
 menu_item4.config(fg="black", bg="#c95b6e", font=('Arial', 9, 'bold'))
 menu_item4["menu"].config(fg="black", bg="#c95b6e")
 menu_item4.place(x=250, y=190, width=88, height=20)

 menu_item5 =tk.OptionMenu(frame, menu5 ,"Grande", "Media", "Broto")
 menu_item5.config(fg="black", bg="#c95b6e", font=('Arial', 9, 'bold'))
 menu_item5["menu"].config(fg="black", bg="#c95b6e")
 menu_item5.place(x=250, y=210, width=88, height=20)

 menu_item6 =tk.OptionMenu(frame, menu6 ,"Grande", "Media", "Broto")
 menu_item6.config(fg="black", bg="#c95b6e", font=('Arial', 9, 'bold'))
 menu_item6["menu"].config(fg="black", bg="#c95b6e")
 menu_item6.place(x=250, y=230, width=88, height=20)

 menu_item7 =tk.OptionMenu(frame, menu7 ,"Grande", "Media", "Broto")
 menu_item7.config(fg="black", bg="#c95b6e", font=('Arial', 9, 'bold'))
 menu_item7["menu"].config(fg="black", bg="#c95b6e")
 menu_item7.place(x=250, y=250, width=88, height=20)

#Entry de Quantidades
 
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

###############################################################
 #Titulos
 especial_label = tk.Label(frame,text="Pizzas Especiais", bg= '#c52f49', fg='white'
                    , font = ('Arial', 12, "bold"))
 especial_label.place(x=220, y= 300)

 saborEsp_label = tk.Label(frame,text="Sabor", bg= '#c52f49', fg='black'
                    , font = ('Arial', 11, "bold"))
 saborEsp_label.place(x=160, y= 330)
 
 tamanhoEsp_label = tk.Label(frame,text="Tamanho", bg= '#c52f49', fg='black'
                    , font = ('Arial', 11, 'bold'))
 tamanhoEsp_label.place(x=260, y= 330)

 quantidadeEsp_label = tk.Label(frame,text="Quantidade", bg= '#c52f49', fg='black'
                    , font = ('Arial', 11, 'bold'))
 quantidadeEsp_label.place(x=360, y= 330)

 #Itens Pizzas Especiais
 item1_especial = tk.Label(frame,text="BAURU", bg= '#c95b6e', fg='black'
                    , font = ('Arial', 9, 'bold'))
 item1_especial.place(x=150, y= 360)

 item1_especial = tk.Label(frame,text="BRASILEIRA", bg= '#c95b6e', fg='black'
                    , font = ('Arial', 9, 'bold'))
 item1_especial.place(x=150, y= 380)

 item1_especial = tk.Label(frame,text="CARNE SECA", bg= '#c95b6e', fg='black'
                    , font = ('Arial', 9, 'bold'))
 item1_especial.place(x=150, y= 400)

 item1_especial = tk.Label(frame,text="IV QUEIJOS", bg= '#c95b6e', fg='black'
                    , font = ('Arial', 9, 'bold'))
 item1_especial.place(x=150, y= 420)

 item1_especial = tk.Label(frame,text="MODINHA", bg= '#c95b6e', fg='black'
                    , font = ('Arial', 9, 'bold'))
 item1_especial.place(x=150, y= 440)

 item1_especial = tk.Label(frame,text="TOSCANA", bg= '#c95b6e', fg='black'
                    , font = ('Arial', 9, 'bold'))
 item1_especial.place(x=150, y= 460)

 item1_especial = tk.Label(frame,text="CALABRESA II", bg= '#c95b6e', fg='black'
                    , font = ('Arial', 9, 'bold'))
 item1_especial.place(x=150, y= 480)



 #Menus de Tamanho
 menu1_especial = tk.StringVar()
 menu1_especial.set("Tamanho")  

 menu2_especial = tk.StringVar()
 menu2_especial.set("Tamanho")  

 menu3_especial = tk.StringVar()
 menu3_especial.set("Tamanho")  

 menu4_especial = tk.StringVar()
 menu4_especial.set("Tamanho")  

 menu5_especial = tk.StringVar()
 menu5_especial.set("Tamanho")  

 menu6_especial = tk.StringVar()
 menu6_especial.set("Tamanho")  

 menu7_especial = tk.StringVar()
 menu7_especial.set("Tamanho")

 menu_especial1 =tk.OptionMenu(frame, menu1_especial ,"Grande", "Media", "Broto")
 menu_especial1.config(fg="black", bg="#c95b6e", font=('Arial', 9, 'bold'))
 menu_especial1["menu"].config(fg="black", bg="#c95b6e")
 menu_especial1.place(x=250, y= 360, width=88, height=20) 


 menu_especial2 =tk.OptionMenu(frame, menu2_especial ,"Grande", "Media", "Broto")
 menu_especial2.config(fg="black", bg="#c95b6e", font=('Arial', 9, 'bold'))
 menu_especial2["menu"].config(fg="black", bg="#c95b6e")
 menu_especial2.place(x=250, y=380, width=88, height=20)

 menu_especial3 =tk.OptionMenu(frame, menu3_especial ,"Grande", "Media", "Broto")
 menu_especial3.config(fg="black", bg="#c95b6e", font=('Arial', 9, 'bold'))
 menu_especial3["menu"].config(fg="black", bg="#c95b6e")
 menu_especial3.place(x=250, y=400, width=88, height=20)

 menu_especial4 =tk.OptionMenu(frame, menu4_especial ,"Grande", "Media", "Broto")
 menu_especial4.config(fg="black", bg="#c95b6e", font=('Arial', 9, 'bold'))
 menu_especial4["menu"].config(fg="black", bg="#c95b6e")
 menu_especial4.place(x=250, y=420, width=88, height=20)

 menu_especial5 =tk.OptionMenu(frame, menu5_especial ,"Grande", "Media", "Broto")
 menu_especial5.config(fg="black", bg="#c95b6e", font=('Arial', 9, 'bold'))
 menu_especial5["menu"].config(fg="black", bg="#c95b6e")
 menu_especial5.place(x=250, y=440, width=88, height=20)

 menu_especial6 =tk.OptionMenu(frame, menu6_especial ,"Grande", "Media", "Broto")
 menu_especial6.config(fg="black", bg="#c95b6e", font=('Arial', 9, 'bold'))
 menu_especial6["menu"].config(fg="black", bg="#c95b6e")
 menu_especial6.place(x=250, y=460, width=88, height=20)

 menu_especial7 =tk.OptionMenu(frame, menu7_especial ,"Grande", "Media", "Broto")
 menu_especial7.config(fg="black", bg="#c95b6e", font=('Arial', 9, 'bold'))
 menu_especial7["menu"].config(fg="black", bg="#c95b6e")
 menu_especial7.place(x=250, y=480, width=88, height=20)

#Entry de Quantidades
 
 entry_especial1 = tk.Spinbox(frame,values=(0,1,2,3,4,5) ,bg="#a95b6e", fg='black')
 entry_especial1.place(x=380, y= 360, width=40, height=18)

 entry_especial2 = tk.Spinbox(frame,values=(0,1,2,3,4,5) ,bg="#a95b6e", fg='black')
 entry_especial2.place(x=380, y= 380, width=40, height=18)

 entry_especial3 = tk.Spinbox(frame,values=(0,1,2,3,4,5) ,bg="#a95b6e", fg='black')
 entry_especial3.place(x=380, y= 400, width=40, height=18)

 entry_especial4 = tk.Spinbox(frame,values=(0,1,2,3,4,5) ,bg="#a95b6e", fg='black')
 entry_especial4.place(x=380, y= 420, width=40, height=18)

 entry_especial5 = tk.Spinbox(frame,values=(0,1,2,3,4,5) ,bg="#a95b6e", fg='black')
 entry_especial5.place(x=380, y= 440, width=40, height=18)

 entry_especial6 = tk.Spinbox(frame,values=(0,1,2,3,4,5) ,bg="#a95b6e", fg='black')
 entry_especial6.place(x=380, y= 460, width=40, height=18)

 entry_especial7 = tk.Spinbox(frame,values=(0,1,2,3,4,5) ,bg="#a95b6e", fg='black')
 entry_especial7.place(x=380, y= 480, width=40, height=18)


###################################################################
 botao_voltar = tk.Button(frame, text="Voltar", bd=2, bg = '#c52f49' , fg = 'white' 
                            , font = ('verdana', 8, 'bold'), command=voltar)
 botao_voltar.place(x=270, y=520)





