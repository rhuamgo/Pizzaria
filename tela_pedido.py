import tkinter as tk



def abrir_pedido(janela_incial):
 def voltar():
        janela_pedido.destroy()
        janela_incial.deiconify()

 janela_pedido = tk.Toplevel(janela_incial)  
 janela_pedido.title("Pedido")
 janela_pedido.geometry("400x400")
 janela_pedido.configure(background= '#eb4764')
 janela_pedido.resizable(False, False)
 janela_pedido.iconbitmap("PIZZARIA\\img\\icon.ico")

   
   
 frame1=tk.Frame(janela_pedido, bd = 4, bg = '#dfe3ee',
                     highlightbackground= '#c52f49', highlightthickness= 3 )
 frame1.place(relx=0.02, rely=0.02, relwidth= 0.96, relheight = 0.96)

 label = tk.Label(frame1, text="Bem-vindo à Tela de pedido", bg= '#d72e4c')
 label.pack(pady=20)
    
 botao_voltar = tk.Button(frame1, text="Voltar", command=voltar)
 botao_voltar.pack(pady=20)

