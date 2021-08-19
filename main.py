# imports
import csv
import pandas as pd
from tkinter import *
from tkinter import ttk

# inicialização do estilo e variáveis principais


def get_livros():
    with open('livros.csv', 'r', encoding='UTF-8', errors='ignore') as csv_file:
        livros = csv.reader(csv_file)

        next(livros)

        return [row for row in livros if row]


def get_autores():
    with open('autores.csv', 'r', encoding='UTF-8', errors='ignore') as csv_file:
        autores = csv.reader(csv_file)

        next(autores)

        return [row for row in autores if row]


def get_editoras():
    with open('editoras.csv', 'r', encoding='UTF-8', errors='ignore') as csv_file:
        editoras = csv.reader(csv_file)

        next(editoras)

        return [row for row in editoras if row]


def add_livro(titulo, autor, editora, n_paginas, proprietario):
    with open('livros.csv', 'a', encoding='UTF-8', errors='ignore') as csv_file:
        writer = csv.writer(csv_file)

        id_livro = int(open('ultimo_id_livros.txt', 'r').readline()) + 1
        dados = [id_livro, titulo, autor, editora, n_paginas, proprietario]

        writer.writerow(dados)

        f = open('ultimo_id_livros.txt', 'w')
        f.truncate()
        f.write(str(id_livro))

    with open('autores.csv', 'r+', encoding='UTF-8', errors='ignore') as csv_file:
        autores = [x[1] for x in csv.reader(csv_file) if x]

        if autor not in autores:
            add_autor(autor)

    with open('editoras.csv', 'r+', encoding='UTF-8', errors='ignore') as csv_file:
        editoras = [x[1] for x in csv.reader(csv_file) if x]

        if editora not in editoras:
            add_editora(editora)


def add_autor(autor):
    with open('autores.csv', 'a', encoding='UTF-8', errors='ignore') as csv_file:
        writer = csv.writer(csv_file)

        id_autor = int(open('ultimo_id_autores.txt', 'r').readline()) + 1
        dados = [id_autor, autor]

        writer.writerow(dados)

        f = open('ultimo_id_autores.txt', 'w')
        f.truncate()
        f.write(str(id_autor))


def add_editora(editora):
    with open('editoras.csv', 'a', encoding='UTF-8', errors='ignore') as csv_file:
        writer = csv.writer(csv_file)

        id_editora = int(open('ultimo_id_editoras.txt', 'r').readline()) + 1
        dados = [id_editora, editora]

        writer.writerow(dados)

        f = open('ultimo_id_editoras.txt', 'w')
        f.truncate()
        f.write(str(id_editora))


def carrega_tabelas():
    livros = get_livros()
    autores = get_autores()
    editoras = get_editoras()

    for livro in tabela_livros.get_children():
        tabela_livros.delete(livro)

    for autor in tabela_autores.get_children():
        tabela_autores.delete(autor)

    for editora in tabela_editoras.get_children():
        tabela_editoras.delete(editora)

    count = 0

    for livro in livros:
        id = livro[0]
        titulo = livro[1]
        autor = livro[2]
        editora = livro[3]
        n_paginas = livro[4]
        proprietario = livro[5]

        if count % 2 == 0:

            tabela_livros.insert('', END, values=(
                id, titulo, autor, editora, n_paginas, proprietario), tags=('evenrow',))

        else:
            tabela_livros.insert('', END, values=(
                id, titulo, autor, editora, n_paginas, proprietario), tags=('oddrow',))

        count += 1

    count = 0

    for autor in autores:
        id = autor[0]
        nome = autor[1]

        if count % 2 == 0:
            tabela_autores.insert('', END, values=(
                id, nome), tags=('evenrow',))
        else:
            tabela_autores.insert('', END, values=(id, nome), tags=('oddrow',))

        count += 1

    count = 0

    for editora in editoras:
        id = editora[0]
        nome = editora[1]

        if count % 2 == 0:
            tabela_editoras.insert(
                '', END, values=(id, nome), tags=('evenrow'))
        else:
            tabela_editoras.insert(
                '', END, values=(id, nome), tags=('oddrow',))

        count += 1


