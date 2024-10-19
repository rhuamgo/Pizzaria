import tkinter as tk
from tkinter import  END, messagebox
import tela_cardapio_salgado


def finalizarPedido(janela,tipoPedido,janelaInicial):
 def centralizando_Janela(janela, largura, altura):
    #Pega o tamanho da tela em pixel 
    largura_tela = janela.winfo_screenwidth() #essa função pergunta para SO do monitor e retorna o valor em largura e altura
    altura_tela = janela.winfo_screenheight()
    #Dide o tamanho e a largura da tela por 2 e subtrais com a divisão dos mesmo valores da janela
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    #passa o tamanho da tela posicionando ela no eixo x e y
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

 def formatar_telefone(event):
    #da um get no entry e gudar na variavel
    telefone = telefoneEntry.get()
    codigo = 0
    # usei o replace para substituir caracter especiais e espaços da variavel para ela ficar "limpa"
    telefone = telefone.replace("(", "").replace(")", "").replace(" ", "").replace("-", "")

    #usei o len para ver o tamanho da strin e verifico se ela tem pelo menos 11 digitos
    if len(telefone) <= 11 :
        #formato a variavel fatiando ela pelo [parametro inicial:parametro final]
        telefone = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"

    # pego o valor atual do entry e deleto ele todo e insiro com o insert o novo valor
        codigo =(telefone[11:])
        telefoneEntry.delete(0, END)
        telefoneEntry.insert(0, telefone)
        if tipoPedido == 'Retirada':
            codigoPedido.configure(text=f'Codigo de Retirada: {codigo}',bg = '#d72e4c' , fg = 'white' 
                            , font = ('verdana', 10, 'bold'))
            codigoPedido.place(x=120, y=190)
    else:
        messagebox.showerror("ERRO", "Verifique o numero")
        telefoneEntry.delete(0, END)
        

 def finalizarEntrega():
    if tipoPedido == 'Entrega':
        telefone = telefoneEntry.get()   
        if nomeEntry.get() == "" or telefoneEntry.get() == "" or endecoEntry.get() == "": 
            messagebox.showinfo("ERRO", "Preencha todos os campos e tente novamente!")
            return
        elif telefone[13:] == "":  
            messagebox.showinfo("ERRO", "Telefone Invalido Verifique e tente novamente!") 
            
        else:
            messagebox.showinfo("PEDIDO CONFIRMADO", "PEDIDO CONFIRMADO COM SUCESSO! \n \n A Entrega sera efetuada em até 20 minutos!")
            janela_final.destroy()
            janelaInicial.deiconify()
            tela_cardapio_salgado.Pizzas_adicionadas = []

    else: 
        telefone = telefoneEntry.get()

        if nomeRetiraEntry.get() == "":
            messagebox.showwarning("ERRO", "Preencha todos os campos e tente novamente!")
            return
        elif telefone[13:] == "":  
                messagebox.showinfo("ERRO", "Telefone Invalido Verifique e tente novamente!") 
                
        else:    
            messagebox.showinfo("PEDIDO CONFIRMADO", "PEDIDO CONFIRMADO COM SUCESSO! \n \n Seu pedido já está em produção")
            janela_final.destroy()
            janelaInicial.deiconify()
            tela_cardapio_salgado.Pizzas_adicionadas = []
        
 def voltar():
        janela_final.destroy()
        janela.deiconify()

 janela_final = tk.Toplevel(janela)  
 janela_final.title("Finalizar Pedido")
 janela_final.configure(background= '#eb4764')
 janela_final.resizable(False, False)
 janela_final.iconbitmap("img\\icon.ico")

 largura_janela = 400
 altura_janela = 450
 centralizando_Janela(janela_final, largura_janela, altura_janela)
 




 frame1=tk.Frame(janela_final, bd = 4, bg = '#c95b6e',
                     highlightbackground= '#c52f49', highlightthickness= 0 )
 frame1.place(relx=0.02, rely=0.02, relwidth= 0.96, relheight = 0.96)
 
 #SE O PEDIDO FOR ENTREGA
 if tipoPedido == 'Entrega':

     titulo_retirada = tk.Label(frame1,text="ENTREGA", bg= '#c52f49', fg='white'
                    , font = ('Arial Black', 14, "bold"))
     titulo_retirada.pack(padx=10, pady=30)
     
     #CAMPO NOME
     nome = tk.Label(frame1, text='Nome:                ',bd=3, bg = '#d72e4c' , fg = 'white' 
                            , font = ('verdana', 10, 'bold'))
     nome.place(x=23, y=120)

     nomeEntry = tk.Entry(frame1, width=22,bd=2,font=('verdana', 10) )
     nomeEntry.place(x=140, y=120)

     #CAMPO NUMERO TELL
     telefone = tk.Label(frame1, text='Telefone:          ',bd=3, bg = '#d72e4c' , fg = 'white' 
                            , font = ('verdana', 10, 'bold'))
     telefone.place(x=23, y=150)

     telefoneEntry = tk.Entry(frame1, width=22,bd=2,font=('verdana', 10) )
     telefoneEntry.place(x=140, y=150)
     #usei o bind para vincular o evento "liberar tecla" com a função da mascara
     telefoneEntry.bind("<KeyRelease>", formatar_telefone)
     
     #CAMPO ENDEREÇO
     endereco = tk.Label(frame1, text='Endereço:         ',bd=3, bg = '#d72e4c' , fg = 'white' 
                            , font = ('verdana', 10, 'bold'))
     endereco.place(x=23, y=180)

     endecoEntry = tk.Entry(frame1, width=22,bd=2,font=('verdana', 10) )
     endecoEntry.place(x=140, y=180)

    #CAMPO NUMERO ENDEREÇO
     numero = tk.Label(frame1, text='N°:',bd=3, bg = '#d72e4c' , fg = 'white' 
                            , font = ('verdana', 10, 'bold'))
     numero.place(x=252, y=210)

     numeroEntry = tk.Entry(frame1, width=4,bd=2,font=('verdana', 10) )
     numeroEntry.place(x=285, y=210)

    #CAMPO COMPLEMENTO
     complemento = tk.Label(frame1, text='Complemento:',bd=4, bg = '#d72e4c' , fg = 'white' 
                            , font = ('verdana', 10, 'bold'))
     complemento.place(x=23, y=210)

     complementoEntry = tk.Entry(frame1, width=13,bd=2,font=('verdana', 10) )
     complementoEntry.place(x=140, y=210)
    
     #BOTÃO VOLTAR
     botao_voltar = tk.Button(frame1, text="Voltar", bd=2, bg = '#d72e4c' , fg = 'white' 
                            , font = ('verdana', 8, 'bold'), command=voltar)
     botao_voltar.place(x=100, y=350)
     
     #BOTAO FINALIZAR
     botao_voltar = tk.Button(frame1, text="Finalizar", bd=2, bg = '#d72e4c' , fg = 'white' 
                            , font = ('verdana', 8, 'bold'), command=finalizarEntrega)
     botao_voltar.place(x=250, y=350)

