from DBHelper import DBHelper
from tkinter import *
from tkinter import ttk

data_base = DBHelper()

root = Tk()
root.title('Livraria')
root.geometry('500x500')

style = ttk.Style()
style.theme_use('default')
style.configure(
    'Treeview',
    background='#D3D3D3',
    foreground='black',
    rowheight=25,
    fieldbackground='#D3D3D3'
)
style.map(
    'Treeview',
    background=[('selected', '#347083')]
)

tree_frame = Frame(root)
tree_frame.pack(pady=10, padx=10, expand=True, fill=BOTH, anchor=N)

tree_scrool = Scrollbar(tree_frame)
tree_scrool.pack(side=RIGHT, fill=Y)

my_tree = ttk.Treeview(
    tree_frame, yscrollcommand=tree_scrool.set, selectmode='extended')
my_tree.pack(expand=True, fill=BOTH)

tree_scrool.config(command=my_tree.yview)

my_tree['columns'] = ('id', 'titulo', 'autor', 'editora',
                      'n_paginas', 'proprietario')
my_tree.column('#0', width=0, stretch=NO)

my_tree.column('id', anchor=CENTER, width=100)
my_tree.column('titulo', anchor=W, width=140)
my_tree.column('autor', anchor=W, width=140)
my_tree.column('editora', anchor=W, width=140)
my_tree.column('n_paginas', anchor=CENTER, width=100)
my_tree.column('proprietario', anchor=W, width=140)

my_tree.heading('#0', text='', anchor=W)
my_tree.heading('id', text='ID', anchor=CENTER)
my_tree.heading('titulo', text='Título', anchor=W)
my_tree.heading('autor', text='Autor(a)', anchor=W)
my_tree.heading('editora', text='Editora', anchor=W)
my_tree.heading('n_paginas', text='Nº Páginas', anchor=CENTER)
my_tree.heading('proprietario', text='Proprietário(a)', anchor=W)

livros = [
    [1, 'Patriarcas e Profetas', 'Ellen G. White',
        'CPB - Casa Publicadora Brasileira', 773, 'João Artur do Nascimento Neto'],
    [2, 'Profetas e Reis', 'Ellen G. White',
        'CPB - Casa Publicadora Brasileira', 500, 'João Artur do Nascimento Neto'],
    [3, 'O Desejado de Todas as Nações', 'Ellen G. White',
        'CPB - Casa Publicadora Brasileira', 829, 'João Artur do Nascimento Neto'],
    [4, 'Atos dos Apóstolos', 'Ellen G. White',
        'CPB - Casa Publicadora Brasileira', 500, 'João Artur do Nascimento Neto'],
    [5, 'O Grande Conflito', 'Ellen G. White',
        'CPB - Casa Publicadora Brasileira', 623, 'João Artur do Nascimento Neto'],
    [6, 'Patriarcas e Profetas', 'Ellen G. White',
        'CPB - Casa Publicadora Brasileira', 773, 'João Artur do Nascimento Neto'],
    [7, 'Profetas e Reis', 'Ellen G. White',
        'CPB - Casa Publicadora Brasileira', 500, 'João Artur do Nascimento Neto'],
    [8, 'O Desejado de Todas as Nações', 'Ellen G. White',
        'CPB - Casa Publicadora Brasileira', 829, 'João Artur do Nascimento Neto'],
    [9, 'Atos dos Apóstolos', 'Ellen G. White',
        'CPB - Casa Publicadora Brasileira', 500, 'João Artur do Nascimento Neto'],
    [10, 'O Grande Conflito', 'Ellen G. White',
        'CPB - Casa Publicadora Brasileira', 623, 'João Artur do Nascimento Neto'],
    [11, 'Patriarcas e Profetas', 'Ellen G. White',
        'CPB - Casa Publicadora Brasileira', 773, 'João Artur do Nascimento Neto'],
    [12, 'Profetas e Reis', 'Ellen G. White',
        'CPB - Casa Publicadora Brasileira', 500, 'João Artur do Nascimento Neto'],
    [13, 'O Desejado de Todas as Nações', 'Ellen G. White',
        'CPB - Casa Publicadora Brasileira', 829, 'João Artur do Nascimento Neto'],
    [14, 'Atos dos Apóstolos', 'Ellen G. White',
        'CPB - Casa Publicadora Brasileira', 500, 'João Artur do Nascimento Neto'],
    [15, 'O Grande Conflito', 'Ellen G. White',
        'CPB - Casa Publicadora Brasileira', 623, 'João Artur do Nascimento Neto'],
    [16, 'Patriarcas e Profetas', 'Ellen G. White',
        'CPB - Casa Publicadora Brasileira', 773, 'João Artur do Nascimento Neto'],
    [17, 'Profetas e Reis', 'Ellen G. White',
        'CPB - Casa Publicadora Brasileira', 500, 'João Artur do Nascimento Neto'],
    [18, 'O Desejado de Todas as Nações', 'Ellen G. White',
        'CPB - Casa Publicadora Brasileira', 829, 'João Artur do Nascimento Neto'],
    [19, 'Atos dos Apóstolos', 'Ellen G. White',
        'CPB - Casa Publicadora Brasileira', 500, 'João Artur do Nascimento Neto'],
    [20, 'O Grande Conflito', 'Ellen G. White',
        'CPB - Casa Publicadora Brasileira', 623, 'João Artur do Nascimento Neto'],
]

