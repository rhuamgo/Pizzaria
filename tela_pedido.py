import tkinter as tk

def abrir_janela():
    janela_pedido = tk.Toplevel()  
    janela_pedido.title("Pedido")
    
    label = tk.Label(janela_pedido, text="Bem-vindo à Tela de pedido")
    label.pack(pady=20)
    
    janela_pedido.geometry("400x400")