def mudar_tabela(event):
    livro_register_frame.pack_forget()
    autor_register_frame.pack_forget()
    editora_register_frame.pack_forget()
    button_register_frame.pack_forget()
    editar_excluir_livro.pack_forget()
    botoes_editar_excluir_livro.pack_forget()
    editar_excluir_autor.pack_forget()
    botoes_editar_excluir_autor.pack_forget()
    editar_excluir_editora.pack_forget()
    botoes_editar_excluir_editora.pack_forget()

    if drop_down.get() == 'Livros':
        tabela_autores.pack_forget()
        tabela_editoras.pack_forget()

        table_frame['text'] = 'Livros'

        tabela_livros.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

    elif drop_down.get() == 'Autores':
        tabela_livros.pack_forget()
        tabela_editoras.pack_forget()

        table_frame['text'] = 'Autores'

        tabela_autores.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

    elif drop_down.get() == 'Editoras':
        tabela_livros.pack_forget()
        tabela_autores.pack_forget()

        table_frame['text'] = 'Editoras'

        tabela_editoras.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )


def adicionar_novo():
    table_frame['text'] = 'Novo Livro'

    tabela_livros.pack_forget()
    tabela_autores.pack_forget()
    tabela_editoras.pack_forget()
    editar_excluir_livro.pack_forget()
    botoes_editar_excluir_livro.pack_forget()
    editar_excluir_autor.pack_forget()
    botoes_editar_excluir_autor.pack_forget()
    editar_excluir_editora.pack_forget()
    botoes_editar_excluir_editora.pack_forget()

    livro_register_frame.pack(
        expand=True,
        fill=BOTH,
        padx=10,
        pady=10,
        anchor=N
    )

    button_register_frame.pack(
        expand=False,
        fill=X,
        padx=10,
        pady=10,
        anchor=S
    )


def cancelar_registro():
    table_frame['text'] = 'Livros'

    if drop_down_register.get() == 'Livro':
        livro_register_frame.pack_forget()

        titulo_entry_registro_livro.delete(0, END)
        autor_entry_registro_livro.delete(0, END)
        editora_entry_registro_livro.delete(0, END)
        n_pages_entry_registro_livro.delete(0, END)
        proprietario_entry_registro_livro.delete(0, END)

    elif drop_down_register.get() == 'Autor':
        autor_register_frame.pack_forget()

        autor_entry_registro_autor.delete(0, END)

    elif drop_down_register.get() == 'Editora':
        editora_register_frame.pack_forget()

        editora_entry_registro_editora.delete(0, END)

    button_register_frame.pack_forget()

    tabela_livros.pack(
        expand=True,
        fill=BOTH,
        padx=10,
        pady=10
    )

    drop_down_register.current(0)


def mudar_tela_registro(event):
    button_register_frame.pack_forget()

    if drop_down_register.get() == 'Livro':
        table_frame['text'] = 'Novo Livro'

        autor_register_frame.pack_forget()
        editora_register_frame.pack_forget()

        livro_register_frame.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10,
            anchor=N
        )

    elif drop_down_register.get() == 'Autor':
        table_frame['text'] = 'Novo Autor'

        livro_register_frame.pack_forget()
        editora_register_frame.pack_forget()

        autor_register_frame.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10,
            anchor=N
        )

    elif drop_down_register.get() == 'Editora':
        table_frame['text'] = 'Nova Editora'

        livro_register_frame.pack_forget()
        autor_register_frame.pack_forget()

        editora_register_frame.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10,
            anchor=N
        )

    button_register_frame.pack(
        expand=False,
        fill=X,
        padx=10,
        pady=10,
        anchor=S
    )


def adicionar_registro():
    if drop_down_register.get() == 'Livro':
        titulo = titulo_entry_registro_livro.get()
        autor = autor_entry_registro_livro.get()
        editora = editora_entry_registro_livro.get()
        n_pages = n_pages_entry_registro_livro.get()
        proprietario = proprietario_entry_registro_livro.get()

        add_livro(titulo, autor, editora, n_pages, proprietario)

        titulo_entry_registro_livro.delete(0, END)
        autor_entry_registro_livro.delete(0, END)
        editora_entry_registro_livro.delete(0, END)
        n_pages_entry_registro_livro.delete(0, END)
        proprietario_entry_registro_livro.delete(0, END)

    elif drop_down_register.get() == 'Autor':
        autor = autor_entry_registro_autor.get()

        add_autor(autor)

        autor_entry_registro_autor.delete(0, END)

    elif drop_down_register.get() == 'Editora':
        editora = editora_entry_registro_editora.get()

        add_editora(editora)

        editora_entry_registro_editora.delete(0, END)

    carrega_tabelas()

    cancelar_registro()


