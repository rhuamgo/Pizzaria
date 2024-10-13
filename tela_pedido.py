import tkinter as tk

def abrir_janela():
    janela_pedido = tk.Tk()  
    janela_pedido.title("Pedido")
    janela_pedido.geometry("400x400")
    janela_pedido.configure(background= '#1e3743')
    janela_pedido.resizable(False, False)
    janela_pedido.iconbitmap("icon.ico")
   
    frame1=tk.Frame(janela_pedido, bd = 4, bg = '#dfe3ee',
                     highlightbackground= '#759fe6', highlightthickness= 3 )
    frame1.place(relx=0.02, rely=0.02, relwidth= 0.96, relheight = 0.96)

    label = tk.Label(janela_pedido, text="Bem-vindo à Tela de pedido", bg= '#108DB2')
    label.pack(pady=20)
    
    janela_pedido.mainloop()
