import tkinter as tk
from tkinter import messagebox

def sair():
    messagebox.showinfo('sair', 'até breve')
    root.destroy()

def ir_para_cadastro():
    messagebox.showinfo('login')

    #Janela principal
root = tk.Tk()
root.title('Login do Usuário')

    #Página,

titulo = tk.Label(root, text= 'Tela de login', font=('verdana', 18))

    #layout

tk.Label(root, text='nome').pack(pady=40)
nome_entry = tk.Entry(root)
nome_entry.pack(pady=40)

    #layout da senha

tk.Label(root, text='senha:').pack(pady=40)
senha_entry = tk.Entry(root, show='*')
senha_entry.pack(pady=40)

    #botao para sair

btn_sair = tk.Button(root, text='sair', command= sair, width=17, height=5, bg='blue', fg='white')
btn_sair.pack(side=tk.LEFT, padx= 40, pady= 40)

    #botao login

btn_login = tk.Button(root, text='nome', command= ir_para_cadastro)
btn_login.pack(side=tk.LEFT, padx=40, pady=40)


    #inicio do loop da interface
root.mainloop()
