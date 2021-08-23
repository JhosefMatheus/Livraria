# imports
import csv
import pandas as pd
from tkinter import *
from tkinter import messagebox
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
    with open('livros.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)

        id_livro = int(open('ultimo_id_livros.txt', 'r').readline()) + 1
        dados = [id_livro, titulo, autor, editora, n_paginas, proprietario]

        writer.writerow(dados)

        f = open('ultimo_id_livros.txt', 'w')
        f.truncate()
        f.write(str(id_livro))

    with open('autores.csv', 'r+') as csv_file:
        autores = [x[1] for x in csv.reader(csv_file) if x]

        if autor not in autores:
            add_autor(autor)

    with open('editoras.csv', 'r+') as csv_file:
        editoras = [x[1] for x in csv.reader(csv_file) if x]

        if editora not in editoras:
            add_editora(editora)


def add_autor(autor):
    with open('autores.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)

        id_autor = int(open('ultimo_id_autores.txt', 'r').readline()) + 1
        dados = [id_autor, autor]

        writer.writerow(dados)

        f = open('ultimo_id_autores.txt', 'w')
        f.truncate()
        f.write(str(id_autor))


def add_editora(editora):
    with open('editoras.csv', 'a') as csv_file:
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
        titulo = titulo_entry_registro_livro.get().strip()
        autor = autor_entry_registro_livro.get().strip()
        editora = editora_entry_registro_livro.get().strip()
        n_pages = n_pages_entry_registro_livro.get().strip()
        proprietario = proprietario_entry_registro_livro.get().strip()

        if len(titulo) == 0 or len(autor) == 0 or len(editora) == 0 or len(n_pages) == 0 or len(proprietario) == 0 or not n_pages.isdigit():
            messagebox.showinfo('Valores inválidos',
                                'Algum dos valores digitados está inválido!')
        else:
            add_livro(titulo, autor, editora, n_pages, proprietario)

            titulo_entry_registro_livro.delete(0, END)
            autor_entry_registro_livro.delete(0, END)
            editora_entry_registro_livro.delete(0, END)
            n_pages_entry_registro_livro.delete(0, END)
            proprietario_entry_registro_livro.delete(0, END)

            carrega_tabelas()
            cancelar_registro()

    elif drop_down_register.get() == 'Autor':
        autor = autor_entry_registro_autor.get().strip()

        if len(autor) == 0:
            messagebox.showinfo('Valor inválido', 'Valor digitado inválido')
        else:
            add_autor(autor)

            autor_entry_registro_autor.delete(0, END)

            carrega_tabelas()
            cancelar_registro()

    elif drop_down_register.get() == 'Editora':
        editora = editora_entry_registro_editora.get().strip()

        if len(editora) == 0:
            messagebox.showinfo('Valor inválido', 'Valor digitado inválido')
        else:
            add_editora(editora)

            editora_entry_registro_editora.delete(0, END)

            carrega_tabelas()
            cancelar_registro()


def selecionar_livro(event):
    try:
        livro_selecionado = tabela_livros.item(tabela_livros.focus())['values']

        titulo_entry_editar_excluir_livro.delete(0, END)
        autor_entry_editar_excluir_livro.delete(0, END)
        editora_entry_editar_excluir_livro.delete(0, END)
        n_pages_entry_editar_excluir_livro.delete(0, END)
        proprietario_entry_editar_excluir_livro.delete(0, END)

        titulo_entry_editar_excluir_livro.insert(0, livro_selecionado[1])
        autor_entry_editar_excluir_livro.insert(0, livro_selecionado[2])
        editora_entry_editar_excluir_livro.insert(0, livro_selecionado[3])
        n_pages_entry_editar_excluir_livro.insert(0, livro_selecionado[4])
        proprietario_entry_editar_excluir_livro.insert(0, livro_selecionado[5])

        tabela_livros.pack_forget()

        table_frame['text'] = 'Editar/Excluir Livro'

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

    except IndexError as e:
        messagebox.showinfo('Livro selecionado inválido',
                            'Por favor clique em algum livro da tabela')


def selecionar_autor(event):
    try:
        autor_selecionado = tabela_autores.item(
            tabela_autores.focus())['values']

        autor_entry_editar_excluir_autor.delete(0, END)

        autor_entry_editar_excluir_autor.insert(0, autor_selecionado[1])

        tabela_autores.pack_forget()

        table_frame['text'] = 'Editar/Excluir Autor'

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
    except IndexError as e:
        messagebox.showinfo('Autor selecionado inválido',
                            'Por favor clique em algum autor da tabela')


def selecionar_editora(event):
    try:
        editora_selecionada = tabela_editoras.item(
            tabela_editoras.focus())['values']

        editora_entry_editar_excluir_editora.delete(0, END)

        editora_entry_editar_excluir_editora.insert(0, editora_selecionada[1])

        tabela_editoras.pack_forget()

        table_frame['text'] = 'Editar/Excluir Editora'

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

    except IndexError as e:
        messagebox.showinfo('Editora selecionada inválida',
                            'Por favor clique em alguma editora da tabela')


def editar_livro():
    livro_selecionado = tabela_livros.item(tabela_livros.focus())['values']

    titulo = titulo_entry_editar_excluir_livro.get().strip()
    autor = autor_entry_editar_excluir_livro.get().strip()
    editora = editora_entry_editar_excluir_livro.get().strip()
    n_paginas = n_pages_entry_editar_excluir_livro.get().strip()
    proprietario = proprietario_entry_editar_excluir_livro.get().strip()

    id_livro_selecionado = livro_selecionado[0]
    autor_livro_selecionado = livro_selecionado[2]
    editora_livro_selecionado = livro_selecionado[3]

    df_livros = pd.read_csv('livros.csv')
    df_autores = pd.read_csv('autores.csv')
    df_editoras = pd.read_csv('editoras.csv')

    if len(titulo) == 0 or len(autor) == 0 or len(editora) == 0 or len(n_paginas) == 0 or len(proprietario) == 0 or not n_paginas.isdigit():
        messagebox.showinfo(
            'Valores inválidos', 'Algum dos valores digitados é um valor inválido ou está em branco')

    else:

        df_livros.loc[id_livro_selecionado - 1,
                      'titulo'] = titulo
        df_livros.loc[id_livro_selecionado - 1,
                      'autor'] = autor
        df_livros.loc[id_livro_selecionado - 1,
                      'editora'] = editora
        df_livros.loc[id_livro_selecionado - 1,
                      'n_paginas'] = n_paginas
        df_livros.loc[id_livro_selecionado - 1,
                      'proprietario'] = proprietario

        df_livros.to_csv('livros.csv', index=False)

        autores = list(df_livros.loc[df_livros['autor']
                                     == autor_livro_selecionado].autor)
        editoras = list(
            df_livros.loc[df_livros['editora'] == editora_livro_selecionado].editora)

        if autor_livro_selecionado not in autores:
            df_autores = df_autores[df_autores.autor !=
                                    autor_livro_selecionado]

        if editora_livro_selecionado not in editoras:
            df_editoras = df_editoras[df_editoras.editora !=
                                      editora_livro_selecionado]

        df_autores.to_csv('autores.csv', index=False)
        df_editoras.to_csv('editoras.csv', index=False)

        with open('autores.csv', 'r+') as csv_file:
            autores = [x[1] for x in csv.reader(csv_file) if x]

            if autor not in autores:
                add_autor(autor)

        with open('editoras.csv', 'r+') as csv_file:
            editoras = [x[1] for x in csv.reader(csv_file) if x]

            if editora not in editoras:
                add_editora(editora)

        cancelar_edicao_livro()

        carrega_tabelas()


def cancelar_edicao_livro():
    tabela_livros.selection_remove(tabela_livros.focus())

    tabela_livros.focus('')

    titulo_entry_editar_excluir_livro.delete(0, END)
    autor_entry_editar_excluir_livro.delete(0, END)
    editora_entry_editar_excluir_livro.delete(0, END)
    n_pages_entry_editar_excluir_livro.delete(0, END)
    proprietario_entry_editar_excluir_livro.delete(0, END)

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
    livro_selecionado = tabela_livros.item(tabela_livros.focus())['values']

    id_livro = livro_selecionado[0]
    autor_livro = livro_selecionado[2]
    editora_livro = livro_selecionado[3]

    df_livros = pd.read_csv('livros.csv')
    df_autores = pd.read_csv('autores.csv')
    df_editoras = pd.read_csv('editoras.csv')

    df_livros.drop(id_livro - 1, axis=0, inplace=True)

    df_livros.to_csv('livros.csv', index=False)

    autores = list(df_livros.loc[df_livros['autor']
                                 == autor_livro].autor)
    editoras = list(
        df_livros.loc[df_livros['editora'] == editora_livro].editora)

    if autor_livro not in autores:
        df_autores = df_autores[df_autores.autor != autor_livro]

    if editora_livro not in editoras:
        df_editoras = df_editoras[df_editoras.editora !=
                                  editora_livro]

    df_autores.to_csv('autores.csv', index=False)
    df_editoras.to_csv('editoras.csv', index=False)

    cancelar_edicao_livro()

    carrega_tabelas()


def editar_autor():
    id_autor, nome_autor = tabela_autores.item(
        tabela_autores.focus())['values']

    df_livros = pd.read_csv('livros.csv')
    df_autores = pd.read_csv('autores.csv')

    if len(autor_entry_editar_excluir_autor.get().strip()) == 0:
        messagebox.showinfo(
            'Valor inválido', 'O valor digitado para nome do autor está em branco')
    else:

        df_autores.loc[id_autor - 1,
                       'autor'] = autor_entry_editar_excluir_autor.get()

        df_autores.to_csv('autores.csv', index=False)

        df_livros.loc[df_livros['autor'] == nome_autor,
                      'autor'] = autor_entry_editar_excluir_autor.get()

        df_livros.to_csv('livros.csv', index=False)

        cancelar_edicao_autor()

        carrega_tabelas()


def excluir_autor():
    id_autor, nome_autor = tabela_autores.item(
        tabela_autores.focus())['values']

    df_livros = pd.read_csv('livros.csv')
    df_autores = pd.read_csv('autores.csv')

    df_autores.drop(id_autor - 1, axis=0, inplace=True)
    df_autores.to_csv('autores.csv', index=False)

    df_livros.loc[df_livros['autor'] ==
                  nome_autor, 'autor'] = 'Desconhecido(a)'

    df_livros.to_csv('livros.csv', index=False)

    cancelar_edicao_autor()

    carrega_tabelas()


def cancelar_edicao_autor():
    tabela_autores.selection_remove(tabela_autores.focus())

    tabela_autores.focus('')

    autor_entry_editar_excluir_autor.delete(0, END)

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
    id_editora, nome_editora = tabela_editoras.item(
        tabela_editoras.focus())['values']

    df_livros = pd.read_csv('livros.csv')
    df_editoras = pd.read_csv('editoras.csv')

    if len(editora_entry_editar_excluir_editora.get().strip()) == 0:
        messagebox.showinfo(
            'Valor inválido', 'Valores digitado está em branco')

    else:

        df_editoras.loc[id_editora - 1,
                        'editora'] = editora_entry_editar_excluir_editora.get()

        df_editoras.to_csv('editoras.csv', index=False)

        df_livros.loc[df_livros['editora'] == nome_editora,
                      'editora'] = editora_entry_editar_excluir_editora.get()

        df_livros.to_csv('livros.csv', index=False)

        cancelar_edicao_editora()

        carrega_tabelas()


def excluir_editora():
    id_editora, nome_editora = tabela_editoras.item(
        tabela_editoras.focus())['values']

    df_livros = pd.read_csv('livros.csv')
    df_editoras = pd.read_csv('editoras.csv')

    df_editoras.drop(id_editora - 1, axis=0, inplace=True)
    df_editoras.to_csv('editoras.csv', index=False)

    df_livros.loc[df_livros['editora'] ==
                  nome_editora, 'editora'] = 'Desconhecida'
    df_livros.to_csv('livros.csv', index=False)

    cancelar_edicao_editora()

    carrega_tabelas()


def cancelar_edicao_editora():
    tabela_editoras.selection_remove(tabela_editoras.focus())

    tabela_editoras.focus('')

    editora_entry_editar_excluir_editora.delete(0, END)

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
    fieldbackground='#D3D3D3',
    font='Arial 12'
)
style.map(
    'Treeview',
    background=[('selected', '#347083')]
)

# criação do frame responsável por conter as tabelas e criação das tabelas
table_frame = LabelFrame(
    root,
    text='Livros',
    font='Arial 12'
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
    text='Titulo',
    font='Arial 12'
)
titulo_label_registro_livro.grid(row=0, column=0, padx=10, pady=10)

titulo_entry_registro_livro = Entry(
    livro_register_frame,
    font='Arial 12'
)
titulo_entry_registro_livro.grid(row=0, column=1, padx=10, pady=10, sticky=EW)

autor_label_registro_livro = Label(
    livro_register_frame,
    text='Autor',
    font='Arial 12'
)
autor_label_registro_livro.grid(row=1, column=0, padx=10, pady=10)

autor_entry_registro_livro = Entry(
    livro_register_frame,
    font='Arial 12'
)
autor_entry_registro_livro.grid(row=1, column=1, padx=10, pady=10, sticky=EW)

editora_label_registro_livro = Label(
    livro_register_frame,
    text='Editora',
    font='Arial 12'
)
editora_label_registro_livro.grid(row=2, column=0, padx=10, pady=10)

editora_entry_registro_livro = Entry(
    livro_register_frame,
    font='Arial 12'
)
editora_entry_registro_livro.grid(row=2, column=1, padx=10, pady=10, sticky=EW)

n_pages_label_registro_livro = Label(
    livro_register_frame,
    text='Nº Páginas',
    font='Arial 12'
)
n_pages_label_registro_livro.grid(row=3, column=0, padx=10, pady=10)

n_pages_entry_registro_livro = Entry(
    livro_register_frame,
    font='Arial 12'
)
n_pages_entry_registro_livro.grid(row=3, column=1, padx=10, pady=10, sticky=EW)

proprietario_label_registro_livro = Label(
    livro_register_frame,
    text='Proprietário',
    font='Arial'
)
proprietario_label_registro_livro.grid(row=4, column=0, padx=10, pady=10)

proprietario_entry_registro_livro = Entry(
    livro_register_frame,
    font='Arial 12'
)
proprietario_entry_registro_livro.grid(
    row=4, column=1, padx=10, pady=10, sticky=EW)

# frame responsável pela tela de registro dos autores
autor_register_frame = Frame(
    table_frame,
)

autor_register_frame.columnconfigure(1, weight=1)

autor_label_registro_autor = Label(
    autor_register_frame,
    text='Autor',
    font='Arial 12'
)
autor_label_registro_autor.grid(row=0, column=0, padx=10, pady=10)

autor_entry_registro_autor = Entry(
    autor_register_frame,
    font='Arial 12'
)
autor_entry_registro_autor.grid(row=0, column=1, padx=10, pady=10, sticky=EW)

# frame responsável pela tela de registro das editoras
editora_register_frame = Frame(
    table_frame
)

editora_register_frame.columnconfigure(1, weight=1)

editora_label_registro_editora = Label(
    editora_register_frame,
    text='Editora',
    font='Arial 12'
)
editora_label_registro_editora.grid(row=0, column=0, padx=10, pady=10)

editora_entry_registro_editora = Entry(
    editora_register_frame,
    font='Arial 12'
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
    command=lambda: adicionar_registro(),
    font='Arial 12'
)
button_add.grid(row=0, column=0, padx=10, pady=10, sticky=EW)

button_cancel = Button(
    button_register_frame,
    text='Cancelar',
    relief=GROOVE,
    command=lambda: cancelar_registro(),
    font='Arial 12'
)
button_cancel.grid(row=0, column=1, padx=10, pady=10, sticky=EW)

drop_down_register = ttk.Combobox(
    button_register_frame,
    values=(
        'Livro',
        'Autor',
        'Editora'
    ),
    state='readonly',
    font='Arial 12'
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
    text='Titulo',
    font='Arial 12'
)
titulo_label_editar_excluir_livro.grid(row=0, column=0, padx=10, pady=10)

titulo_entry_editar_excluir_livro = Entry(
    editar_excluir_livro,
    font='Arial 12'
)
titulo_entry_editar_excluir_livro.grid(
    row=0, column=1, padx=10, pady=10, sticky=EW)

autor_label_editar_excluir_livro = Label(
    editar_excluir_livro,
    text='Autor',
    font='Arial 12'
)
autor_label_editar_excluir_livro.grid(row=1, column=0, padx=10, pady=10)

autor_entry_editar_excluir_livro = Entry(
    editar_excluir_livro,
    font='Arial 12'
)
autor_entry_editar_excluir_livro.grid(
    row=1, column=1, padx=10, pady=10, sticky=EW)

editora_label_editar_excluir_livro = Label(
    editar_excluir_livro,
    text='Editora',
    font='Arial 12'
)
editora_label_editar_excluir_livro.grid(row=2, column=0, padx=10, pady=10)

editora_entry_editar_excluir_livro = Entry(
    editar_excluir_livro,
    font='Arial 12'
)
editora_entry_editar_excluir_livro.grid(
    row=2, column=1, padx=10, pady=10, sticky=EW)

n_pages_label_editar_excluir_livro = Label(
    editar_excluir_livro,
    text='Nº Páginas',
    font='Arial 12'
)
n_pages_label_editar_excluir_livro.grid(row=3, column=0, padx=10, pady=10)

n_pages_entry_editar_excluir_livro = Entry(
    editar_excluir_livro,
    font='Arial 12'
)
n_pages_entry_editar_excluir_livro.grid(
    row=3, column=1, padx=10, pady=10, sticky=EW)

proprietario_label_editar_excluir_livro = Label(
    editar_excluir_livro,
    text='Proprietário',
    font='Arial 12'
)
proprietario_label_editar_excluir_livro.grid(row=4, column=0, padx=10, pady=10)

proprietario_entry_editar_excluir_livro = Entry(
    editar_excluir_livro,
    font='Arial 12'
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
    command=lambda: editar_livro(),
    font='Arial 12'
)
botao_editar_livro.grid(row=0, column=0, padx=10, pady=10, sticky=EW)

botao_excluir_livro = Button(
    botoes_editar_excluir_livro,
    text='Excluir',
    relief=GROOVE,
    command=lambda: excluir_livro(),
    font='Arial 12'
)
botao_excluir_livro.grid(row=0, column=1, padx=10, pady=10, sticky=EW)

botao_cancelar_edicao_livro = Button(
    botoes_editar_excluir_livro,
    text='Cancelar',
    relief=GROOVE,
    command=lambda: cancelar_edicao_livro(),
    font='Arial 12'
)
botao_cancelar_edicao_livro.grid(row=0, column=2, padx=10, pady=10, sticky=EW)

editar_excluir_autor = Frame(
    table_frame
)

editar_excluir_autor.columnconfigure(1, weight=1)

autor_label_editar_excluir_autor = Label(
    editar_excluir_autor,
    text='Autor',
    font='Arial 12'
)
autor_label_editar_excluir_autor.grid(row=0, column=0, padx=10, pady=10)

autor_entry_editar_excluir_autor = Entry(
    editar_excluir_autor,
    font='Arial 12'
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
    command=lambda: editar_autor(),
    font='Arial 12'
)
botao_editar_autor.grid(row=0, column=0, padx=10, pady=10, sticky=EW)

botao_excluir_autor = Button(
    botoes_editar_excluir_autor,
    text='Excluir',
    relief=GROOVE,
    command=lambda: excluir_autor(),
    font='Arial 12'
)
botao_excluir_autor.grid(row=0, column=1, padx=10, pady=10, sticky=EW)

botao_cancelar_edicao_autor = Button(
    botoes_editar_excluir_autor,
    text='Cancelar',
    relief=GROOVE,
    command=lambda: cancelar_edicao_autor(),
    font='Arial 12'
)
botao_cancelar_edicao_autor.grid(row=0, column=2, padx=10, pady=10, sticky=EW)

editar_excluir_editora = Frame(
    table_frame
)

editar_excluir_editora.columnconfigure(1, weight=1)

editora_label_editar_excluir_editora = Label(
    editar_excluir_editora,
    text='Editora',
    font='Arial 12'
)
editora_label_editar_excluir_editora.grid(row=0, column=0, padx=10, pady=10)

editora_entry_editar_excluir_editora = Entry(
    editar_excluir_editora,
    font='Arial 12'
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
    command=lambda: editar_editora(),
    font='Arial 12'
)
botao_editar_editora.grid(row=0, column=0, padx=10, pady=10, sticky=EW)

botao_excluir_editora = Button(
    botoes_editar_excluir_editora,
    text='Excluir',
    relief=GROOVE,
    command=lambda: excluir_editora(),
    font='Arial 12'
)
botao_excluir_editora.grid(row=0, column=1, padx=10, pady=10, sticky=EW)

botao_cancelar_edicao_editora = Button(
    botoes_editar_excluir_editora,
    text='Cancelar',
    relief=GROOVE,
    command=lambda: cancelar_edicao_editora(),
    font='Arial 12'
)
botao_cancelar_edicao_editora.grid(
    row=0, column=2, padx=10, pady=10, sticky=EW)


# criação do label frame responsável por gerenciar os botões de comandos
button_frame = LabelFrame(
    root,
    text='Comandos',
    font='Arial 12'
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
    command=lambda: adicionar_novo(),
    font='Arial 12'
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
    ),
    state='readonly',
    font='Arial 12'
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
