from tkinter import *

class Gui():
    #Classe que define a interface gráfica da aplicação
    window = Tk()
    window.wm_title("Cadastro de Pessoas")

    #Criando variáveis que armazenarão o texto inserido pelo usuário
    txtNome = StringVar()
    txtPai = StringVar()
    txtMae = StringVar()
    txtIdade = StringVar()
    txtEndereco = StringVar()

    #Criando os objetos que estarão na janela
    lblNome = Label(window, text="Nome:")
    lblPai = Label(window, text="Pai:")
    lblMae = Label(window, text="Mãe:")
    lblIdade = Label(window, text="Idade:")
    lblEndereco = Label(window, text="Endereço")

    #Criando 
    entNome = Entry(window, textvariable=txtNome)
    entPai = Entry(window, textvariable=txtPai)
    entMae = Entry(window, textvariable=txtMae)
    entIdade = Entry(window, textvariable=txtIdade)
    entEndereco = Entry(window, textvariable=txtEndereco)

    #Criando Listbox e Scroobar
    listaPessoas = Listbox(window)
    scrollPessoas = Scrollbar(window)

    #Criando os botões da tela
    btnVerTodos = Button(window, text="Ver Todos")
    btnBuscar = Button(window, text="Buscar")
    btnInserir = Button(window, text="Inserir")
    btnAtualizar = Button(window, text="Atualizar selecionados")
    btnDel = Button(window, text="Deletar selecionados")
    btnClose = Button(window, text="Fechar")

    #Posicionando objetos na tela
    lblNome.grid(row=0,column=0)
    lblPai.grid(row=1,column=0)
    lblMae.grid(row=2,column=0)
    lblIdade.grid(row=3,column=0)
    lblEndereco.grid(row=4,column=0)
    entNome.grid(row=0, column=1, padx=50, pady=50)
    entPai.grid(row=1, column=1)
    entMae.grid(row=2, column=1)
    entIdade.grid(row=3, column=1)
    entEndereco.grid(row=4, column=1)
    listaPessoas.grid(row=0, column=2, rowspan=10)
    scrollPessoas.grid(row=0, column=6, rowspan=10)
    btnVerTodos.grid(row=5, column=0, columnspan=2)
    btnBuscar.grid(row=6, column=0, columnspan=2)
    btnInserir.grid(row=7, column=0, columnspan=2)
    btnAtualizar.grid(row=8, column=0, columnspan=2)
    btnDel.grid(row=9, column=0, columnspan=2)
    btnClose.grid(row=10, column=0, columnspan=2)

    #Associar a Scrollbar com o Listbox
    listaPessoas.configure(yscrollcommand=scrollPessoas.set)
    scrollPessoas.configure(command=listaPessoas.yview)

    x_pad = 5
    y_pad = 3
    width_entry = 30

    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == 'Button':
            child.grid_configure(sticky='WE',padx=x_pad,pady=y_pad)
        elif widget_class == 'Listbox':
            child.grid_configure(sticky='NS',padx=0,pady=0)
        elif widget_class == 'Scrollbar':
            child.grid_configure(sticky='NS',padx=0,pady=0)
        else:
            child.grid_configure(sticky='N',padx=0,pady=0)

    def run(self):
        Gui.window.mainloop()
    