def selecionar_livro(event):
    table_frame['text'] = 'Editar/Excluir Livro'

    tabela_livros.pack_forget()

    titulo_entry_editar_excluir_livro.delete(0, END)
    autor_entry_editar_excluir_livro.delete(0, END)
    editora_entry_editar_excluir_livro.delete(0, END)
    n_pages_entry_editar_excluir_livro.delete(0, END)
    proprietario_entry_editar_excluir_livro.delete(0, END)

    editar_excluir_livro.pack(
        expand=True,
        fill=BOTH,
        padx=10,
        pady=10,
        anchor=N
    )

    botoes_editar_excluir_livro.pack(
        expand=False,
        fill=X,
        padx=10,
        pady=10,
        anchor=S
    )

    livro_selecionado = tabela_livros.item(tabela_livros.focus())['values']

    titulo_entry_editar_excluir_livro.insert(0, livro_selecionado[1])
    autor_entry_editar_excluir_livro.insert(0, livro_selecionado[2])
    editora_entry_editar_excluir_livro.insert(0, livro_selecionado[3])
    n_pages_entry_editar_excluir_livro.insert(0, livro_selecionado[4])
    proprietario_entry_editar_excluir_livro.insert(0, livro_selecionado[5])


def selecionar_autor(event):
    table_frame['text'] = 'Editar/Excluir Autor'

    tabela_autores.pack_forget()

    autor_entry_editar_excluir_autor.delete(0, END)

    editar_excluir_autor.pack(
        expand=True,
        fill=BOTH,
        padx=10,
        pady=10,
        anchor=N
    )

    botoes_editar_excluir_autor.pack(
        expand=False,
        fill=X,
        padx=10,
        pady=10,
        anchor=S
    )

    autor_selecionado = tabela_autores.item(tabela_autores.focus())['values']

    autor_entry_editar_excluir_autor.insert(0, autor_selecionado[1])


def selecionar_editora(event):
    table_frame['text'] = 'Editar/Excluir Editora'

    tabela_editoras.pack_forget()

    editora_entry_editar_excluir_editora.delete(0, END)

    editar_excluir_editora.pack(
        expand=True,
        fill=BOTH,
        padx=10,
        pady=10,
        anchor=N
    )

    botoes_editar_excluir_editora.pack(
        expand=False,
        fill=X,
        padx=10,
        pady=10,
        anchor=S
    )

    editora_selecionada = tabela_editoras.item(
        tabela_editoras.focus())['values']

    editora_entry_editar_excluir_editora.insert(0, editora_selecionada[1])


def editar_livro():
    livro_selecionado = tabela_livros.item(tabela_livros.focus())['values']

    id_livro = livro_selecionado[0]

    df = pd.read_csv('livros.csv')

    df.loc[id_livro - 1, 'titulo'] = titulo_entry_editar_excluir_livro.get()
    df.loc[id_livro - 1, 'autor'] = autor_entry_editar_excluir_livro.get()
    df.loc[id_livro - 1, 'editora'] = editora_entry_editar_excluir_livro.get()
    df.loc[id_livro - 1, 'n_paginas'] = n_pages_entry_editar_excluir_livro.get()
    df.loc[id_livro - 1, 'proprietario'] = proprietario_entry_editar_excluir_livro.get()

    df.to_csv('livros.csv', index=False)

    cancelar_edicao_livro()

    carrega_tabelas()


def cancelar_edicao_livro():
    editar_excluir_livro.pack_forget()
    botoes_editar_excluir_livro.pack_forget()

    table_frame['text'] = 'Livros'

    tabela_livros.pack(
        expand=True,
        fill=BOTH,
        padx=10,
        pady=10
    )