#SE O TIPO FOR RETIRADA
 if tipoPedido == 'Retirada':

     titulo_retirada = tk.Label(frame1,text="RETIRADA", bg= '#c52f49', fg='white'
                    , font = ('Arial Black', 14, "bold"))
     titulo_retirada.pack(padx=10, pady=30)
     
     #CAMPO NOME
     nome = tk.Label(frame1, text='Nome:               ',bd=3, bg = '#d72e4c' , fg = 'white' 
                            , font = ('verdana', 10, 'bold'))
     nome.place(x=23, y=120)

     nomeRetiraEntry = tk.Entry(frame1, width=22,bd=2,font=('verdana', 10) )
     nomeRetiraEntry.place(x=140, y=120)

     #CAMPO NUMERO TELL
     telefone = tk.Label(frame1, text='Telefone:           ',bd=3, bg = '#d72e4c' , fg = 'white' 
                            , font = ('verdana', 10, 'bold'))
     telefone.place(x=23, y=150)

     telefoneEntry = tk.Entry(frame1, width=22,bd=2,font=('verdana', 10) )
     telefoneEntry.place(x=140, y=150)

     #usei o bind para vincular o evento "liberar tecla" com a função da mascara
     telefoneEntry.bind("<KeyRelease>", formatar_telefone)
     
     #CODIGO DE RETIRADA
     codigoPedido = tk.Label(frame1,bd=3,text='Codigo de Retirada: ' ,bg = '#d72e4c' , fg = 'white' 
                            , font = ('verdana', 10, 'bold'))
     
     codigoPedido.place(x=120, y=190)
     
     #ENDEREÇO LOJA
     endereco = tk.Label(frame1, text='Endereço de Retirada: Rua Miguel Arcanjo n°48',bd=3, bg = '#d72e4c' , fg = 'white' 
                            , font = ('verdana', 10, 'bold'))
     endereco.place(x=23, y=220)





     #BOTÃO VOLTAR
     botao_voltar = tk.Button(frame1, text="Voltar", bd=2, bg = '#d72e4c' , fg = 'white' 
                            , font = ('verdana', 8, 'bold'), command=voltar)
     botao_voltar.place(x=100, y=350)
     
     #BOTAO FINALIZAR
     botao_voltar = tk.Button(frame1, text="Finalizar", bd=2, bg = '#d72e4c' , fg = 'white' 
                            , font = ('verdana', 8, 'bold'), command=finalizarEntrega)
     botao_voltar.place(x=250, y=350)



 janela_final.mainloop()