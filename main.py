# imports
from DBHelper import DBHelper
from tkinter import *
from tkinter import ttk
from ButtonActions import ButtonActions

# inicialização do estilo e variáveis principais
data_base = DBHelper()
button_actions = ButtonActions()

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
tree_frame = Frame(root)
tree_frame.pack(pady=10, padx=10, expand=True, fill=BOTH, anchor=N)

# criação do scrool lateral
tree_scrool = Scrollbar(tree_frame)
tree_scrool.pack(side=RIGHT, fill=Y)

# criação da tabela livros
books_table = ttk.Treeview(
    tree_frame, yscrollcommand=tree_scrool.set, selectmode='extended')
books_table.pack(expand=True, fill=BOTH)

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

# criação da tabela autores
authors_table = ttk.Treeview(
    tree_frame,
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

# criação da tabela editoras
publishing_companys_table = ttk.Treeview(
    tree_frame,
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

# for livro in livros:
#     id = livro[0]
#     titulo = livro[1]
#     autor = livro[2]
#     editora = livro[3]
#     n_pags = livro[4]
#     proprietario = livro[5]

#     if (id % 2 == 0):
#         books_table.insert(parent='', index='end', values=(
#             id, titulo, autor, editora, n_pags, proprietario), tags=('evenrow',))
#     else:
#         books_table.insert(parent='', index='end', values=(
#             id, titulo, autor, editora, n_pags, proprietario), tags=('oddrow',))

# criação do frame responsável por adicionar ou editar registros
data_frame = LabelFrame(
    root,
    text='Adicionar/Editar'
)
data_frame.pack(expand=True, fill=BOTH, padx=10, pady=10, anchor=N)

# criação dos labels e entradas responsáveis por adicionar ou editar registros
title_book_label = Label(data_frame, text='Título')
title_book_label.grid(row=0, column=0, padx=10, pady=10)
title_book_entry = Entry(data_frame)
title_book_entry.grid(row=0, column=1, padx=10, pady=10)

author_book_label = Label(data_frame, text='Autor')
author_book_label.grid(row=0, column=2, padx=10, pady=10)
author_book_entry = Entry(data_frame)
author_book_entry.grid(row=0, column=3, padx=10, pady=10)

publishing_company_label = Label(data_frame, text='Editora')
publishing_company_label.grid(row=0, column=4, padx=10, pady=10)
publishing_company_entry = Entry(data_frame)
publishing_company_entry.grid(row=0, column=5, padx=10, pady=10)

n_pages_label = Label(data_frame, text='Número de páginas')
n_pages_label.grid(row=1, column=0, padx=10, pady=10)
n_pages_entry = Entry(data_frame)
n_pages_entry.grid(row=1, column=1, padx=10, pady=10)

owner_book_label = Label(data_frame, text='Proprietário')
owner_book_label.grid(row=1, column=2, padx=10, pady=10)
owner_book_entry = Entry(data_frame)
owner_book_entry.grid(row=1, column=3, padx=10, pady=10)

# criação do label responsável por gerenciar os botões de comandos
button_frame = LabelFrame(root, text='Comandos')
button_frame.pack(fill=BOTH, expand=True, pady=10, padx=10, anchor=N)

add_button = Button(button_frame, text='Adicionar Dado')
add_button.grid(row=0, column=0, padx=10, pady=10)

update_button = Button(button_frame, text='Atualizar Dado Selecionado')
update_button.grid(row=0, column=1, padx=10, pady=10)

remove_one_button = Button(button_frame, text='Deletar Dado Selecionado', command=lambda: data_base.selecionar_dado(
    title_book_entry, author_book_entry, publishing_company_entry, n_pages_entry, owner_book_entry, books_table))
remove_one_button.grid(row=0, column=2, padx=10, pady=10)

show_books_button = Button(button_frame, text='Mostar Livros', command=lambda: button_actions.mostra_livros(
    books_table, authors_table, publishing_companys_table, tree_scrool))
show_books_button.grid(row=0, column=3, padx=10, pady=10)

show_authors_button = Button(button_frame, text='Mostrar Autores (Livros)', command=lambda: button_actions.mostra_autores(
    books_table, authors_table, publishing_companys_table, tree_scrool))
show_authors_button.grid(row=0, column=4, padx=10, pady=10)

show_publishing_company_button = Button(
    button_frame, text='Mostar Editoras (Livros)', command=lambda: button_actions.mostra_editoras(books_table, authors_table, publishing_companys_table, tree_scrool))
show_publishing_company_button.grid(row=0, column=5, padx=10, pady=10)

# button = Button(button_frame, text='')
# button.grid(row=0, column=0, padx=10, pady=10)

# button = Button(button_frame, text='')
# button.grid(row=0, column=0, padx=10, pady=10)

root.mainloop()