def excluir_livro():
    pass


def editar_autor():
    autor_selecionado = tabela_autores.item(tabela_autores.focus())['values']

    id_autor = autor_selecionado[0]

    df = pd.read_csv('autores.csv')

    df.loc[id_autor - 1, 'autor'] = autor_entry_editar_excluir_autor.get()

    df.to_csv('autores.csv', index=False)

    cancelar_edicao_autor()

    carrega_tabelas()


def cancelar_edicao_autor():
    editar_excluir_autor.pack_forget()
    botoes_editar_excluir_autor.pack_forget()

    table_frame['text'] = 'Livros'

    tabela_livros.pack(
        expand=True,
        fill=BOTH,
        padx=10,
        pady=10
    )


def editar_editora():
    editora_selecionada = tabela_editoras.item(
        tabela_editoras.focus())['values']

    id_editora = editora_selecionada[0]

    df = pd.read_csv('editoras.csv')

    df.loc[id_editora - 1, 'editora'] = editora_entry_editar_excluir_editora.get()

    df.to_csv('editoras.csv', index=False)

    cancelar_edicao_editora()

    carrega_tabelas()


def cancelar_edicao_editora():
    editar_excluir_editora.pack_forget()
    botoes_editar_excluir_editora.pack_forget()

    table_frame['text'] = 'Livros'

    tabela_livros.pack(
        expand=True,
        fill=BOTH,
        padx=10,
        pady=10
    )


root = Tk()
root.title('Livraria')
root.geometry('500x500')

style = ttk.Style()
style.theme_use('default')
style.configure(
    'Treeview',
    background='white',
    foreground='black',
    fieldbackground='#D3D3D3'
)
style.map(
    'Treeview',
    background=[('selected', '#347083')]
)

# criação do frame responsável por conter as tabelas e criação das tabelas
table_frame = LabelFrame(
    root,
    text='Livros'
)
table_frame.pack(
    expand=True,
    fill=BOTH,
    padx=10,
    pady=10
)

# criação do scrool lateral
tree_scrool = Scrollbar(table_frame)
tree_scrool.pack(
    side=RIGHT,
    fill=Y
)

# criação da tabela livros
tabela_livros = ttk.Treeview(
    table_frame,
    yscrollcommand=tree_scrool.set,
    selectmode=EXTENDED
)
tabela_livros.pack(
    expand=True,
    fill=BOTH,
    padx=10,
    pady=10
)

tree_scrool.config(command=tabela_livros.yview)

tabela_livros['columns'] = ('id', 'titulo', 'autor', 'editora',
                            'n_paginas', 'proprietario')
tabela_livros.column('#0', width=0, stretch=NO)

tabela_livros.column('id', anchor=CENTER, width=100)
tabela_livros.column('titulo', anchor=W, width=140)
tabela_livros.column('autor', anchor=W, width=140)
tabela_livros.column('editora', anchor=W, width=140)
tabela_livros.column('n_paginas', anchor=CENTER, width=100)
tabela_livros.column('proprietario', anchor=W, width=140)

tabela_livros.heading('#0', text='', anchor=W)
tabela_livros.heading('id', text='ID', anchor=CENTER)
tabela_livros.heading('titulo', text='Título', anchor=W)
tabela_livros.heading('autor', text='Autor(a)', anchor=W)
tabela_livros.heading('editora', text='Editora', anchor=W)
tabela_livros.heading('n_paginas', text='Nº Páginas', anchor=CENTER)
tabela_livros.heading('proprietario', text='Proprietário(a)', anchor=W)

tabela_livros.tag_configure('oddrow', background='white')
tabela_livros.tag_configure('evenrow', background='lightblue')

tabela_livros.bind('<ButtonRelease-1>', selecionar_livro)

# criação da tabela autores
tabela_autores = ttk.Treeview(
    table_frame,
    yscrollcommand=tree_scrool.set,
    selectmode=EXTENDED,
    columns=('id', 'autor')
)

tabela_autores.column('#0', width=0, stretch=NO)
tabela_autores.column('id', anchor=CENTER, width=100)
tabela_autores.column('autor', anchor=W, width=140)

