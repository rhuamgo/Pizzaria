import tkinter as tk


def abrir_contato(janela_incial):
    
 def voltar():
        janela_contato.destroy()
        janela_incial.deiconify()


 janela_contato = tk.Toplevel()  
 janela_contato.title("Contato")
 janela_contato.geometry("400x400")
 janela_contato.configure(background= '#eb4764')
 janela_contato.resizable(False, False)
 janela_contato.iconbitmap("img\\icon.ico")

 frame_contato=tk.Frame(janela_contato, bd = 4, bg = '#c95b6e',
                     highlightbackground= '#c52f49', highlightthickness= 3 )
 frame_contato.place(relx=0.02, rely=0.02, relwidth= 0.96, relheight = 0.96)


 label_titulo = tk.Label(frame_contato, text="Pizzaria Lá Casa",bd=4, bg= '#c52f49', fg='white'
                    , font = ("Arial Black", 14, 'bold'))
 label_titulo.pack(padx=10)

 label_descricao = tk.Label(frame_contato, text="Seja Bem-Vindo!",bd=4, bg= '#c52f49', fg='white'
                    , font = ("Arial", 12, 'bold'))
 label_descricao.pack(padx=10, pady=10)

 label_titulo = tk.Label(frame_contato, text="Telefone para Contato: \n (48) 99120-3158",bd=4, bg= '#c52f49', fg='white'
                    , font = ("Arial", 12, 'bold'))
 label_titulo.pack(padx=10, pady=10)

 label_titulo = tk.Label(frame_contato, text="Horario de Funcionamento:\n Segunda a Sexta das 09:00 AM As 22:00 PM \n"+
                         "Sabado e Domingo das 09:00 AM As 02:00 AM",bd=4, bg= '#c52f49', fg='white'
                           , font = ("Arial", 10, 'bold'))
 label_titulo.pack(padx=10, pady=10)
 
 image_contato = tk.PhotoImage(file="img\\qrCode.png")
 janela_contato.img_retire= image_contato

 label_qrCode = tk.Label(frame_contato, image=image_contato)
 label_qrCode.pack(padx=10)

 botao_voltar = tk.Button(frame_contato, text="Voltar", bd=2, bg = '#d72e4c' , fg = 'white' 
                            , font = ('verdana', 8, 'bold'), command=voltar)
 botao_voltar.pack(padx=10, pady=10)