my_tree.tag_configure('oddrow', background='white')
my_tree.tag_configure('evenrow', background='lightblue')

for livro in livros:
    id = livro[0]
    titulo = livro[1]
    autor = livro[2]
    editora = livro[3]
    n_pags = livro[4]
    proprietario = livro[5]

    if (id % 2 == 0):
        my_tree.insert(parent='', index='end', values=(
            id, titulo, autor, editora, n_pags, proprietario), tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', values=(
            id, titulo, autor, editora, n_pags, proprietario), tags=('oddrow',))

register_frame = LabelFrame(
    root,
    text='Adicionar Livro'
)
register_frame.pack(expand=True, fill='both', padx=10, pady=10, anchor=N)

title_book_label = Label(register_frame, text='Título')
title_book_label.grid(row=0, column=0, padx=10, pady=10)
title_book_entry = Entry(register_frame)
title_book_entry.grid(row=0, column=1, padx=10, pady=10)

author_book_label = Label(register_frame, text='Autor')
author_book_label.grid(row=0, column=2, padx=10, pady=10)
author_book_entry = Entry(register_frame)
author_book_entry.grid(row=0, column=3, padx=10, pady=10)

publishing_company_label = Label(register_frame, text='Editora')
publishing_company_label.grid(row=0, column=4, padx=10, pady=10)
publishing_company_entry = Entry(register_frame)
publishing_company_entry.grid(row=0, column=5, padx=10, pady=10)

n_pages_label = Label(register_frame, text='Número de páginas')
n_pages_label.grid(row=1, column=0, padx=10, pady=10)
n_pages_entry = Entry(register_frame)
n_pages_entry.grid(row=1, column=1, padx=10, pady=10)

owner_book_label = Label(register_frame, text='Proprietário')
owner_book_label.grid(row=1, column=2, padx=10, pady=10)
owner_book_entry = Entry(register_frame)
owner_book_entry.grid(row=1, column=3, padx=10, pady=10)

button_frame = LabelFrame(root, text='Comandos')
button_frame.pack(fill='both', expand=True, pady=10, padx=10)

add_button = Button(button_frame, text='Adicionar Livro')
add_button.grid(row=0, column=0, padx=10, pady=10)

update_button = Button(button_frame, text='Atualizar Livro')
update_button.grid(row=0, column=1, padx=10, pady=10)

remove_one_button = Button(button_frame, text='Deletar Livro')
remove_one_button.grid(row=0, column=2, padx=10, pady=10)

show_books_button = Button(button_frame, text='Mostar Livros')
show_books_button.grid(row=0, column=3, padx=10, pady=10)

show_authors_button = Button(button_frame, text='Mostrar Autores')
show_authors_button.grid(row=0, column=4, padx=10, pady=10)

show_publishing_company_button = Button(button_frame, text='Mostar Editoras')
show_publishing_company_button.grid(row=0, column=5, padx=10, pady=10)

# button = Button(button_frame, text='')
# button.grid(row=0, column=0, padx=10, pady=10)

# button = Button(button_frame, text='')
# button.grid(row=0, column=0, padx=10, pady=10)

root.mainloop()