tabela_autores.heading('#0', text='', anchor=W)
tabela_autores.heading('id', text='ID', anchor=CENTER)
tabela_autores.heading('autor', text='Autor', anchor=W)

tabela_autores.tag_configure('oddrow', background='white')
tabela_autores.tag_configure('evenrow', background='lightblue')

tabela_autores.bind('<ButtonRelease-1>', selecionar_autor)

# criação da tabela editoras
tabela_editoras = ttk.Treeview(
    table_frame,
    yscrollcommand=tree_scrool.set,
    selectmode=EXTENDED,
    columns=('id', 'editora')
)

tabela_editoras.column('#0', width=0, stretch=NO)
tabela_editoras.column('id', anchor=CENTER, width=100)
tabela_editoras.column('editora', anchor=W, width=140)

tabela_editoras.heading('#0', text='', anchor=W)
tabela_editoras.heading('id', text='ID', anchor=CENTER)
tabela_editoras.heading('editora', text='Editora', anchor=W)

tabela_editoras.tag_configure('oddrow', background='white')
tabela_editoras.tag_configure('evenrow', background='lightblue')

tabela_editoras.bind('<ButtonRelease-1>', selecionar_editora)

carrega_tabelas()

# frame responsável pela tela de registro dos livros
livro_register_frame = Frame(
    table_frame
)

livro_register_frame.columnconfigure(1, weight=1)

titulo_label_registro_livro = Label(
    livro_register_frame,
    text='Titulo'
)
titulo_label_registro_livro.grid(row=0, column=0, padx=10, pady=10)

titulo_entry_registro_livro = Entry(
    livro_register_frame
)
titulo_entry_registro_livro.grid(row=0, column=1, padx=10, pady=10, sticky=EW)

autor_label_registro_livro = Label(
    livro_register_frame,
    text='Autor'
)
autor_label_registro_livro.grid(row=1, column=0, padx=10, pady=10)

autor_entry_registro_livro = Entry(
    livro_register_frame
)
autor_entry_registro_livro.grid(row=1, column=1, padx=10, pady=10, sticky=EW)

editora_label_registro_livro = Label(
    livro_register_frame,
    text='Editora'
)
editora_label_registro_livro.grid(row=2, column=0, padx=10, pady=10)

editora_entry_registro_livro = Entry(
    livro_register_frame
)
editora_entry_registro_livro.grid(row=2, column=1, padx=10, pady=10, sticky=EW)

n_pages_label_registro_livro = Label(
    livro_register_frame,
    text='Nº Páginas'
)
n_pages_label_registro_livro.grid(row=3, column=0, padx=10, pady=10)

n_pages_entry_registro_livro = Entry(
    livro_register_frame
)
n_pages_entry_registro_livro.grid(row=3, column=1, padx=10, pady=10, sticky=EW)

proprietario_label_registro_livro = Label(
    livro_register_frame,
    text='Proprietário'
)
proprietario_label_registro_livro.grid(row=4, column=0, padx=10, pady=10)

proprietario_entry_registro_livro = Entry(
    livro_register_frame
)
proprietario_entry_registro_livro.grid(
    row=4, column=1, padx=10, pady=10, sticky=EW)

# frame responsável pela tela de registro dos autores
autor_register_frame = Frame(
    table_frame
)

autor_register_frame.columnconfigure(1, weight=1)

autor_label_registro_autor = Label(
    autor_register_frame,
    text='Autor'
)
autor_label_registro_autor.grid(row=0, column=0, padx=10, pady=10)

autor_entry_registro_autor = Entry(
    autor_register_frame
)
autor_entry_registro_autor.grid(row=0, column=1, padx=10, pady=10, sticky=EW)

# frame responsável pela tela de registro das editoras
editora_register_frame = Label(
    table_frame
)

editora_register_frame.columnconfigure(1, weight=1)

editora_label_registro_editora = Label(
    editora_register_frame,
    text='Editora'
)
editora_label_registro_editora.grid(row=0, column=0, padx=10, pady=10)

editora_entry_registro_editora = Entry(
    editora_register_frame
)
editora_entry_registro_editora.grid(
    row=0, column=1, padx=10, pady=10, sticky=EW)

