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
        drop_down, table_frame, books_table, authors_table, publishing_companys_table, fields_register_frame, label_titulo, entry_titulo, label_autor, entry_autor, label_editora, entry_editora, label_n_pages, entry_n_pages, label_proprietario, entry_proprietario, button_register_frame, button_adicionar, button_cancelar)


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
books_table = ttk.Treeview(
    table_frame,
    yscrollcommand=tree_scrool.set,
    selectmode=EXTENDED
)
books_table.pack(
    expand=True,
    fill=BOTH,
    padx=10,
    pady=10
)

tree_scrool.config(command=books_table.yview)

books_table['columns'] = ('id', 'titulo', 'autor', 'editora',
                          'n_paginas', 'proprietario')
books_table.column('#0', width=0, stretch=NO)

books_table.column('id', anchor=CENTER, width=100)
books_table.column('titulo', anchor=W, width=140)
books_table.column('autor', anchor=W, width=140)
books_table.column('editora', anchor=W, width=140)
books_table.column('n_paginas', anchor=CENTER, width=100)
books_table.column('proprietario', anchor=W, width=140)

books_table.heading('#0', text='', anchor=W)
books_table.heading('id', text='ID', anchor=CENTER)
books_table.heading('titulo', text='Título', anchor=W)
books_table.heading('autor', text='Autor(a)', anchor=W)
books_table.heading('editora', text='Editora', anchor=W)
books_table.heading('n_paginas', text='Nº Páginas', anchor=CENTER)
books_table.heading('proprietario', text='Proprietário(a)', anchor=W)

books_table.tag_configure('oddrow', background='white')
books_table.tag_configure('evenrow', background='lightblue')

livros = data_base.get_books()
for livro in livros:
    id = livro[0]
    titulo = livro[1]
    autor = livro[2]
    editora = livro[3]
    n_paginas = livro[4]
    proprietario = livro[5]

    if id % 2 == 0:
        books_table.insert(parent='', index=END, iid=id, text='', values=(
            id,
            titulo,
            autor,
            editora,
            n_paginas,
            proprietario
        ), tags='evenrow')
    else:
        books_table.insert(parent='', index=END, iid=id, text='', values=(
            id,
            titulo,
            autor,
            editora,
            n_paginas,
            proprietario
        ), tags='oddrow')

# criação da tabela autores
authors_table = ttk.Treeview(
    table_frame,
    yscrollcommand=tree_scrool.set,
    selectmode=EXTENDED,
    columns=('id', 'autor')
)

authors_table.column('#0', width=0, stretch=NO)
authors_table.column('id', anchor=CENTER, width=100)
authors_table.column('autor', anchor=W, width=140)

authors_table.heading('#0', text='', anchor=W)
authors_table.heading('id', text='ID', anchor=CENTER)
authors_table.heading('autor', text='Autor', anchor=W)

authors_table.tag_configure('oddrow', background='white')
authors_table.tag_configure('evenrow', background='lightblue')

autores = data_base.get_authors()

for autor in autores:
    id = autor[0]
    nome = autor[1]

    if id % 2 == 0:
        authors_table.insert(parent='', index=END, iid=id, text='', values=(
            id,
            nome
        ), tags='evenrow')

    else:
        authors_table.insert(parent='', index=END, iid=id, text='', values=(
            id,
            nome
        ), tags='oddrow')


# criação da tabela editoras
publishing_companys_table = ttk.Treeview(
    table_frame,
    yscrollcommand=tree_scrool.set,
    selectmode=EXTENDED,
    columns=('id', 'editora')
)

publishing_companys_table.column('#0', width=0, stretch=NO)
publishing_companys_table.column('id', anchor=CENTER, width=100)
publishing_companys_table.column('editora', anchor=W, width=140)

publishing_companys_table.heading('#0', text='', anchor=W)
publishing_companys_table.heading('id', text='ID', anchor=CENTER)
publishing_companys_table.heading('editora', text='Editora', anchor=W)

publishing_companys_table.tag_configure('oddrow', background='white')
publishing_companys_table.tag_configure('evenrow', background='lightblue')

editoras = data_base.get_publishing_companys()

for editora in editoras:
    id = editora[0]
    nome = editora[1]

    if id % 2 == 0:
        publishing_companys_table.insert(parent='', index=END, iid=id, values=(
            id,
            nome
        ), tags='evenrow')

    else:
        publishing_companys_table.insert(parent='', index=END, iid=id, values=(
            id,
            nome
        ), tags='oddrow')

fields_register_frame = Frame(
    table_frame
)

label_titulo = Label(
    fields_register_frame,
    text='Titulo'
)
entry_titulo = Entry(
    fields_register_frame
)

label_autor = Label(
    fields_register_frame,
    text='Autor'
)
entry_autor = Entry(
    fields_register_frame
)

label_editora = Label(
    fields_register_frame,
    text='Editora'
)
entry_editora = Entry(
    fields_register_frame
)

label_n_pages = Label(
    fields_register_frame,
    text='Nº de Páginas'
)
entry_n_pages = Entry(
    fields_register_frame
)

label_proprietario = Label(
    fields_register_frame,
    text='Proprietário'
)
entry_proprietario = Entry(
    fields_register_frame
)

button_register_frame = Frame(
    table_frame
)

button_adicionar = Button(
    button_register_frame,
    text='Adicionar'
)

button_cancelar = Button(
    button_register_frame,
    text='Cancelar'
)

# criação do label responsável por gerenciar os botões de comandos
button_frame = LabelFrame(
    root,
    text='Comandos'
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
    command=lambda: button_actions.adicionar(
        table_frame, books_table, authors_table, publishing_companys_table, fields_register_frame, label_titulo, entry_titulo, label_autor, entry_autor, label_editora, entry_editora, label_n_pages, entry_n_pages, label_proprietario, entry_proprietario, button_register_frame, button_adicionar, button_cancelar)
)
add_new.grid(
    row=0,
    column=0,
    padx=10,
    pady=10
)

update_button = Button(
    button_frame,
    text='Atualizar Dado Selecionado'
)
update_button.grid(
    row=0,
    column=1,
    padx=10,
    pady=10
)

remove_one_button = Button(
    button_frame,
    text='Deletar Dado Selecionado'
)
remove_one_button.grid(
    row=0,
    column=2,
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
    column=3,
    padx=10,
    pady=10
)

root.mainloop()
