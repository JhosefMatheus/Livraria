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
tree_frame.pack(pady=10)

tree_scrool = Scrollbar(tree_frame)
tree_scrool.pack(side=RIGHT, fill=Y)

my_tree = ttk.Treeview(
    tree_frame, yscrollcommand=tree_scrool.set, selectmode='extended')
my_tree.pack(fill='both')

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
        'CPB - Casa Publicadora Brasileira', 623, 'João Artur do Nascimento Neto']
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


root.mainloop()