# comandos do livro_register_frame
button_register_frame = Frame(
    table_frame
)
button_register_frame.columnconfigure(0, weight=1)
button_register_frame.columnconfigure(1, weight=1)
button_register_frame.columnconfigure(2, weight=1)

button_add = Button(
    button_register_frame,
    text='Adicionar',
    relief=GROOVE,
    command=lambda: adicionar_registro()
)
button_add.grid(row=0, column=0, padx=10, pady=10, sticky=EW)

button_cancel = Button(
    button_register_frame,
    text='Cancelar',
    relief=GROOVE,
    command=lambda: cancelar_registro()
)
button_cancel.grid(row=0, column=1, padx=10, pady=10, sticky=EW)

drop_down_register = ttk.Combobox(
    button_register_frame,
    values=(
        'Livro',
        'Editora',
        'Autor'
    )
)
drop_down_register.current(0)
drop_down_register.bind('<<ComboboxSelected>>', mudar_tela_registro)
drop_down_register.grid(row=0, column=2, padx=10, pady=10, sticky=EW)

# criação do frame responsável por editar/excluir um livro
editar_excluir_livro = Frame(
    table_frame
)

editar_excluir_livro.columnconfigure(1, weight=1)

titulo_label_editar_excluir_livro = Label(
    editar_excluir_livro,
    text='Titulo'
)
titulo_label_editar_excluir_livro.grid(row=0, column=0, padx=10, pady=10)

titulo_entry_editar_excluir_livro = Entry(
    editar_excluir_livro
)
titulo_entry_editar_excluir_livro.grid(
    row=0, column=1, padx=10, pady=10, sticky=EW)

autor_label_editar_excluir_livro = Label(
    editar_excluir_livro,
    text='Autor'
)
autor_label_editar_excluir_livro.grid(row=1, column=0, padx=10, pady=10)

autor_entry_editar_excluir_livro = Entry(
    editar_excluir_livro
)
autor_entry_editar_excluir_livro.grid(
    row=1, column=1, padx=10, pady=10, sticky=EW)

editora_label_editar_excluir_livro = Label(
    editar_excluir_livro,
    text='Editora'
)
editora_label_editar_excluir_livro.grid(row=2, column=0, padx=10, pady=10)

editora_entry_editar_excluir_livro = Entry(
    editar_excluir_livro
)
editora_entry_editar_excluir_livro.grid(
    row=2, column=1, padx=10, pady=10, sticky=EW)

n_pages_label_editar_excluir_livro = Label(
    editar_excluir_livro,
    text='Nº Páginas'
)
n_pages_label_editar_excluir_livro.grid(row=3, column=0, padx=10, pady=10)

n_pages_entry_editar_excluir_livro = Entry(
    editar_excluir_livro
)
n_pages_entry_editar_excluir_livro.grid(
    row=3, column=1, padx=10, pady=10, sticky=EW)

proprietario_label_editar_excluir_livro = Label(
    editar_excluir_livro,
    text='Proprietário'
)
proprietario_label_editar_excluir_livro.grid(row=4, column=0, padx=10, pady=10)

proprietario_entry_editar_excluir_livro = Entry(
    editar_excluir_livro
)
proprietario_entry_editar_excluir_livro.grid(
    row=4, column=1, padx=10, pady=10, sticky=EW)

botoes_editar_excluir_livro = Frame(
    table_frame
)

botoes_editar_excluir_livro.columnconfigure(0, weight=1)
botoes_editar_excluir_livro.columnconfigure(1, weight=1)
botoes_editar_excluir_livro.columnconfigure(2, weight=1)

botao_editar_livro = Button(
    botoes_editar_excluir_livro,
    text='Editar',
    relief=GROOVE,
    command=lambda: editar_livro()
)
botao_editar_livro.grid(row=0, column=0, padx=10, pady=10, sticky=EW)

botao_excluir_livro = Button(
    botoes_editar_excluir_livro,
    text='Excluir',
    relief=GROOVE
)
botao_excluir_livro.grid(row=0, column=1, padx=10, pady=10, sticky=EW)

