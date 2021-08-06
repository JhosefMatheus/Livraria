# imports
from DBHelper import DBHelper
from tkinter import *
from tkinter import ttk
from ButtonActions import ButtonActions

# inicialização do estilo e variáveis principais
data_base = DBHelper()
button_actions = ButtonActions()


def change_table(event):
    button_actions.change_table(
        drop_down, livro_register_frame, button_register_frame, table_frame, tabela_livros, tabela_autores, tabela_editoras)


def change_register_frame(event):
    button_actions.change_register_frame(
        drop_down_register, table_frame, livro_register_frame, autor_register_frame, editora_register_frame, button_register_frame)


root = Tk()
root.title('Livraria')
root.geometry('500x500')

style = ttk.Style()
style.theme_use('default')
style.configure(
    'Treeview',
    background='#D3D3D3',
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

livros = data_base.get_livros()
for livro in livros:
    id = livro[0]
    titulo = livro[1]
    autor = livro[2]
    editora = livro[3]
    n_paginas = livro[4]
    proprietario = livro[5]

    if id % 2 == 0:
        tabela_livros.insert(parent='', index=END, iid=id, text='', values=(
            id,
            titulo,
            autor,
            editora,
            n_paginas,
            proprietario
        ), tags='evenrow')
    else:
        tabela_livros.insert(parent='', index=END, iid=id, text='', values=(
            id,
            titulo,
            autor,
            editora,
            n_paginas,
            proprietario
        ), tags='oddrow')

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

autores = data_base.get_authores()

for autor in autores:
    id = autor[0]
    nome = autor[1]

    if id % 2 == 0:
        tabela_autores.insert(parent='', index=END, iid=id, text='', values=(
            id,
            nome
        ), tags='evenrow')

    else:
        tabela_autores.insert(parent='', index=END, iid=id, text='', values=(
            id,
            nome
        ), tags='oddrow')


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

editoras = data_base.get_editoras()

for editora in editoras:
    id = editora[0]
    nome = editora[1]

    if id % 2 == 0:
        tabela_editoras.insert(parent='', index=END, iid=id, values=(
            id,
            nome
        ), tags='evenrow')

    else:
        tabela_editoras.insert(parent='', index=END, iid=id, values=(
            id,
            nome
        ), tags='oddrow')

# frame responsável pela tela de registro dos livros
livro_register_frame = Frame(
    table_frame
)

livro_register_frame.columnconfigure(1, weight=1)

titulo_label = Label(
    livro_register_frame,
    text='Titulo'
)
titulo_label.grid(row=0, column=0, padx=10, pady=10)

titulo_entry = Entry(
    livro_register_frame
)
titulo_entry.grid(row=0, column=1, padx=10, pady=10, sticky=EW)

autor_label = Label(
    livro_register_frame,
    text='Autor'
)
autor_label.grid(row=1, column=0, padx=10, pady=10)

autor_entry = Entry(
    livro_register_frame
)
autor_entry.grid(row=1, column=1, padx=10, pady=10, sticky=EW)

editora_label = Label(
    livro_register_frame,
    text='Editora'
)
editora_label.grid(row=2, column=0, padx=10, pady=10)

editora_entry = Entry(
    livro_register_frame
)
editora_entry.grid(row=2, column=1, padx=10, pady=10, sticky=EW)

n_pages_label = Label(
    livro_register_frame,
    text='Nº Páginas'
)
n_pages_label.grid(row=3, column=0, padx=10, pady=10)

n_pages_entry = Entry(
    livro_register_frame
)
n_pages_entry.grid(row=3, column=1, padx=10, pady=10, sticky=EW)

proprietario_label = Label(
    livro_register_frame,
    text='Nº Páginas'
)
proprietario_label.grid(row=4, column=0, padx=10, pady=10)

proprietario_entry = Entry(
    livro_register_frame
)
proprietario_entry.grid(row=4, column=1, padx=10, pady=10, sticky=EW)

# frame responsável pela tela de registro dos autores
autor_register_frame = Frame(
    table_frame
)

autor_register_frame.columnconfigure(1, weight=1)

nome_autor_label = Label(
    autor_register_frame,
    text='Autor'
)
nome_autor_label.grid(row=0, column=0, padx=10, pady=10)

nome_autor_entry = Entry(
    autor_register_frame
)
nome_autor_entry.grid(row=0, column=1, padx=10, pady=10, sticky=EW)

# frame responsável pela tela de registro das editoras
editora_register_frame = Label(
    table_frame
)

editora_register_frame.columnconfigure(1, weight=1)

nome_editora_label = Label(
    editora_register_frame,
    text='Editora'
)
nome_editora_label.grid(row=0, column=0, padx=10, pady=10)

nome_editora_entry = Entry(
    editora_register_frame
)
nome_editora_entry.grid(row=0, column=1, padx=10, pady=10, sticky=EW)

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
    command=''
)
button_add.grid(row=0, column=0, padx=10, pady=10, sticky=EW)

button_cancel = Button(
    button_register_frame,
    text='Cancelar',
    relief=GROOVE,
    command=lambda: button_actions.cancel_register_click(
        table_frame, drop_down_register, livro_register_frame, autor_register_frame, editora_register_frame, button_register_frame, tabela_livros)
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
drop_down_register.bind('<<ComboboxSelected>>', change_register_frame)
drop_down_register.grid(row=0, column=2, padx=10, pady=10, sticky=EW)

# criação do label responsável por gerenciar os botões de comandos
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
    command=lambda: button_actions.add_click(
        table_frame, tabela_livros, tabela_autores, tabela_editoras, livro_register_frame, button_register_frame)
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
drop_down.bind('<<ComboboxSelected>>', change_table)
drop_down.grid(
    row=0,
    column=1,
    padx=10,
    pady=10
)

root.mainloop()
