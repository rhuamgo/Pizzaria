import tkinter as tk

def abrir_janela():
    nova_janela = tk.Toplevel()  
    nova_janela.title("Nova Janela")
    
    label = tk.Label(nova_janela, text="Bem-vindo à Tela de pedido")
    label.pack(pady=20)
    
    nova_janela.geometry("400x400")