botao_cancelar_edicao_livro = Button(
    botoes_editar_excluir_livro,
    text='Cancelar',
    relief=GROOVE,
    command=lambda: cancelar_edicao_livro()
)
botao_cancelar_edicao_livro.grid(row=0, column=2, padx=10, pady=10, sticky=EW)

editar_excluir_autor = Frame(
    table_frame
)

editar_excluir_autor.columnconfigure(1, weight=1)

autor_label_editar_excluir_autor = Label(
    editar_excluir_autor,
    text='Autor'
)
autor_label_editar_excluir_autor.grid(row=0, column=0, padx=10, pady=10)

autor_entry_editar_excluir_autor = Entry(
    editar_excluir_autor
)
autor_entry_editar_excluir_autor.grid(
    row=0, column=1, padx=10, pady=10, sticky=EW)

botoes_editar_excluir_autor = Frame(
    table_frame
)

botoes_editar_excluir_autor.columnconfigure(0, weight=1)
botoes_editar_excluir_autor.columnconfigure(1, weight=1)
botoes_editar_excluir_autor.columnconfigure(2, weight=1)

botao_editar_autor = Button(
    botoes_editar_excluir_autor,
    text='Editar',
    relief=GROOVE,
    command=lambda: editar_autor()
)
botao_editar_autor.grid(row=0, column=0, padx=10, pady=10, sticky=EW)

botao_excluir_autor = Button(
    botoes_editar_excluir_autor,
    text='Excluir',
    relief=GROOVE
)
botao_excluir_autor.grid(row=0, column=1, padx=10, pady=10, sticky=EW)

botao_cancelar_edicao_autor = Button(
    botoes_editar_excluir_autor,
    text='Cancelar',
    relief=GROOVE,
    command=lambda: cancelar_edicao_autor()
)
botao_cancelar_edicao_autor.grid(row=0, column=2, padx=10, pady=10, sticky=EW)

editar_excluir_editora = Frame(
    table_frame
)

editar_excluir_editora.columnconfigure(1, weight=1)

editora_label_editar_excluir_editora = Label(
    editar_excluir_editora,
    text='Editora'
)
editora_label_editar_excluir_editora.grid(row=0, column=0, padx=10, pady=10)

editora_entry_editar_excluir_editora = Entry(
    editar_excluir_editora
)
editora_entry_editar_excluir_editora.grid(
    row=0, column=1, padx=10, pady=10, sticky=EW)

botoes_editar_excluir_editora = Frame(
    table_frame
)

botoes_editar_excluir_editora.columnconfigure(0, weight=1)
botoes_editar_excluir_editora.columnconfigure(1, weight=1)
botoes_editar_excluir_editora.columnconfigure(2, weight=1)

botao_editar_editora = Button(
    botoes_editar_excluir_editora,
    text='Editar',
    relief=GROOVE,
    command=lambda: editar_editora()
)
botao_editar_editora.grid(row=0, column=0, padx=10, pady=10, sticky=EW)

botao_excluir_editora = Button(
    botoes_editar_excluir_editora,
    text='Excluir',
    relief=GROOVE
)
botao_excluir_editora.grid(row=0, column=1, padx=10, pady=10, sticky=EW)

botao_cancelar_edicao_editora = Button(
    botoes_editar_excluir_editora,
    text='Cancelar',
    relief=GROOVE,
    command=lambda: cancelar_edicao_editora()
)
botao_cancelar_edicao_editora.grid(
    row=0, column=2, padx=10, pady=10, sticky=EW)


# criação do label frame responsável por gerenciar os botões de comandos
button_frame = LabelFrame(
    root,
    text='Comandos',
)
button_frame.pack(
    fill=X,
    expand=False,
    pady=10,
    padx=10,
    anchor=S
)

add_new = Button(
    button_frame,
    text='Novo',
    relief=GROOVE,
    command=lambda: adicionar_novo()
)

add_new.grid(
    row=0,
    column=0,
    padx=10,
    pady=10
)

drop_down = ttk.Combobox(
    button_frame,
    values=(
        'Livros',
        'Autores',
        'Editoras'
    )
)
drop_down.current(0)
drop_down.bind('<<ComboboxSelected>>', mudar_tabela)
drop_down.grid(
    row=0,
    column=1,
    padx=10,
    pady=10
)

root.mainloop()
