# imports
from tkcalendar import DateEntry
from ttkwidgets.autocomplete import AutocompleteCombobox
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from db_manager import db_manager

db = db_manager()


def carrega_tabelas():
    '''
    Função responsável por carregar a treeview tabela_livros, tabela_autores, tabela_editoras
    sempre que alguma alteração é feita em uma dessas tabelas.
    '''
    livros = db.get_data('livros.csv')
    autores = db.get_data('autores_livros.csv')
    editoras = db.get_data('editoras_livros.csv')
    dvds = db.get_data('dvds.csv')
    cds = db.get_data('cds.csv')
    autores_artistas_cds = db.get_data('autores_artistas_cds.csv')
    diretores_dvds = db.get_data('diretores_dvds.csv')
    distribuidoras_cds = db.get_data('distribuidoras_cds.csv')
    distribuidoras_dvds = db.get_data('distribuidoras_dvds.csv')

    for livro in tabela_livros.get_children():
        tabela_livros.delete(livro)

    for autor in tabela_autores.get_children():
        tabela_autores.delete(autor)

    for editora in tabela_editoras.get_children():
        tabela_editoras.delete(editora)

    for dvd in tabela_dvds.get_children():
        tabela_dvds.delete(dvd)

    for cd in tabela_cds.get_children():
        tabela_cds.delete(cd)

    for autor_artista_cd in tabela_autores_artistas_cds.get_children():
        tabela_autores_artistas_cds.delete(autor_artista_cd)

    for diretor_dvd in tabela_diretores_dvds.get_children():
        tabela_diretores_dvds.delete(diretor_dvd)

    for distribuidora_cd in tabela_distribuidoras_cds.get_children():
        tabela_distribuidoras_cds.delete(distribuidora_cd)

    for distribuidora_dvd in tabela_distribuidoras_dvds.get_children():
        tabela_distribuidoras_dvds.delete(distribuidora_dvd)

    count = 0

    for livro in livros:
        id = livro[0]
        titulo = livro[1]
        autor = livro[2]
        editora = livro[3]
        n_paginas = livro[4]
        situacao = livro[5]
        beneficiado = livro[6]
        telefone = livro[7]
        data_emprestimo = livro[8]
        data_devolucao = livro[9]

        if count % 2 == 0:

            tabela_livros.insert('', END, values=(
                id,
                titulo,
                autor,
                editora,
                n_paginas,
                situacao,
                beneficiado,
                telefone,
                data_emprestimo,
                data_devolucao
            ), tags=('evenrow',))

        else:
            tabela_livros.insert('', END, values=(
                id,
                titulo,
                autor,
                editora,
                n_paginas,
                situacao,
                beneficiado,
                telefone,
                data_emprestimo,
                data_devolucao
            ), tags=('oddrow',))

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

    count = 0

    for dvd in dvds:
        id = dvd[0]
        titulo = dvd[1]
        diretor = dvd[2]
        distribuidora = dvd[3]
        tempo = dvd[4]
        situacao = dvd[5]
        beneficiado = dvd[6]
        telefone = dvd[7]
        data_emprestimo = dvd[8]
        data_devolucao = dvd[9]

        if count % 2 == 0:
            tabela_dvds.insert(
                '',
                END,
                values=(
                    id,
                    titulo,
                    diretor,
                    distribuidora,
                    tempo,
                    situacao,
                    beneficiado,
                    telefone,
                    data_emprestimo,
                    data_devolucao
                ),
                tags=('evenrow',)
            )

        else:
            tabela_dvds.insert(
                '',
                END,
                values=(
                    id,
                    titulo,
                    diretor,
                    distribuidora,
                    tempo,
                    situacao,
                    beneficiado,
                    telefone,
                    data_emprestimo,
                    data_devolucao
                ),
                tags=('oddrow',)
            )

        count += 1

    count = 0

    for cd in cds:
        id = cd[0]
        titulo = cd[1]
        artista_autor = cd[2]
        distribuidora = cd[3]
        tempo = cd[4]
        situacao = cd[5]
        beneficiado = cd[6]
        telefone = cd[7]
        data_emprestimo = cd[8]
        data_devolucao = cd[9]

        if count % 2 == 0:
            tabela_cds.insert(
                '',
                END,
                values=(
                    id,
                    titulo,
                    artista_autor,
                    distribuidora,
                    tempo,
                    situacao,
                    beneficiado,
                    telefone,
                    data_emprestimo,
                    data_devolucao
                ),
                tags=('evenrow',)
            )

        else:
            tabela_cds.insert(
                '',
                END,
                values=(
                    id,
                    titulo,
                    artista_autor,
                    distribuidora,
                    tempo,
                    situacao,
                    beneficiado,
                    telefone,
                    data_emprestimo,
                    data_devolucao
                ),
                tags=('oddrow',)
            )

        count += 1

    count = 0

    for autor_artista_cd in autores_artistas_cds:
        id = autor_artista_cd[0]
        nome_autor_artista_cd = autor_artista_cd[1]

        if count % 2 == 0:
            tabela_autores_artistas_cds.insert('', END, values=(
                id, nome_autor_artista_cd), tags=('evenrow',))

        else:
            tabela_autores_artistas_cds.insert('', END, values=(
                id, nome_autor_artista_cd), tags=('oddrow',))

        count += 1

    count = 0

    for diretor_dvd in diretores_dvds:
        id = diretor_dvd[0]
        nome_diretor_dvd = diretor_dvd[1]

        if count % 2 == 0:
            tabela_diretores_dvds.insert('', END, values=(
                id, nome_diretor_dvd), tags=('evenrow',))

        else:
            tabela_diretores_dvds.insert('', END, values=(
                id, nome_diretor_dvd), tags=('oddrow',))

        count += 1

    count = 0

    for distribuidora_cd in distribuidoras_cds:
        id = distribuidora_cd[0]
        nome_distribuidora_cd = distribuidora_cd[1]

        if count % 2 == 0:
            tabela_distribuidoras_cds.insert('', END, values=(
                id, nome_distribuidora_cd), tags=('evenrow',))

        else:
            tabela_distribuidoras_cds.insert('', END, values=(
                id, nome_distribuidora_cd), tags=('oddrow',))

        count += 1

    count = 0

    for distribuidora_dvd in distribuidoras_dvds:
        id = distribuidora_dvd[0]
        nome_distribuidora_dvd = distribuidora_dvd[1]

        if count % 2 == 0:
            tabela_distribuidoras_dvds.insert('', END, values=(
                id, nome_distribuidora_dvd), tags=('evenrow',))

        else:
            tabela_distribuidoras_dvds.insert('', END, values=(
                id, nome_distribuidora_dvd), tags=('oddrow',))

        count += 1


def mudar_tabela(event):
    '''
    Função responsável por alterar a tabela que está sendo exibida para o usuário no momento
    '''
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
    editar_excluir_dvd.pack_forget()
    botoes_editar_excluir_dvd.pack_forget()
    editar_excluir_autor_artista_cd.pack_forget()
    botoes_editar_excluir_autor_artista_cd.pack_forget()
    editar_excluir_diretor_dvd.pack_forget()
    botoes_editar_excluir_diretor_dvd.pack_forget()
    editar_excluir_distribuidora_cd.pack_forget()
    botoes_editar_excluir_distribuidora_cd.pack_forget()
    editar_excluir_distribuidora_dvd.pack_forget()
    botoes_editar_excluir_distribuidora_dvd.pack_forget()

    carrega_tabelas()

    table_frame.pack_forget()
    button_frame.pack_forget()

    if drop_down.get() == 'Livros':
        pesquisa_autor.pack_forget()
        pesquisa_editora.pack_forget()
        pesquisa_dvd.pack_forget()
        pesquisa_cd.pack_forget()
        pesquisa_artista_autor_cd.pack_forget()
        pesquisa_diretor_dvd.pack_forget()
        pesquisa_distribuidora_cd.pack_forget()
        pesquisa_distribuidora_dvd.pack_forget()

        pesquisa_livro.pack(
            expand=False,
            fill=X,
            padx=10,
            pady=10
        )

        tabela_autores.pack_forget()
        tabela_editoras.pack_forget()
        tabela_dvds.pack_forget()
        tabela_cds.pack_forget()
        tabela_autores_artistas_cds.pack_forget()
        tabela_diretores_dvds.pack_forget()
        tabela_distribuidoras_dvds.pack_forget()
        tabela_distribuidoras_cds.pack_forget()

        table_frame['text'] = 'Livros'

        table_frame.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

        tabela_livros.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

    elif drop_down.get() == 'Autores':
        pesquisa_livro.pack_forget()
        pesquisa_editora.pack_forget()
        pesquisa_dvd.pack_forget()
        pesquisa_cd.pack_forget()
        pesquisa_artista_autor_cd.pack_forget()
        pesquisa_diretor_dvd.pack_forget()
        pesquisa_distribuidora_cd.pack_forget()
        pesquisa_distribuidora_dvd.pack_forget()

        pesquisa_autor.pack(
            expand=False,
            fill=X,
            padx=10,
            pady=10
        )

        table_frame.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10,
        )

        tabela_livros.pack_forget()
        tabela_editoras.pack_forget()
        tabela_dvds.pack_forget()
        tabela_cds.pack_forget()
        tabela_autores_artistas_cds.pack_forget()
        tabela_diretores_dvds.pack_forget()
        tabela_distribuidoras_dvds.pack_forget()
        tabela_distribuidoras_cds.pack_forget()

        table_frame['text'] = 'Autores'

        tabela_autores.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

    elif drop_down.get() == 'Editoras':
        pesquisa_livro.pack_forget()
        pesquisa_autor.pack_forget()
        pesquisa_dvd.pack_forget()
        pesquisa_cd.pack_forget()
        pesquisa_artista_autor_cd.pack_forget()
        pesquisa_diretor_dvd.pack_forget()
        pesquisa_distribuidora_cd.pack_forget()
        pesquisa_distribuidora_dvd.pack_forget()

        pesquisa_editora.pack(
            expand=False,
            fill=X,
            padx=10,
            pady=10
        )

        tabela_livros.pack_forget()
        tabela_autores.pack_forget()
        tabela_dvds.pack_forget()
        tabela_cds.pack_forget()
        tabela_autores_artistas_cds.pack_forget()
        tabela_diretores_dvds.pack_forget()
        tabela_distribuidoras_cds.pack_forget()
        tabela_distribuidoras_dvds.pack_forget()

        table_frame.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

        table_frame['text'] = 'Editoras'

        tabela_editoras.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

    elif drop_down.get() == 'DVD\'s':
        pesquisa_livro.pack_forget()
        pesquisa_autor.pack_forget()
        pesquisa_editora.pack_forget()
        pesquisa_cd.pack_forget()
        pesquisa_artista_autor_cd.pack_forget()
        pesquisa_diretor_dvd.pack_forget()
        pesquisa_distribuidora_cd.pack_forget()
        pesquisa_distribuidora_dvd.pack_forget()

        pesquisa_dvd.pack(
            expand=False,
            fill=X,
            padx=10,
            pady=10
        )

        tabela_livros.pack_forget()
        tabela_autores.pack_forget()
        tabela_editoras.pack_forget()
        tabela_cds.pack_forget()
        tabela_autores_artistas_cds.pack_forget()
        tabela_diretores_dvds.pack_forget()
        tabela_distribuidoras_cds.pack_forget()
        tabela_distribuidoras_dvds.pack_forget()

        table_frame.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

        table_frame['text'] = 'DVD\'s'

        tabela_dvds.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

    elif drop_down.get() == 'CD\'s':
        pesquisa_livro.pack_forget()
        pesquisa_autor.pack_forget()
        pesquisa_editora.pack_forget()
        pesquisa_dvd.pack_forget()
        pesquisa_artista_autor_cd.pack_forget()
        pesquisa_diretor_dvd.pack_forget()
        pesquisa_distribuidora_cd.pack_forget()
        pesquisa_distribuidora_dvd.pack_forget()

        pesquisa_cd.pack(
            expand=False,
            fill=X,
            padx=10,
            pady=10
        )

        tabela_livros.pack_forget()
        tabela_autores.pack_forget()
        tabela_editoras.pack_forget()
        tabela_dvds.pack_forget()
        tabela_autores_artistas_cds.pack_forget()
        tabela_diretores_dvds.pack_forget()
        tabela_distribuidoras_dvds.pack_forget()
        tabela_distribuidoras_cds.pack_forget()

        table_frame.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

        table_frame['text'] = 'CD\'s'

        tabela_cds.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

    elif drop_down.get() == 'Artistas/Autores CD\'s':
        pesquisa_livro.pack_forget()
        pesquisa_autor.pack_forget()
        pesquisa_editora.pack_forget()
        pesquisa_dvd.pack_forget()
        pesquisa_cd.pack_forget()
        pesquisa_diretor_dvd.pack_forget()
        pesquisa_distribuidora_cd.pack_forget()
        pesquisa_distribuidora_dvd.pack_forget()

        pesquisa_artista_autor_cd.pack(
            expand=False,
            fill=X,
            padx=10,
            pady=10
        )

        tabela_livros.pack_forget()
        tabela_autores.pack_forget()
        tabela_editoras.pack_forget()
        tabela_dvds.pack_forget()
        tabela_cds.pack_forget()
        tabela_diretores_dvds.pack_forget()
        tabela_distribuidoras_dvds.pack_forget()
        tabela_distribuidoras_cds.pack_forget()

        table_frame.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

        table_frame['text'] = 'Artistas/Autores CD\'s'

        tabela_autores_artistas_cds.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

    elif drop_down.get() == 'Diretores DVD\'s':
        pesquisa_livro.pack_forget()
        pesquisa_autor.pack_forget()
        pesquisa_editora.pack_forget()
        pesquisa_dvd.pack_forget()
        pesquisa_cd.pack_forget()
        pesquisa_artista_autor_cd.pack_forget()
        pesquisa_distribuidora_cd.pack_forget()
        pesquisa_distribuidora_dvd.pack_forget()

        pesquisa_diretor_dvd.pack(
            expand=False,
            fill=X,
            padx=10,
            pady=10
        )

        tabela_livros.pack_forget()
        tabela_autores.pack_forget()
        tabela_editoras.pack_forget()
        tabela_dvds.pack_forget()
        tabela_cds.pack_forget()
        tabela_autores_artistas_cds.pack_forget()
        tabela_distribuidoras_dvds.pack_forget()
        tabela_distribuidoras_cds.pack_forget()

        table_frame.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

        table_frame['text'] = 'Diretores DVD\'s'

        tabela_diretores_dvds.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

    elif drop_down.get() == 'Distribuidoras DVD\'s':
        pesquisa_livro.pack_forget()
        pesquisa_autor.pack_forget()
        pesquisa_editora.pack_forget()
        pesquisa_dvd.pack_forget()
        pesquisa_cd.pack_forget()
        pesquisa_artista_autor_cd.pack_forget()
        pesquisa_diretor_dvd.pack_forget()
        pesquisa_distribuidora_cd.pack_forget()

        pesquisa_distribuidora_dvd.pack(
            expand=False,
            fill=X,
            padx=10,
            pady=10
        )

        tabela_livros.pack_forget()
        tabela_autores.pack_forget()
        tabela_editoras.pack_forget()
        tabela_dvds.pack_forget()
        tabela_cds.pack_forget()
        tabela_autores_artistas_cds.pack_forget()
        tabela_diretores_dvds.pack_forget()
        tabela_distribuidoras_cds.pack_forget()

        table_frame.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

        table_frame['text'] = 'Distribuidoras DVD\'s'

        tabela_distribuidoras_dvds.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

    elif drop_down.get() == 'Distribuidoras CD\'s':
        pesquisa_livro.pack_forget()
        pesquisa_autor.pack_forget()
        pesquisa_editora.pack_forget()
        pesquisa_cd.pack_forget()
        pesquisa_dvd.pack_forget()
        pesquisa_artista_autor_cd.pack_forget()
        pesquisa_diretor_dvd.pack_forget()
        pesquisa_distribuidora_dvd.pack_forget()

        pesquisa_distribuidora_cd.pack(
            expand=False,
            fill=X,
            padx=10,
            pady=10
        )

        tabela_livros.pack_forget()
        tabela_autores.pack_forget()
        tabela_editoras.pack_forget()
        tabela_dvds.pack_forget()
        tabela_cds.pack_forget()
        tabela_autores_artistas_cds.pack_forget()
        tabela_diretores_dvds.pack_forget()
        tabela_distribuidoras_dvds.pack_forget()

        table_frame.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

        table_frame['text'] = 'Distribuidoras CD\'s'

        tabela_distribuidoras_cds.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

    button_frame.pack(
        expand=False,
        fill=X,
        padx=10,
        pady=10
    )


def adicionar_novo():
    '''
    Função responsável por carregar a tela de registro. Está função sempre carrega a tela de registro
    do livro.
    '''
    table_frame['text'] = 'Novo Livro'

    pesquisa_livro.pack_forget()
    pesquisa_autor.pack_forget()
    pesquisa_editora.pack_forget()
    pesquisa_dvd.pack_forget()
    pesquisa_cd.pack_forget()
    pesquisa_artista_autor_cd.pack_forget()
    pesquisa_diretor_dvd.pack_forget()
    pesquisa_distribuidora_cd.pack_forget()
    pesquisa_distribuidora_dvd.pack_forget()

    entrada_pesquisa_livro.delete(0, END)
    entrada_pesquisa_autor.delete(0, END)
    entrada_pesquisa_editora.delete(0, END)
    entrada_pesquisa_dvd.delete(0, END)
    entrada_pesquisa_cd.delete(0, END)
    entrada_pesquisa_artista_autor.delete(0, END)
    entrada_pesquisa_diretor_dvd.delete(0, END)
    entrada_pesquisa_distribuidora_cd.delete(0, END)
    entrada_pesquisa_distribuidora_dvd.delete(0, END)

    tabela_livros.pack_forget()
    tabela_autores.pack_forget()
    tabela_editoras.pack_forget()
    tabela_dvds.pack_forget()
    tabela_cds.pack_forget()
    tabela_autores_artistas_cds.pack_forget()
    tabela_diretores_dvds.pack_forget()
    tabela_distribuidoras_cds.pack_forget()
    tabela_distribuidoras_dvds.pack_forget()

    editar_excluir_livro.pack_forget()
    botoes_editar_excluir_livro.pack_forget()
    editar_excluir_autor.pack_forget()
    botoes_editar_excluir_autor.pack_forget()
    editar_excluir_editora.pack_forget()
    botoes_editar_excluir_editora.pack_forget()
    editar_excluir_dvd.pack_forget()
    botoes_editar_excluir_dvd.pack_forget()
    editar_excluir_autor_artista_cd.pack_forget()
    botoes_editar_excluir_autor_artista_cd.pack_forget()
    editar_excluir_diretor_dvd.pack_forget()
    botoes_editar_excluir_diretor_dvd.pack_forget()
    editar_excluir_distribuidora_cd.pack_forget()
    botoes_editar_excluir_distribuidora_cd.pack_forget()
    editar_excluir_distribuidora_dvd.pack_forget()
    botoes_editar_excluir_distribuidora_dvd.pack_forget()

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
    '''
    Esta funçõa cancela a tela de registro em questão e apaga todos os valores presentes
    em seus campos de registro.
    '''
    table_frame.pack_forget()
    button_frame.pack_forget()

    if drop_down_register.get() == 'Livro':
        livro_register_frame.pack_forget()

        titulo_entry_registro_livro.delete(0, END)
        autor_entry_registro_livro.delete(0, END)
        editora_entry_registro_livro.delete(0, END)
        n_pages_entry_registro_livro.delete(0, END)
        situacao_livro.current(0)
        beneficiado_livro.delete(0, END)
        beneficiado_livro.configure(state=DISABLED)
        telefone_contato.delete(0, END)
        telefone_contato.configure(state=DISABLED)
        data_emprestimo.delete(0, END)
        data_emprestimo.configure(state=DISABLED)
        data_devolucao.delete(0, END)
        data_devolucao.configure(state=DISABLED)

    elif drop_down_register.get() == 'Autor':
        autor_register_frame.pack_forget()

        autor_entry_registro_autor.delete(0, END)

    elif drop_down_register.get() == 'Editora':
        editora_register_frame.pack_forget()

        editora_entry_registro_editora.delete(0, END)

    elif drop_down_register.get() == 'DVD':
        dvd_register_frame.pack_forget()

        titulo_dvd_registro.delete(0, END)
        diretor_dvd_registro.delete(0, END)
        distribuidora_dvd_registro.delete(0, END)
        tempo_dvd_registro.delete(0, END)
        situacao_dvd_registro.current(0)
        beneficiado_dvd_registro.delete(0, END)
        beneficiado_dvd_registro.configure(state=DISABLED)
        telefone_dvd_registro.delete(0, END)
        telefone_dvd_registro.configure(state=DISABLED)
        dt_emprestimo_dvd_registro.delete(0, END)
        dt_emprestimo_dvd_registro.configure(state=DISABLED)
        dt_devolucao_dvd_registro.delete(0, END)
        dt_devolucao_dvd_registro.configure(state=DISABLED)

    elif drop_down_register.get() == 'CD':
        cd_register_frame.pack_forget()

        titulo_cd_registro.delete(0, END)
        artista_autor_cd_registro.delete(0, END)
        distribuidora_cd_registro.delete(0, END)
        tempo_cd_registro.delete(0, END)
        situacao_cd_registro.current(0)
        beneficiado_cd_registro.delete(0, END)
        beneficiado_cd_registro.configure(state=DISABLED)
        telefone_cd_registro.delete(0, END)
        telefone_cd_registro.configure(state=DISABLED)
        dt_emprestimo_cd_registro.delete(0, END)
        dt_emprestimo_cd_registro.configure(state=DISABLED)
        dt_devolucao_cd_registro.delete(0, END)
        dt_devolucao_cd_registro.configure(state=DISABLED)

    elif drop_down_register.get() == 'Autor/Artista CD':
        autor_artista_cd_register_frame.pack_forget()

        nome_autor_artista_registro.delete(0, END)

    elif drop_down_register.get() == 'Diretor(a) DVD':
        diretor_dvd_register_frame.pack_forget()

        nome_diretor_dvd_registro.delete(0, END)

    elif drop_down_register.get() == 'Distribuidora CD':
        distribuidora_cd_register_frame.pack_forget()

        nome_distribuidora_cd_registro.delete(0, END)

    elif drop_down_register.get() == 'Distribuidora DVD':
        distribuidora_dvd_register_frame.pack_forget()

        nome_distribuidora_dvd_registro.delete(0, END)

    button_register_frame.pack_forget()

    pesquisa_livro.pack(
        expand=False,
        fill=X,
        padx=10,
        pady=10,
    )

    table_frame.pack(
        expand=True,
        fill=BOTH,
        padx=10,
        pady=10
    )

    tabela_livros.pack(
        expand=True,
        fill=BOTH,
        padx=10,
        pady=10
    )

    button_frame.pack(
        fill=X,
        expand=False,
        pady=10,
        padx=10,
        anchor=S
    )

    drop_down_register.current(0)
    drop_down.current(0)


def mudar_tela_registro(event):
    '''
    Esta função muda entre as telas de registro (livro, autor, editora)
    '''
    button_register_frame.pack_forget()

    if drop_down_register.get() == 'Livro':
        table_frame['text'] = 'Novo Livro'

        autor_register_frame.pack_forget()
        editora_register_frame.pack_forget()
        dvd_register_frame.pack_forget()
        cd_register_frame.pack_forget()
        autor_artista_cd_register_frame.pack_forget()
        diretor_dvd_register_frame.pack_forget()
        distribuidora_cd_register_frame.pack_forget()
        distribuidora_dvd_register_frame.pack_forget()

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
        dvd_register_frame.pack_forget()
        cd_register_frame.pack_forget()
        autor_artista_cd_register_frame.pack_forget()
        diretor_dvd_register_frame.pack_forget()
        distribuidora_cd_register_frame.pack_forget()
        distribuidora_dvd_register_frame.pack_forget()

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
        dvd_register_frame.pack_forget()
        cd_register_frame.pack_forget()
        autor_artista_cd_register_frame.pack_forget()
        diretor_dvd_register_frame.pack_forget()
        distribuidora_cd_register_frame.pack_forget()
        distribuidora_dvd_register_frame.pack_forget()

        editora_register_frame.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10,
            anchor=N
        )

    elif drop_down_register.get() == 'DVD':
        table_frame['text'] = 'Novo DVD'

        livro_register_frame.pack_forget()
        autor_register_frame.pack_forget()
        editora_register_frame.pack_forget()
        cd_register_frame.pack_forget()
        autor_artista_cd_register_frame.pack_forget()
        diretor_dvd_register_frame.pack_forget()
        distribuidora_cd_register_frame.pack_forget()
        distribuidora_dvd_register_frame.pack_forget()

        dvd_register_frame.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10,
            anchor=N
        )

    elif drop_down_register.get() == 'CD':
        table_frame['text'] = 'Novo CD'

        livro_register_frame.pack_forget()
        autor_register_frame.pack_forget()
        editora_register_frame.pack_forget()
        dvd_register_frame.pack_forget()
        autor_artista_cd_register_frame.pack_forget()
        diretor_dvd_register_frame.pack_forget()
        distribuidora_cd_register_frame.pack_forget()
        distribuidora_dvd_register_frame.pack_forget()

        cd_register_frame.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10,
            anchor=N
        )

    elif drop_down_register.get() == 'Autor/Artista CD':
        table_frame['text'] = 'Novo Autor/Artista CD'

        livro_register_frame.pack_forget()
        autor_register_frame.pack_forget()
        editora_register_frame.pack_forget()
        cd_register_frame.pack_forget()
        dvd_register_frame.pack_forget()
        diretor_dvd_register_frame.pack_forget()
        distribuidora_cd_register_frame.pack_forget()
        distribuidora_dvd_register_frame.pack_forget()

        autor_artista_cd_register_frame.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10,
            anchor=N
        )

    elif drop_down_register.get() == 'Diretor(a) DVD':
        table_frame['text'] = 'Novo Diretor(a) DVD'

        livro_register_frame.pack_forget()
        autor_register_frame.pack_forget()
        editora_register_frame.pack_forget()
        cd_register_frame.pack_forget()
        autor_artista_cd_register_frame.pack_forget()
        dvd_register_frame.pack_forget()
        distribuidora_cd_register_frame.pack_forget()
        distribuidora_dvd_register_frame.pack_forget()

        diretor_dvd_register_frame.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10,
            anchor=N
        )

    elif drop_down_register.get() == 'Distribuidora CD':
        table_frame['text'] = 'Nova Distribuidora CD'

        livro_register_frame.pack_forget()
        autor_register_frame.pack_forget()
        editora_register_frame.pack_forget()
        cd_register_frame.pack_forget()
        dvd_register_frame.pack_forget()
        autor_artista_cd_register_frame.pack_forget()
        diretor_dvd_register_frame.pack_forget()
        distribuidora_dvd_register_frame.pack_forget()

        distribuidora_cd_register_frame.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10,
            anchor=N
        )

    elif drop_down_register.get() == 'Distribuidora DVD':
        table_frame['text'] = 'Nova Distribuidora DVD'

        livro_register_frame.pack_forget()
        autor_register_frame.pack_forget()
        editora_register_frame.pack_forget()
        cd_register_frame.pack_forget()
        dvd_register_frame.pack_forget()
        autor_artista_cd_register_frame.pack_forget()
        diretor_dvd_register_frame.pack_forget()
        distribuidora_cd_register_frame.pack_forget()

        distribuidora_dvd_register_frame.pack(
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
    '''
    Esta função é responsável por inserir os valores digitados nos campos de registro da tela
    de registro em questão nas suas devidas tabelas. Caso qualquer dos valores seja um valor
    nulo (valor em branco) ou um valor que não condiza com o seu campo, esta função exibe uma
    mensagem de erro dizendo que algum dos valores digitados está inválido.
    '''
    if drop_down_register.get() == 'Livro':
        titulo = titulo_entry_registro_livro.get().strip()
        autor = autor_entry_registro_livro.get().strip()
        editora = editora_entry_registro_livro.get().strip()
        n_pages = n_pages_entry_registro_livro.get().strip()
        situacao = situacao_livro.get()
        beneficiado = beneficiado_livro.get().strip()
        telefone = telefone_contato.get().strip()
        dt_emprestimo = data_emprestimo.get().strip()
        dt_devolucao = data_devolucao.get().strip()

        if situacao == 'Disponível':
            if len(titulo) == 0 or len(autor) == 0 or len(editora) == 0 or len(n_pages) == 0 or not n_pages.isdigit():
                messagebox.showinfo('Valores inválidos',
                                    'Algum dos valores digitados está inválido!')
            else:
                db.add_livro(titulo, autor, editora, n_pages, situacao,
                             beneficiado, telefone, dt_emprestimo, dt_devolucao)

        else:
            if len(titulo) == 0 or len(autor) == 0 or len(editora) == 0 or len(n_pages) == 0 or not n_pages.isdigit() or len(beneficiado) == 0 or len(telefone) == 0 or len(dt_emprestimo) == 0 or len(dt_devolucao) == 0:
                messagebox.showinfo(
                    'Valores inválidos', 'Algum dos valores digitados está inválido!')

            else:
                db.add_livro(titulo, autor, editora, n_pages, situacao,
                             beneficiado, telefone, dt_emprestimo, dt_devolucao)

            titulo_entry_registro_livro.delete(0, END)
            autor_entry_registro_livro.delete(0, END)
            editora_entry_registro_livro.delete(0, END)
            n_pages_entry_registro_livro.delete(0, END)
            situacao_livro.current(0)
            beneficiado_livro.delete(0, END)
            beneficiado_livro.configure(state=DISABLED)
            telefone_contato.delete(0, END)
            telefone_contato.configure(state=DISABLED)
            data_emprestimo.delete(0, END)
            data_emprestimo.configure(state=DISABLED)
            data_devolucao.delete(0, END)
            data_devolucao.configure(state=DISABLED)

            atualiza_auto_completar()

            carrega_tabelas()
            cancelar_registro()

    elif drop_down_register.get() == 'Autor':
        autor = autor_entry_registro_autor.get().strip()

        if len(autor) == 0:
            messagebox.showinfo('Valor inválido', 'Valor digitado inválido')
        else:
            db.add_autor(autor)

            autor_entry_registro_autor.delete(0, END)

            atualiza_auto_completar()

            carrega_tabelas()
            cancelar_registro()

    elif drop_down_register.get() == 'Editora':
        editora = editora_entry_registro_editora.get().strip()

        if len(editora) == 0:
            messagebox.showinfo('Valor inválido', 'Valor digitado inválido')
        else:
            db.add_editora(editora)

            editora_entry_registro_editora.delete(0, END)

            atualiza_auto_completar()

            carrega_tabelas()
            cancelar_registro()

    elif drop_down_register.get() == 'DVD':
        titulo = titulo_dvd_registro.get().strip()
        diretor = diretor_dvd_registro.get().strip()
        distribuidora = distribuidora_dvd_registro.get().strip()
        tempo = tempo_dvd_registro.get().strip()
        situacao = situacao_dvd_registro.get().strip()
        beneficiado = beneficiado_dvd_registro.get().strip()
        telefone = telefone_dvd_registro.get().strip()
        dt_emprestimo = dt_emprestimo_dvd_registro.get().strip()
        dt_devolucao = dt_devolucao_dvd_registro.get().strip()

        if situacao == 'Disponível':

            if (len(titulo) == 0 or len(diretor) == 0 or len(distribuidora) == 0 or len(tempo) == 0):
                messagebox.showinfo(
                    'Valor inválido', 'Algum dos valores digitados está em branco')

            else:
                db.add_dvd(titulo, diretor, distribuidora, tempo, situacao,
                           beneficiado, telefone, dt_emprestimo, dt_devolucao)

        else:

            if len(titulo) == 0 or len(diretor) == 0 or len(distribuidora) == 0 or len(tempo) == 0 or len(beneficiado) == 0 or len(telefone) == 0 or len(dt_emprestimo) == 0 or len(dt_devolucao) == 0:
                messagebox.showinfo(
                    'Valor inváldio', 'Algum dos valores digitados está em branco')

            else:
                db.add_dvd(titulo, diretor, distribuidora, tempo, situacao,
                           beneficiado, telefone, dt_emprestimo, dt_devolucao)

        titulo_dvd_registro.delete(0, END)
        diretor_dvd_registro.delete(0, END)
        distribuidora_dvd_registro.delete(0, END)
        tempo_dvd_registro.delete(0, END)
        situacao_dvd_registro.current(0)
        beneficiado_dvd_registro.delete(0, END)
        beneficiado_dvd_registro.configure(state=DISABLED)
        telefone_dvd_registro.delete(0, END)
        telefone_dvd_registro.configure(state=DISABLED)
        dt_emprestimo_dvd_registro.delete(0, END)
        dt_emprestimo_dvd_registro.configure(state=DISABLED)
        dt_devolucao_dvd_registro.delete(0, END)
        dt_devolucao_dvd_registro.configure(state=DISABLED)

        atualiza_auto_completar()

        carrega_tabelas()
        cancelar_registro()

    elif drop_down_register.get() == 'CD':
        titulo = titulo_cd_registro.get().strip()
        artista_autor = artista_autor_cd_registro.get().strip()
        distribuidora = distribuidora_cd_registro.get().strip()
        tempo = tempo_cd_registro.get().strip()
        situacao = situacao_cd_registro.get().strip()
        beneficiado = beneficiado_cd_registro.get().strip()
        telefone = telefone_cd_registro.get().strip()
        dt_emprestimo = dt_emprestimo_cd_registro.get().strip()
        dt_devolucao = dt_devolucao_cd_registro.get().strip()

        if situacao == 'Disponível':

            if (len(titulo) == 0 or len(artista_autor) == 0 or len(distribuidora) == 0 or len(tempo) == 0):
                messagebox.showinfo(
                    'Valor inválido', 'Algum dos valores digitados está em branco')

            else:
                db.add_cd(titulo, artista_autor, distribuidora, tempo, situacao,
                          beneficiado, telefone, dt_emprestimo, dt_devolucao)

        else:
            if len(titulo) == 0 or len(artista_autor) == 0 or len(distribuidora) == 0 or len(tempo) == 0 or len(beneficiado) == 0 or len(telefone) == 0 or len(dt_emprestimo) == 0 or len(dt_devolucao) == 0:
                messagebox.showinfo(
                    'Valor inválido', 'Algum dos valores digitados está em branco')

            else:
                db.add_cd(titulo, artista_autor, distribuidora, tempo, situacao,
                          beneficiado, telefone, dt_emprestimo, dt_devolucao)

        titulo_cd_registro.delete(0, END)
        artista_autor_cd_registro.delete(0, END)
        distribuidora_cd_registro.delete(0, END)
        tempo_cd_registro.delete(0, END)
        situacao_cd_registro.current(0)
        beneficiado_cd_registro.delete(0, END)
        beneficiado_cd_registro.configure(state=DISABLED)
        telefone_cd_registro.delete(0, END)
        telefone_cd_registro.configure(state=DISABLED)
        dt_emprestimo_cd_registro.delete(0, END)
        dt_emprestimo_cd_registro.configure(state=DISABLED)
        dt_devolucao_cd_registro.delete(0, END)
        dt_devolucao_cd_registro.configure(state=DISABLED)

        atualiza_auto_completar()

        carrega_tabelas()
        cancelar_registro()

    elif drop_down_register.get() == 'Autor/Artista CD':
        nome_autor_artista = nome_autor_artista_registro.get().strip()

        if len(nome_autor_artista) == 0:
            messagebox.showinfo(
                'Valor inválido', 'O nome do autor possivelmente está em branco')

        else:
            db.add_autor_artista_cd(nome_autor_artista)

            nome_autor_artista_registro.delete(0, END)

            atualiza_auto_completar()

            carrega_tabelas()
            cancelar_registro()

    elif drop_down_register.get() == 'Diretor(a) DVD':
        nome_diretor = nome_diretor_dvd_registro.get().strip()

        if len(nome_diretor) == 0:
            messagebox.showinfo(
                'Valor inválido', 'O nome do autor possivelmente está em branco')

        else:
            db.add_diretor_dvd(nome_diretor)

            nome_diretor_dvd_registro.delete(0, END)

            atualiza_auto_completar()

            carrega_tabelas()
            cancelar_registro()

    elif drop_down_register.get() == 'Distribuidora CD':
        distribuidora = nome_distribuidora_cd_registro.get().strip()

        if len(distribuidora) == 0:
            messagebox.showinfo(
                'Valor inválido', 'O nome do autor possivelmente está em branco')

        else:
            db.add_distribuidora_cd(distribuidora)

            nome_distribuidora_cd_registro.delete(0, END)

            atualiza_auto_completar()

            carrega_tabelas()
            cancelar_registro()

    elif drop_down_register.get() == 'Distribuidora DVD':
        distribuidora = nome_distribuidora_dvd_registro.get().strip()

        if len(distribuidora) == 0:
            messagebox.showinfo(
                'Valor inválido', 'O nome do autor possivelmente está em branco')

        else:
            db.add_distribuidora_dvd(distribuidora)

            nome_distribuidora_dvd_registro.delete(0, END)

            atualiza_auto_completar()

            carrega_tabelas()
            cancelar_registro()


def selecionar_livro(event):
    '''
    Esta função é responsável por abrir a tela de edição/exclusão do livro selecionado em
    questão. Caso o usuário clique em qualquer local da tabela que não seja um livro uma
    mensagem será exibida informando que o usuário não clicou em nenhum livro.
    '''
    try:
        livro_selecionado = tabela_livros.item(tabela_livros.focus())['values']

        titulo_entry_editar_excluir_livro.delete(0, END)
        autor_entry_editar_excluir_livro.delete(0, END)
        editora_entry_editar_excluir_livro.delete(0, END)
        n_pages_entry_editar_excluir_livro.delete(0, END)
        beneficiado_livro_editar_excluir.delete(0, END)
        telefone_contato_editar_excluir_livro.delete(0, END)
        dt_emprestimo_livro_editar_excluir.delete(0, END)
        dt_devolucao_livro_editar_excluir.delete(0, END)

        titulo_entry_editar_excluir_livro.insert(0, livro_selecionado[1])
        autor_entry_editar_excluir_livro.insert(0, livro_selecionado[2])
        editora_entry_editar_excluir_livro.insert(0, livro_selecionado[3])
        n_pages_entry_editar_excluir_livro.insert(0, livro_selecionado[4])
        situacao_livro_editar_excluir.current(
            0 if livro_selecionado[5] == 'Disponível' else 1)

        if situacao_livro_editar_excluir.get() == 'Disponível':
            beneficiado_livro_editar_excluir.configure(state=DISABLED)
            telefone_contato_editar_excluir_livro.configure(state=DISABLED)
            dt_emprestimo_livro_editar_excluir.configure(state=DISABLED)
            dt_devolucao_livro_editar_excluir.configure(state=DISABLED)

        else:
            beneficiado_livro_editar_excluir.configure(state=NORMAL)
            beneficiado_livro_editar_excluir.insert(0, livro_selecionado[6])

            telefone_contato_editar_excluir_livro.configure(state=NORMAL)
            telefone_contato_editar_excluir_livro.insert(
                0, livro_selecionado[7])

            dt_emprestimo_livro_editar_excluir.configure(state=NORMAL)
            dt_emprestimo_livro_editar_excluir.insert(0, livro_selecionado[8])
            dt_emprestimo_livro_editar_excluir.configure(state='readonly')

            dt_devolucao_livro_editar_excluir.configure(state=NORMAL)
            dt_devolucao_livro_editar_excluir.insert(0, livro_selecionado[9])
            dt_devolucao_livro_editar_excluir.configure(state='readonly')

        pesquisa_livro.pack_forget()

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
        pass


def selecionar_autor(event):
    '''
    Esta função é responsável por abrir a tela de edição/exclusão do autor selecionado em
    questão. Caso o usuário clique em qualquer local da tabela que não seja um autor uma
    mensagem será exibida informando que o usuário não clicou em nenhum autor.
    '''
    try:
        autor_selecionado = tabela_autores.item(
            tabela_autores.focus())['values']

        autor_entry_editar_excluir_autor.delete(0, END)

        autor_entry_editar_excluir_autor.insert(0, autor_selecionado[1])

        pesquisa_autor.pack_forget()

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
        pass


def selecionar_editora(event):
    '''
    Esta função é responsável por abrir a tela de edição/exclusão da editora selecionado em
    questão. Caso o usuário clique em qualquer local da tabela que não seja uma editora uma
    mensagem será exibida informando que o usuário não clicou em nenhuma editora.
    '''
    try:
        editora_selecionada = tabela_editoras.item(
            tabela_editoras.focus())['values']

        editora_entry_editar_excluir_editora.delete(0, END)

        editora_entry_editar_excluir_editora.insert(0, editora_selecionada[1])

        pesquisa_editora.pack_forget()

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
        pass


def selecionar_dvd(event):
    try:
        dvd_selecionado = tabela_dvds.item(tabela_dvds.focus())['values']

        titulo_editar_excluir_dvd.delete(0, END)
        diretor_editar_excluir_dvd.delete(0, END)
        distribuidora_editar_excluir_dvd.delete(0, END)
        tempo_editar_excluir_dvd.delete(0, END)
        beneficiado_editar_excluir_dvd.delete(0, END)
        telefone_editar_excluir_dvd.delete(0, END)
        dt_emprestimo_editar_excluir_dvd.delete(0, END)
        dt_devolucao_editar_excluir_dvd.delete(0, END)

        titulo_editar_excluir_dvd.insert(0, dvd_selecionado[1])
        diretor_editar_excluir_dvd.insert(0, dvd_selecionado[2])
        distribuidora_editar_excluir_dvd.insert(0, dvd_selecionado[3])
        tempo_editar_excluir_dvd.insert(0, dvd_selecionado[4])
        situacao_editar_excluir_dvd.current(
            0 if dvd_selecionado[5] == 'Disponível' else 1)

        if situacao_editar_excluir_dvd.get() == 'Disponível':
            beneficiado_editar_excluir_dvd.configure(state=DISABLED)
            telefone_editar_excluir_dvd.configure(state=DISABLED)
            dt_emprestimo_cd_editar_excluir.configure(state=DISABLED)
            dt_devolucao_cd_editar_excluir.configure(state=DISABLED)

        else:
            beneficiado_editar_excluir_dvd.configure(state=NORMAL)
            beneficiado_editar_excluir_dvd.insert(0, dvd_selecionado[6])

            telefone_editar_excluir_dvd.configure(state=NORMAL)
            telefone_editar_excluir_dvd.insert(0, dvd_selecionado[7])

            dt_emprestimo_editar_excluir_dvd.configure(state=NORMAL)
            dt_emprestimo_editar_excluir_dvd.insert(0, dvd_selecionado[8])
            dt_emprestimo_editar_excluir_dvd.configure(state='readonly')

            dt_devolucao_editar_excluir_dvd.configure(state=NORMAL)
            dt_devolucao_editar_excluir_dvd.insert(0, dvd_selecionado[9])
            dt_devolucao_editar_excluir_dvd.configure(state='readonly')

        pesquisa_dvd.pack_forget()

        tabela_dvds.pack_forget()

        table_frame['text'] = 'Editar/Excluir DVD'

        editar_excluir_dvd.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10,
            anchor=N
        )

        botoes_editar_excluir_dvd.pack(
            expand=False,
            fill=X,
            padx=10,
            pady=10,
            anchor=S
        )

    except Exception as e:
        pass


def selecionar_cd(event):
    try:
        cd_selecionado = tabela_cds.item(tabela_cds.focus())['values']

        titulo_cd_editar_excluir.delete(0, END)
        autor_artista_cd_editar_excluir.delete(0, END)
        distribuidora_cd_editar_excluir.delete(0, END)
        tempo_cd_editar_excluir.delete(0, END)
        beneficiado_cd_editar_excluir.delete(0, END)
        telefone_cd_editar_excluir.delete(0, END)
        dt_emprestimo_cd_editar_excluir.delete(0, END)
        dt_devolucao_cd_editar_excluir.delete(0, END)

        titulo_cd_editar_excluir.insert(0, cd_selecionado[1])
        autor_artista_cd_editar_excluir.insert(0, cd_selecionado[2])
        distribuidora_cd_editar_excluir.insert(0, cd_selecionado[3])
        tempo_cd_editar_excluir.insert(0, cd_selecionado[4])
        situacao_cd_editar_excluir.current(
            0 if cd_selecionado[5] == 'Disponível' else 1)

        if situacao_cd_editar_excluir.get() == 'Disponível':
            beneficiado_cd_editar_excluir.configure(state=DISABLED)
            telefone_cd_editar_excluir.configure(state=DISABLED)
            dt_emprestimo_cd_editar_excluir.configure(state=DISABLED)
            dt_devolucao_cd_editar_excluir.configure(state=DISABLED)

        else:
            beneficiado_cd_editar_excluir.configure(state=NORMAL)
            beneficiado_cd_editar_excluir.insert(0, cd_selecionado[6])

            telefone_cd_editar_excluir.configure(state=NORMAL)
            telefone_cd_editar_excluir.insert(0, cd_selecionado[7])

            dt_emprestimo_cd_editar_excluir.configure(state=NORMAL)
            dt_emprestimo_cd_editar_excluir.insert(0, cd_selecionado[8])
            dt_emprestimo_cd_editar_excluir.configure(state='readonly')

            dt_devolucao_cd_editar_excluir.configure(state=NORMAL)
            dt_devolucao_cd_editar_excluir.insert(0, cd_selecionado[9])
            dt_devolucao_cd_editar_excluir.configure(state='readonly')

        pesquisa_cd.pack_forget()
        tabela_cds.pack_forget()

        table_frame['text'] = 'Editar/Excluir CD'

        editar_excluir_cd.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

        botoes_editar_excluir_cd.pack(
            expand=False,
            fill=X,
            padx=10,
            pady=10
        )

    except Exception as e:
        pass


def selecionar_artista_autor_cd(event):
    try:
        artista_autor_selecionado = tabela_autores_artistas_cds.item(
            tabela_autores_artistas_cds.focus())['values']

        nome_autor_artista_editar_excluir_cd.delete(0, END)

        nome_autor_artista_editar_excluir_cd.insert(
            0, artista_autor_selecionado[1])

        pesquisa_artista_autor_cd.pack_forget()
        tabela_autores_artistas_cds.pack_forget()

        table_frame['text'] = 'Editar/Excluir Artista/Autor CD'

        editar_excluir_autor_artista_cd.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

        botoes_editar_excluir_autor_artista_cd.pack(
            expand=False,
            fill=X,
            padx=10,
            pady=10
        )
    except Exception as e:
        pass


def selecionar_diretor_dvd(event):
    try:
        diretor_dvd_selecionado = tabela_diretores_dvds.item(
            tabela_diretores_dvds.focus())['values']

        nome_diretor_dvd_editar_excluir.delete(0, END)

        nome_diretor_dvd_editar_excluir.insert(0, diretor_dvd_selecionado[1])

        pesquisa_diretor_dvd.pack_forget()
        tabela_diretores_dvds.pack_forget()

        table_frame['text'] = 'Editar/Excluir Diretor DVD'

        editar_excluir_diretor_dvd.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

        botoes_editar_excluir_diretor_dvd.pack(
            expand=False,
            fill=X,
            padx=10,
            pady=10
        )

    except Exception as e:
        pass


def selecionar_distribuidora_cd(event):
    try:
        distribuidora_selecionada = tabela_distribuidoras_cds.item(
            tabela_distribuidoras_cds.focus())['values']

        nome_distribuidora_cd_editar_excluir.delete(0, END)

        nome_distribuidora_cd_editar_excluir.insert(
            0, distribuidora_selecionada[1])

        pesquisa_distribuidora_cd.pack_forget()
        tabela_distribuidoras_cds.pack_forget()

        table_frame['text'] = 'Editar/Excluir Distribuidora CD'

        editar_excluir_distribuidora_cd.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

        botoes_editar_excluir_distribuidora_cd.pack(
            expand=False,
            fill=X,
            padx=10,
            pady=10
        )
    except Exception as e:
        pass


def selecionar_distribuidora_dvd(event):
    try:
        distribuidora_selecionada = tabela_distribuidoras_dvds.item(
            tabela_distribuidoras_dvds.focus())['values']

        nome_distribuidora_dvd_editar_excluir.delete(0, END)

        nome_distribuidora_dvd_editar_excluir.insert(
            0, distribuidora_selecionada[1])

        pesquisa_distribuidora_dvd.pack_forget()
        tabela_distribuidoras_dvds.pack_forget()

        table_frame['text'] = 'Editar/Excluir Distribuidora DVD'

        editar_excluir_distribuidora_dvd.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

        botoes_editar_excluir_distribuidora_dvd.pack(
            expand=False,
            fill=X,
            padx=10,
            pady=10
        )
    except Exception as e:
        pass


def editar_livro():
    '''
    Esta função é responsável por pegar os valores digitados na tela de edição/exclusão do livro
    em questão e fazer o processo de edição do mesmo. Caso algum dos valores digitados for um valor
    nulo (em branco) ou um valor que não corresponda ao seu tipo o usuário receberá uma mensagem de
    erro informando que algum dos valores não foi digitado corretamente.
    '''
    livro_selecionado = tabela_livros.item(tabela_livros.focus())['values']

    titulo = titulo_entry_editar_excluir_livro.get().strip()
    autor = autor_entry_editar_excluir_livro.get().strip()
    editora = editora_entry_editar_excluir_livro.get().strip()
    n_paginas = n_pages_entry_editar_excluir_livro.get().strip()
    situacao = situacao_livro_editar_excluir.get().strip()
    beneficiado = beneficiado_livro_editar_excluir.get().strip()
    telefone = telefone_contato_editar_excluir_livro.get().strip()
    dt_emprestimo = dt_emprestimo_livro_editar_excluir.get().strip()
    dt_devolucao = dt_devolucao_livro_editar_excluir.get().strip()

    id_livro_selecionado = livro_selecionado[0]
    autor_livro_selecionado = livro_selecionado[2]
    editora_livro_selecionado = livro_selecionado[3]

    if situacao == 'Disponível':

        if len(titulo) == 0 or len(autor) == 0 or len(editora) == 0 or len(n_paginas) == 0 or not n_paginas.isdigit():
            messagebox.showinfo(
                'Valores inválidos', 'Algum dos valores digitados é um valor inválido ou está em branco')

        else:

            db.editar_livro(
                id_livro_selecionado,
                titulo,
                autor_livro_selecionado,
                autor,
                editora_livro_selecionado,
                editora,
                n_paginas,
                situacao,
                beneficiado,
                telefone,
                dt_emprestimo,
                dt_devolucao
            )

            atualiza_auto_completar()

            cancelar_edicao_livro()

            carrega_tabelas()
    else:

        if len(titulo) == 0 or len(autor) == 0 or len(editora) == 0 or len(n_paginas) == 0 or not n_paginas.isdigit() or len(beneficiado) == 0 or len(telefone) == 0 or len(dt_emprestimo) == 0 or len(dt_devolucao) == 0:
            messagebox.showinfo(
                'Valores inválidos', 'Algum dos valores digitados é um valor inválido ou está em branco')

        else:
            db.editar_livro(
                id_livro_selecionado,
                titulo,
                autor_livro_selecionado,
                autor,
                editora_livro_selecionado,
                editora,
                n_paginas,
                situacao,
                beneficiado,
                telefone,
                dt_emprestimo,
                dt_devolucao
            )

            atualiza_auto_completar()

            cancelar_edicao_livro()

            carrega_tabelas()


def cancelar_edicao_livro():
    '''
    Esta função fecha a tela de edição, limpa todos os campos da mesma e retira o livro selecionado
    do foco do programa.
    '''
    tabela_livros.selection_remove(tabela_livros.focus())

    tabela_livros.focus('')

    titulo_entry_editar_excluir_livro.delete(0, END)
    autor_entry_editar_excluir_livro.delete(0, END)
    editora_entry_editar_excluir_livro.delete(0, END)
    n_pages_entry_editar_excluir_livro.delete(0, END)

    editar_excluir_livro.pack_forget()
    botoes_editar_excluir_livro.pack_forget()

    table_frame.pack_forget()
    button_frame.pack_forget()

    pesquisa_livro.pack(
        expand=False,
        fill=X,
        padx=10,
        pady=10
    )

    table_frame['text'] = 'Livros'

    table_frame.pack(
        fill=BOTH,
        padx=10,
        pady=10,
        expand=True
    )

    tabela_livros.pack(
        expand=True,
        fill=BOTH,
        padx=10,
        pady=10
    )

    button_frame.pack(
        expand=False,
        fill=X,
        padx=10,
        pady=10
    )

    drop_down.current(0)


def excluir_livro():
    '''
    Esta função exclui o livro selecionado.
    '''
    livro_selecionado = tabela_livros.item(tabela_livros.focus())['values']

    id_livro = livro_selecionado[0]
    autor_livro = livro_selecionado[2]
    editora_livro = livro_selecionado[3]

    db.excluir_livro(id_livro, autor_livro, editora_livro)

    atualiza_auto_completar()

    cancelar_edicao_livro()

    carrega_tabelas()


def editar_autor():
    '''
    Esta função é responsável por pegar os valores digitados na tela de edição/exclusão do autor
    em questão e fazer o processo de edição do mesmo. Caso algum dos valores digitados for um valor
    nulo (em branco) ou um valor que não corresponda ao seu tipo o usuário receberá uma mensagem de
    erro informando que algum dos valores não foi digitado corretamente.
    '''
    id_autor_selecionado, nome_autor_selecionado = tabela_autores.item(
        tabela_autores.focus())['values']

    novo_autor = autor_entry_editar_excluir_autor.get().strip()

    if len(novo_autor) == 0:
        messagebox.showinfo(
            'Valor inválido', 'O valor digitado para nome do autor está em branco')
    else:
        db.editar_autor_livro(id_autor_selecionado,
                              nome_autor_selecionado, novo_autor)

        atualiza_auto_completar()

        cancelar_edicao_autor()

        carrega_tabelas()


def cancelar_edicao_autor():
    '''
    Esta função fecha a tela de edição, limpa todos os campos da mesma e retira o autor selecionado
    do foco do programa.
    '''
    tabela_autores.selection_remove(tabela_autores.focus())

    tabela_autores.focus('')

    autor_entry_editar_excluir_autor.delete(0, END)

    editar_excluir_autor.pack_forget()
    botoes_editar_excluir_autor.pack_forget()

    table_frame.pack_forget()
    button_frame.pack_forget()

    pesquisa_livro.pack(
        expand=False,
        fill=X,
        padx=10,
        pady=10
    )

    table_frame['text'] = 'Livros'

    table_frame.pack(
        fill=BOTH,
        padx=10,
        pady=10,
        expand=True
    )

    tabela_livros.pack(
        expand=True,
        fill=BOTH,
        padx=10,
        pady=10
    )

    button_frame.pack(
        expand=False,
        fill=X,
        padx=10,
        pady=10
    )

    drop_down.current(0)


def editar_editora():
    '''
    Esta função é responsável por pegar os valores digitados na tela de edição/exclusão da editora
    em questão e fazer o processo de edição do mesmo. Caso algum dos valores digitados for um valor
    nulo (em branco) ou um valor que não corresponda ao seu tipo o usuário receberá uma mensagem de
    erro informando que algum dos valores não foi digitado corretamente.
    '''
    id_editora_selecionada, nome_editora_selecionada = tabela_editoras.item(
        tabela_editoras.focus())['values']

    nova_editora = editora_entry_editar_excluir_editora.get().strip()

    if len(nova_editora) == 0:
        messagebox.showinfo(
            'Valor inválido', 'Valores digitado está em branco')

    else:
        db.editar_editora_livro(
            id_editora_selecionada, nome_editora_selecionada, nova_editora)

        atualiza_auto_completar()

        cancelar_edicao_editora()

        carrega_tabelas()


def cancelar_edicao_editora():
    '''
    Esta função fecha a tela de edição, limpa todos os campos da mesma e retira a editora selecionada
    do foco do programa.
    '''
    tabela_editoras.selection_remove(tabela_editoras.focus())

    tabela_editoras.focus('')

    editora_entry_editar_excluir_editora.delete(0, END)

    editar_excluir_editora.pack_forget()
    botoes_editar_excluir_editora.pack_forget()

    table_frame.pack_forget()
    button_frame.pack_forget()

    pesquisa_livro.pack(
        expand=False,
        fill=X,
        padx=10,
        pady=10
    )

    table_frame['text'] = 'Livros'

    table_frame.pack(
        fill=BOTH,
        padx=10,
        pady=10,
        expand=True
    )

    tabela_livros.pack(
        expand=True,
        fill=BOTH,
        padx=10,
        pady=10
    )

    button_frame.pack(
        expand=False,
        fill=X,
        padx=10,
        pady=10
    )

    drop_down.current(0)


def editar_dvd():
    dvd_selecionado = tabela_dvds.item(tabela_dvds.focus())['values']

    id_dvd_selecionado = dvd_selecionado[0]
    diretor_dvd_selecionado = dvd_selecionado[2]
    distribuidora_dvd_selecionado = dvd_selecionado[3]

    titulo = titulo_editar_excluir_dvd.get().strip()
    diretor = diretor_editar_excluir_dvd.get().strip()
    distribuidora = distribuidora_editar_excluir_dvd.get().strip()
    tempo = tempo_editar_excluir_dvd.get().strip()
    situacao = situacao_editar_excluir_dvd.get()
    beneficiado = beneficiado_editar_excluir_dvd.get().strip()
    telefone = telefone_editar_excluir_dvd.get().strip()
    dt_emprestimo = dt_emprestimo_editar_excluir_dvd.get()
    dt_devolucao = dt_devolucao_editar_excluir_dvd.get()

    if situacao == 'Disponível':

        if len(titulo) == 0 or len(diretor) == 0 or len(distribuidora) == 0 or len(tempo) == 0:
            messagebox.showinfo('Valores inválidos',
                                'Algum dos valores digitados pode estar em branco')

        else:
            db.editar_dvd(
                id_dvd_selecionado,
                titulo,
                diretor_dvd_selecionado,
                diretor,
                distribuidora_dvd_selecionado,
                distribuidora,
                tempo,
                situacao,
                beneficiado,
                telefone,
                dt_emprestimo,
                dt_devolucao
            )
            atualiza_auto_completar()

            carrega_tabelas()

            cancelar_edicao_dvd()
    else:

        if len(titulo) == 0 or len(diretor) == 0 or len(distribuidora) == 0 or len(tempo) == 0 or len(beneficiado) == 0 or len(telefone) == 0 or len(dt_emprestimo) == 0 or len(dt_devolucao) == 0:
            messagebox.showinfo(
                'Valores inválidos', 'Algum dos valores digitados pode estar em branco')

        else:
            db.editar_dvd(
                id_dvd_selecionado,
                titulo,
                diretor_dvd_selecionado,
                diretor,
                distribuidora_dvd_selecionado,
                distribuidora,
                tempo,
                situacao,
                beneficiado,
                telefone,
                dt_emprestimo,
                dt_devolucao
            )

            atualiza_auto_completar()

            carrega_tabelas()

            cancelar_edicao_dvd()


def excluir_dvd():
    dvd_selecionado = tabela_dvds.item(tabela_dvds.focus())['values']

    id = dvd_selecionado[0]
    diretor = dvd_selecionado[2]
    distribuidora = dvd_selecionado[3]

    db.excluir_dvd(id, diretor, distribuidora)

    atualiza_auto_completar()

    carrega_tabelas()

    cancelar_edicao_dvd()


def cancelar_edicao_dvd():
    tabela_dvds.selection_remove(tabela_dvds.focus())

    tabela_dvds.focus('')

    titulo_editar_excluir_dvd.delete(0, END)
    diretor_editar_excluir_dvd.delete(0, END)
    distribuidora_editar_excluir_dvd.delete(0, END)
    tempo_editar_excluir_dvd.delete(0, END)
    situacao_editar_excluir_dvd.delete(0, END)
    beneficiado_editar_excluir_dvd.delete(0, END)
    telefone_editar_excluir_dvd.delete(0, END)
    dt_emprestimo_editar_excluir_dvd.delete(0, END)
    dt_devolucao_editar_excluir_dvd.delete(0, END)

    editar_excluir_dvd.pack_forget()
    botoes_editar_excluir_dvd.pack_forget()

    table_frame.pack_forget()
    button_frame.pack_forget()

    pesquisa_livro.pack(
        expand=False,
        fill=X,
        padx=10,
        pady=10
    )

    table_frame['text'] = 'Livros'

    table_frame.pack(
        fill=BOTH,
        padx=10,
        pady=10,
        expand=True
    )

    tabela_livros.pack(
        expand=True,
        fill=BOTH,
        padx=10,
        pady=10
    )

    button_frame.pack(
        expand=False,
        fill=X,
        padx=10,
        pady=10
    )

    drop_down.current(0)


def editar_cd():
    cd_selecionado = tabela_cds.item(tabela_cds.focus())['values']

    id_cd_selecionado = cd_selecionado[0]
    autor_artista_cd_selecionado = cd_selecionado[2]
    distribuidora_cd_selecionado = cd_selecionado[3]

    titulo = titulo_cd_editar_excluir.get().strip()
    autor_artista = autor_artista_cd_editar_excluir.get().strip()
    distribuidora = distribuidora_cd_editar_excluir.get().strip()
    tempo = tempo_cd_editar_excluir.get().strip()
    situacao = situacao_cd_editar_excluir.get()
    beneficiado = beneficiado_cd_editar_excluir.get().strip()
    telefone = telefone_cd_editar_excluir.get().strip()
    dt_emprestimo = dt_emprestimo_cd_editar_excluir.get().strip()
    dt_devolucao = dt_devolucao_cd_editar_excluir.get().strip()

    if situacao == 'Disponível':

        if len(titulo) == 0 or len(autor_artista) == 0 or len(distribuidora) == 0 or len(tempo) == 0:
            messagebox.showinfo('Valores inválidos',
                                'Algum dos valores digitados está vazio')

        else:
            db.editar_cd(
                id_cd_selecionado,
                titulo,
                autor_artista_cd_selecionado,
                autor_artista,
                distribuidora_cd_selecionado,
                distribuidora,
                tempo,
                situacao,
                beneficiado,
                telefone,
                dt_emprestimo,
                dt_devolucao
            )

            atualiza_auto_completar()

            carrega_tabelas()

            cancelar_edicao_cd()
    else:
        if len(titulo) == 0 or len(autor_artista) == 0 or len(distribuidora) == 0 or len(tempo) == 0 or len(beneficiado) == 0 or len(telefone) == 0 or len(dt_emprestimo) == 0 or len(dt_devolucao) == 0:
            messagebox.showinfo('Valores inválidos',
                                'Algum dos valores digitados está vazio')

        else:
            db.editar_cd(
                id_cd_selecionado,
                titulo,
                autor_artista_cd_selecionado,
                autor_artista,
                distribuidora_cd_selecionado,
                distribuidora,
                tempo,
                situacao,
                beneficiado,
                telefone,
                dt_emprestimo,
                dt_devolucao
            )

            atualiza_auto_completar()

            carrega_tabelas()

            cancelar_edicao_cd()


def excluir_cd():
    cd_selecionado = tabela_cds.item(tabela_cds.focus())['values']

    id = cd_selecionado[0]
    autor_artista = cd_selecionado[2]
    distribuidora = cd_selecionado[3]

    db.excluir_cd(id, autor_artista, distribuidora)

    atualiza_auto_completar()

    carrega_tabelas()

    cancelar_edicao_cd()


def cancelar_edicao_cd():
    tabela_cds.selection_remove(tabela_dvds.focus())

    tabela_cds.focus('')

    titulo_cd_editar_excluir.delete(0, END)
    autor_artista_cd_editar_excluir.delete(0, END)
    distribuidora_cd_editar_excluir.delete(0, END)
    tempo_cd_editar_excluir.delete(0, END)
    beneficiado_cd_editar_excluir.delete(0, END)
    telefone_cd_editar_excluir.delete(0, END)
    dt_emprestimo_cd_editar_excluir.delete(0, END)
    dt_devolucao_cd_editar_excluir.delete(0, END)

    editar_excluir_cd.pack_forget()
    botoes_editar_excluir_cd.pack_forget()

    table_frame.pack_forget()
    button_frame.pack_forget()

    pesquisa_livro.pack(
        expand=False,
        fill=X,
        padx=10,
        pady=10
    )

    table_frame['text'] = 'Livros'

    table_frame.pack(
        fill=BOTH,
        padx=10,
        pady=10,
        expand=True
    )

    tabela_livros.pack(
        expand=True,
        fill=BOTH,
        padx=10,
        pady=10
    )

    button_frame.pack(
        expand=False,
        fill=X,
        padx=10,
        pady=10
    )

    drop_down.current(0)


def editar_artista_autor_cd():
    artista_autor_selecionado = tabela_autores_artistas_cds.item(
        tabela_autores_artistas_cds.focus())['values'][1]

    novo_artista_autor = nome_autor_artista_editar_excluir_cd.get().strip()

    if len(novo_artista_autor) == 0:
        messagebox('Valor digitado inválido', 'Nome do artista está em branco')

    else:
        db.editar_autor_artista_cd(
            artista_autor_selecionado, novo_artista_autor)

        atualiza_auto_completar()

        carrega_tabelas()

        cancelar_edicao_artista_autor_cd()


def cancelar_edicao_artista_autor_cd():
    tabela_autores_artistas_cds.selection_remove(
        tabela_autores_artistas_cds.focus())

    tabela_autores_artistas_cds.focus('')

    nome_autor_artista_editar_excluir_cd.delete(0, END)

    editar_excluir_autor_artista_cd.pack_forget()
    botoes_editar_excluir_autor_artista_cd.pack_forget()

    table_frame.pack_forget()
    button_frame.pack_forget()

    pesquisa_livro.pack(
        expand=False,
        fill=X,
        padx=10,
        pady=10
    )

    table_frame['text'] = 'Livros'

    table_frame.pack(
        fill=BOTH,
        padx=10,
        pady=10,
        expand=True
    )

    tabela_livros.pack(
        expand=True,
        fill=BOTH,
        padx=10,
        pady=10
    )

    button_frame.pack(
        expand=False,
        fill=X,
        padx=10,
        pady=10
    )

    drop_down.current(0)


def editar_diretor_dvd():
    diretor_selecionado = tabela_diretores_dvds.item(
        tabela_diretores_dvds.focus())['values'][1]

    novo_diretor = nome_diretor_dvd_editar_excluir.get().strip()

    if len(novo_diretor) == 0:
        messagebox.showinfo('Valor inválido', 'Valor digitado está em branco')

    else:
        db.editar_diretor_dvd(diretor_selecionado, novo_diretor)

        atualiza_auto_completar()

        carrega_tabelas()

        cancelar_edicao_diretor_dvd()


def cancelar_edicao_diretor_dvd():
    tabela_diretores_dvds.selection_remove(tabela_diretores_dvds.focus())
    tabela_diretores_dvds.focus('')

    nome_diretor_dvd_editar_excluir.delete(0, END)

    editar_excluir_diretor_dvd.pack_forget()
    botoes_editar_excluir_diretor_dvd.pack_forget()

    table_frame.pack_forget()
    button_frame.pack_forget()

    pesquisa_livro.pack(
        expand=False,
        fill=X,
        padx=10,
        pady=10
    )

    table_frame['text'] = 'Livros'

    table_frame.pack(
        fill=BOTH,
        padx=10,
        pady=10,
        expand=True
    )

    tabela_livros.pack(
        expand=True,
        fill=BOTH,
        padx=10,
        pady=10
    )

    button_frame.pack(
        expand=False,
        fill=X,
        padx=10,
        pady=10
    )

    drop_down.current(0)


def editar_distribuidora_cd():
    distribuidora_selecionada = tabela_distribuidoras_cds.item(
        tabela_distribuidoras_cds.focus())['values'][1]

    nova_distribuidora = nome_distribuidora_cd_editar_excluir.get().strip()

    if len(nova_distribuidora) == 0:
        messagebox.showinfo('Valor inválido', 'Valor digitado está em branco')

    else:
        db.editar_distribuidora_cd(
            distribuidora_selecionada, nova_distribuidora)

        atualiza_auto_completar()

        carrega_tabelas()

        cancelar_edicao_distribuidora_cd()


def cancelar_edicao_distribuidora_cd():
    tabela_distribuidoras_cds.selection_remove(
        tabela_distribuidoras_cds.focus())
    tabela_distribuidoras_cds.focus('')

    nome_distribuidora_cd_editar_excluir.delete(0, END)

    editar_excluir_distribuidora_cd.pack_forget()
    botoes_editar_excluir_distribuidora_cd.pack_forget()

    table_frame.pack_forget()
    button_frame.pack_forget()

    pesquisa_livro.pack(
        expand=False,
        fill=X,
        padx=10,
        pady=10
    )

    table_frame['text'] = 'Livros'

    table_frame.pack(
        fill=BOTH,
        padx=10,
        pady=10,
        expand=True
    )

    tabela_livros.pack(
        expand=True,
        fill=BOTH,
        padx=10,
        pady=10
    )

    button_frame.pack(
        expand=False,
        fill=X,
        padx=10,
        pady=10
    )

    drop_down.current(0)


def editar_distribuidora_dvd():
    distribuidora_selecionada = tabela_distribuidoras_dvds.item(
        tabela_distribuidoras_dvds.focus())['values'][1]
    nova_distribuidora = nome_distribuidora_dvd_editar_excluir.get().strip()

    if len(nova_distribuidora) == 0:
        messagebox.showinfo('Valor inválido', 'Nome de distribuidora vazio')

    else:
        db.editar_distribuidora_dvd(
            distribuidora_selecionada, nova_distribuidora)

        atualiza_auto_completar()

        carrega_tabelas()

        cancelar_edicao_distribuidora_dvd()


def cancelar_edicao_distribuidora_dvd():
    tabela_distribuidoras_dvds.selection_remove(
        tabela_distribuidoras_dvds.focus())
    tabela_distribuidoras_dvds.focus('')

    nome_distribuidora_dvd_editar_excluir.delete(0, END)

    editar_excluir_distribuidora_dvd.pack_forget()
    botoes_editar_excluir_distribuidora_dvd.pack_forget()

    table_frame.pack_forget()
    button_frame.pack_forget()

    pesquisa_livro.pack(
        expand=False,
        fill=X,
        padx=10,
        pady=10
    )

    table_frame['text'] = 'Livros'

    table_frame.pack(
        fill=BOTH,
        padx=10,
        pady=10,
        expand=True
    )

    tabela_livros.pack(
        expand=True,
        fill=BOTH,
        padx=10,
        pady=10
    )

    button_frame.pack(
        expand=False,
        fill=X,
        padx=10,
        pady=10
    )

    drop_down.current(0)


def atualiza_auto_completar():
    '''
    Esta função atualiza todos os campos de auto-completar presentes no programa.
    '''
    autor_entry_registro_livro['completevalues'] = db.nome_autores()
    autor_entry_registro_autor['completevalues'] = db.nome_autores()
    autor_entry_editar_excluir_livro['completevalues'] = db.nome_autores(
    )
    autor_entry_editar_excluir_autor['completevalues'] = db.nome_autores(
    )

    editora_entry_registro_livro['completevalues'] = db.nome_editoras()
    editora_entry_registro_editora['completevalues'] = db.nome_editoras()
    editora_entry_editar_excluir_livro['completevalues'] = db.nome_editoras(
    )
    editora_entry_editar_excluir_editora['completevalues'] = db.nome_editoras(
    )

    artista_autor_cd_registro['completevalues'] = db.nome_autores_artistas_cds(
    )
    nome_autor_artista_registro['completevalues'] = db.nome_autores_artistas_cds(
    )
    autor_artista_cd_editar_excluir['completevalues'] = db.nome_autores_artistas_cds(
    )
    nome_autor_artista_editar_excluir_cd['completevalues'] = db.nome_autores_artistas_cds(
    )

    diretor_dvd_registro['completevalues'] = db.nome_diretores_dvds()
    nome_diretor_dvd_registro['completevalues'] = db.nome_diretores_dvds()
    diretor_editar_excluir_dvd['completevalues'] = db.nome_diretores_dvds()
    nome_diretor_dvd_editar_excluir['completevalues'] = db.nome_diretores_dvds(
    )

    distribuidora_cd_registro['completevalues'] = db.nome_distribuidoras_cds()
    nome_distribuidora_cd_registro['completevalues'] = db.nome_distribuidoras_cds(
    )
    distribuidora_cd_editar_excluir['completevalues'] = db.nome_distribuidoras_cds(
    )
    nome_distribuidora_cd_editar_excluir['completevalues'] = db.nome_distribuidoras_cds(
    )

    distribuidora_dvd_registro['completevalues'] = db.nome_distribuidoras_dvds(
    )
    nome_distribuidora_dvd_registro['completevalues'] = db.nome_distribuidoras_dvds(
    )
    distribuidora_editar_excluir_dvd['completevalues'] = db.nome_distribuidoras_dvds(
    )
    nome_distribuidora_dvd_editar_excluir['completevalues'] = db.nome_distribuidoras_dvds(
    )

    entrada_pesquisa_livro['completevalues'] = db.titulo_livros()
    entrada_pesquisa_autor['completevalues'] = db.nome_autores()
    entrada_pesquisa_editora['completevalues'] = db.nome_editoras()
    entrada_pesquisa_cd['completevalues'] = db.titulos_cds()
    entrada_pesquisa_dvd['completevalues'] = db.titulos_dvds()
    entrada_pesquisa_artista_autor['completevalues'] = db.nome_autores_artistas_cds(
    )
    entrada_pesquisa_diretor_dvd['completevalues'] = db.nome_diretores_dvds()
    entrada_pesquisa_distribuidora_cd['completevalues'] = db.nome_distribuidoras_cds(
    )
    entrada_pesquisa_distribuidora_dvd['completevalues'] = db.nome_distribuidoras_dvds(
    )


def muda_opcao_pesquisa_livro(e):
    '''
    Muda os valores de auto completar do programa de acordo com a opção escolhida.
    '''
    if opcao_pesquisa_livro.get() == 'Título (Todos)':
        entrada_pesquisa_livro['completevalues'] = db.titulo_livros()

    elif opcao_pesquisa_livro.get() == 'Autor (Todos)':
        entrada_pesquisa_livro['completevalues'] = db.nome_autores()

    elif opcao_pesquisa_livro.get() == 'Editora (Todos)':
        entrada_pesquisa_livro['completevalues'] = db.nome_editoras()

    elif opcao_pesquisa_livro.get() == 'Título (Disponíveis)':
        entrada_pesquisa_livro['completevalues'] = db.titulos_livros_disponiveis(
        )

    elif opcao_pesquisa_livro.get() == 'Autor (Disponíveis)':
        entrada_pesquisa_livro['completevalues'] = db.autores_livros_disponiveis(
        )

    elif opcao_pesquisa_livro.get() == 'Editora (Disponíveis)':
        entrada_pesquisa_livro['completevalues'] = db.editoras_livros_disponiveis(
        )

    elif opcao_pesquisa_livro.get() == 'Título (Emprestados)':
        entrada_pesquisa_livro['completevalues'] = db.titulos_livros_emprestados(
        )

    elif opcao_pesquisa_livro.get() == 'Autor (Emprestados)':
        entrada_pesquisa_livro['completevalues'] = db.autores_livros_emprestados(
        )

    elif opcao_pesquisa_livro.get() == 'Editora (Emprestados)':
        entrada_pesquisa_livro['completevalues'] = db.editoras_livros_emprestados(
        )

    elif opcao_pesquisa_livro.get() == 'Título (Empréstimo Expirado)':
        entrada_pesquisa_livro['completevalues'] = db.titulos_livros_emprestimo_expirado(
        )

        set_emprestimos_expirados_livros()

    elif opcao_pesquisa_livro.get() == 'Autor (Empréstimo Expirado)':
        entrada_pesquisa_livro['completevalues'] = db.autores_livros_emprestimo_expirado(
        )

        set_emprestimos_expirados_livros()

    elif opcao_pesquisa_livro.get() == 'Editora (Empréstimo Expirado)':
        entrada_pesquisa_livro['completevalues'] = db.editoras_livros_emprestimo_expirado(
        )

        set_emprestimos_expirados_livros()

    elif opcao_pesquisa_livro.get() == 'Beneficiado':
        entrada_pesquisa_livro['completevalues'] = db.beneficiados_livros()


def set_emprestimos_expirados_livros():
    livros = db.get_livros_emprestimos_expirados()

    for livro in tabela_livros.get_children():
        tabela_livros.delete(livro)

    count = 0

    for livro in livros:
        id = livro[0]
        titulo = livro[1]
        autor = livro[2]
        editora = livro[3]
        n_pag = livro[4]
        situacao = livro[5]
        beneficiado = livro[6]
        telefone = livro[7]
        dt_emprestimo = livro[8]
        dt_devolucao = livro[9]

        if count % 2 == 0:
            tabela_livros.insert(
                '',
                END,
                values=(
                    id,
                    titulo,
                    autor,
                    editora,
                    n_pag,
                    situacao,
                    beneficiado,
                    telefone,
                    dt_emprestimo,
                    dt_devolucao
                ),
                tags=('evenrow',)
            )

        else:
            tabela_livros.insert(
                '',
                END,
                values=(
                    id,
                    titulo,
                    autor,
                    editora,
                    n_pag,
                    situacao,
                    beneficiado,
                    telefone,
                    dt_emprestimo,
                    dt_devolucao
                ),
                tags=('oddrow',)
            )

        count += 1


def muda_opcao_pesquisa_cd(e):
    if opcao_pesquisa_cd.get() == 'Título (Todos)':
        entrada_pesquisa_cd['completevalues'] = db.titulos_cds()

    elif opcao_pesquisa_cd.get() == 'Artista/Autor (Todos)':
        entrada_pesquisa_cd['completevalues'] = db.nome_autores_artistas_cds()

    elif opcao_pesquisa_cd.get() == 'Distribuidora (Todos)':
        entrada_pesquisa_cd['completevalues'] = db.nome_distribuidoras_cds()

    elif opcao_pesquisa_cd.get() == 'Título (Disponíveis)':
        entrada_pesquisa_cd['completevalues'] = db.titulos_cds_disponiveis()

    elif opcao_pesquisa_cd.get() == 'Artista/Autor (Disponíveis)':
        entrada_pesquisa_cd['completevalues'] = db.autores_artistas_cds_disponiveis(
        )

    elif opcao_pesquisa_cd.get() == 'Distribuidora (Disponíveis)':
        entrada_pesquisa_cd['completevalues'] = db.distribuidoras_cds_disponiveis(
        )

    elif opcao_pesquisa_cd.get() == 'Título (Emprestados)':
        entrada_pesquisa_cd['completevalues'] = db.titulos_cds_emprestados()

    elif opcao_pesquisa_cd.get() == 'Artista/Autor (Emprestados)':
        entrada_pesquisa_cd['completevalues'] = db.autores_artistas_cds_emprestados(
        )

    elif opcao_pesquisa_cd.get() == 'Distribuidora (Emprestados)':
        entrada_pesquisa_cd['completevalues'] = db.distribuidoras_cds_emprestados(
        )

    elif opcao_pesquisa_cd.get() == 'Título (Empréstimo Expirado)':
        entrada_pesquisa_cd['completevalues'] = db.titulos_cds_emprestimo_expirado(
        )

        set_emprestimos_expirados_cds()

    elif opcao_pesquisa_cd.get() == 'Artista/Autor (Empréstimo Expirado)':
        entrada_pesquisa_cd['completevalues'] = db.autores_artistas_cds_emprestimo_expirado(
        )
        set_emprestimos_expirados_cds()

    elif opcao_pesquisa_cd.get() == 'Distribuidoras (Empréstimo Expirado)':
        entrada_pesquisa_cd['completevalues'] = db.distribuidoras_cds_emprestimo_expirado(
        )
        set_emprestimos_expirados_cds()

    elif opcao_pesquisa_cd.get() == 'Beneficiado':
        entrada_pesquisa_cd['completevalues'] = db.beneficiados_cds()


def set_emprestimos_expirados_cds():
    cds = db.get_cds_emprestimos_expirados()

    for cd in tabela_cds.get_children():
        tabela_cds.delete(cd)

    count = 0

    for cd in cds:
        id = cds[0]
        titulo = cds[1]
        artista_autor = cds[2]
        distribuidora = cds[3]
        tempo = cds[4]
        situacao = cds[5]
        beneficiado = cds[6]
        telefone = cds[7]
        dt_emprestimo = cds[8]
        dt_devolucao = cds[9]

        if count % 2 == 0:
            tabela_cds.insert(
                '',
                END,
                values=(
                    id,
                    titulo,
                    artista_autor,
                    distribuidora,
                    tempo,
                    situacao,
                    beneficiado,
                    telefone,
                    dt_emprestimo,
                    dt_devolucao
                ),
                tags=('evenrow',)
            )

        else:
            tabela_cds.insert(
                '',
                END,
                values=(
                    id,
                    titulo,
                    artista_autor,
                    distribuidora,
                    tempo,
                    situacao,
                    beneficiado,
                    telefone,
                    dt_emprestimo,
                    dt_devolucao
                ),
                tags=('oddrow',)
            )

        count += 1


def muda_opcao_pesquisa_dvd(e):
    if opcao_pesquisa_dvd.get() == 'Título (Todos)':
        entrada_pesquisa_dvd['completevalues'] = db.titulos_dvds()

    elif opcao_pesquisa_dvd.get() == 'Diretor (Todos)':
        entrada_pesquisa_dvd['completevalues'] = db.nome_diretores_dvds()

    elif opcao_pesquisa_dvd.get() == 'Distribuidora (Todos)':
        entrada_pesquisa_dvd['completevalues'] = db.nome_distribuidoras_dvds()

    elif opcao_pesquisa_dvd.get() == 'Título (Disponíveis)':
        entrada_pesquisa_dvd['completevalues'] = db.titulos_dvds_disponiveis()

    elif opcao_pesquisa_dvd.get() == 'Diretor (Disponíveis)':
        entrada_pesquisa_dvd['completevalues'] = db.diretores_dvds_disponiveis()

    elif opcao_pesquisa_dvd.get() == 'Distribuidora (Disponíveis)':
        entrada_pesquisa_dvd['completevalues'] = db.distribuidoras_dvds_disponiveis(
        )

    elif opcao_pesquisa_dvd.get() == 'Título (Emprestados)':
        entrada_pesquisa_dvd['completevalues'] = db.titulos_dvds_emprestados()

    elif opcao_pesquisa_dvd.get() == 'Diretor (Emprestados)':
        entrada_pesquisa_dvd['completevalues'] = db.diretores_dvds_emprestados()

    elif opcao_pesquisa_dvd.get() == 'Distribuidora (Emprestados)':
        entrada_pesquisa_dvd['completevalues'] = db.distribuidoras_dvds_emprestados(
        )

    elif opcao_pesquisa_dvd.get() == 'Título (Empréstimo Expirado)':
        entrada_pesquisa_dvd['completevalues'] = db.titulos_dvds_emprestimo_expirado(
        )
        set_emprestimos_expirados_dvds()

    elif opcao_pesquisa_dvd.get() == 'Diretor (Empréstimo Expirado)':
        entrada_pesquisa_dvd['completevalues'] = db.diretores_dvds_emprestimo_expirado(
        )
        set_emprestimos_expirados_dvds()

    elif opcao_pesquisa_dvd.get() == 'Distribuidora (Empréstimo Expirado)':
        entrada_pesquisa_dvd['completevalues'] = db.distribuidoras_dvds_emprestimo_expirado(
        )
        set_emprestimos_expirados_dvds()

    elif opcao_pesquisa_dvd.get() == 'Beneficiado':
        entrada_pesquisa_dvd['completevalues'] = db.beneficiados_dvds()


def set_emprestimos_expirados_dvds():
    dvds = db.get_dvds_emprestimos_expirados()

    for dvd in tabela_dvds.get_children():
        tabela_dvds.delete(dvd)

    count = 0

    for dvd in dvds:
        id = dvd[0]
        titulo = dvd[1]
        diretor = dvd[2]
        distribuidora = dvd[3]
        tempo = dvd[4]
        situacao = dvd[5]
        beneficiado = dvd[6]
        telefone = dvd[7]
        dt_emprestimo = dvd[8]
        dt_devolucao = dvd[9]

        if count % 2 == 0:
            tabela_dvds.insert(
                '',
                END,
                values=(
                    id,
                    titulo,
                    diretor,
                    distribuidora,
                    tempo,
                    situacao,
                    beneficiado,
                    telefone,
                    dt_emprestimo,
                    dt_devolucao
                ),
                tags=('evenrow',)
            )

        else:
            tabela_dvds.insert(
                '',
                END,
                values=(
                    id,
                    titulo,
                    diretor,
                    distribuidora,
                    tempo,
                    situacao,
                    beneficiado,
                    telefone,
                    dt_emprestimo,
                    dt_devolucao
                ),
                tags=('oddrow',)
            )

        count += 1


def pesquisar_livros():
    '''
    Exibe na tabela livros o resultado da pesquisa feita de acordo com o dado de entrada e a opção
    de pesquisa.
    '''
    livros = db.pesquisar_livro(
        entrada_pesquisa_livro.get().strip(), opcao_pesquisa_livro.get())

    for livro in tabela_livros.get_children():
        tabela_livros.delete(livro)

    count = 0

    for livro in livros:
        id = livro[0]
        titulo = livro[1]
        autor = livro[2]
        editora = livro[3]
        n_paginas = livro[4]
        situacao = livro[5]
        beneficiado = livro[6]
        telefone = livro[7]
        dt_emprestimo = livro[8]
        dt_devolucao = livro[9]

        if count % 2 == 0:

            tabela_livros.insert(
                '',
                END,
                values=(
                    id,
                    titulo,
                    autor,
                    editora,
                    n_paginas,
                    situacao,
                    beneficiado,
                    telefone,
                    dt_emprestimo,
                    dt_devolucao
                ),
                tags=('evenrow',)
            )

        else:
            tabela_livros.insert(
                '',
                END,
                values=(
                    id,
                    titulo,
                    autor,
                    editora,
                    n_paginas,
                    situacao,
                    beneficiado,
                    telefone,
                    dt_emprestimo,
                    dt_devolucao
                ),
                tags=('oddrow',)
            )

        count += 1


def pesquisar_autor():
    '''
    Exibe na tabela autores o resultado da pesquisa feita de acordo com o dado de entrada.
    '''
    autores = db.pesquisar_autor(entrada_pesquisa_autor.get().strip())

    for autor in tabela_autores.get_children():
        tabela_autores.delete(autor)

    count = 0

    for autor in autores:
        id = autor[0]
        nome_autor = autor[1]

        if count % 2 == 0:
            tabela_autores.insert('', END, values=(
                id, nome_autor), tags=('evenrow',))

        else:
            tabela_autores.insert('', END, values=(
                id, nome_autor), tags=('oddrow',))

        count += 1


def pesquisar_editora():
    '''
    Exibe na tabela editoras o resultado da pesquisa feita de acordo com o dado de entrada.
    '''
    editoras = db.pesquisar_editora(entrada_pesquisa_editora.get().strip())

    for editora in tabela_editoras.get_children():
        tabela_editoras.delete(editora)

    count = 0

    for editora in editoras:
        id = editora[0]
        nome_editora = editora[1]

        if count % 2 == 0:
            tabela_editoras.insert('', END, values=(
                id, nome_editora), tags=('evenrow',))

        else:
            tabela_editoras.insert('', END, values=(
                id, nome_editora), tags=('oddrow',))

        count += 1


def pesquisar_cd():
    cds = db.pesquisar_cd(
        entrada_pesquisa_cd.get().strip(), opcao_pesquisa_cd.get())

    for cd in tabela_cds.get_children():
        tabela_cds.delete(cd)

    count = 0

    for cd in cds:
        id = cd[0]
        titulo = cd[1]
        autor_artista = cd[2]
        distribuidora = cd[3]
        tempo = cd[4]
        situacao = cd[5]
        beneficiado = cd[6]
        telefone = cd[7]
        dt_emprestimo = cd[8]
        dt_devolucao = cd[9]

        if count % 2 == 0:
            tabela_cds.insert(
                '',
                END,
                values=(
                    id,
                    titulo,
                    autor_artista,
                    distribuidora,
                    tempo,
                    situacao,
                    beneficiado,
                    telefone,
                    dt_emprestimo,
                    dt_devolucao
                ),
                tags=('evenrow',)
            )

        else:
            tabela_cds.insert(
                '',
                END,
                values=(
                    id,
                    titulo,
                    autor_artista,
                    distribuidora,
                    tempo,
                    situacao,
                    beneficiado,
                    telefone,
                    dt_emprestimo,
                    dt_devolucao
                ),
                tags=('oddrow',)
            )

        count += 1


def pesquisar_dvd():
    dvds = db.pesquisar_dvd(
        entrada_pesquisa_dvd.get().strip(), opcao_pesquisa_dvd.get())

    for dvd in tabela_dvds.get_children():
        tabela_dvds.delete(dvd)

    count = 0

    for dvd in dvds:
        id = dvd[0]
        titulo = dvd[1]
        diretor = dvd[2]
        distribuidora = dvd[3]
        tempo = dvd[4]
        situacao = dvd[5]
        beneficiado = dvd[6]
        telefone = dvd[7]
        dt_emprestimo = dvd[8]
        dt_devolucao = dvd[9]

        if count % 2 == 0:
            tabela_dvds.insert(
                '',
                END,
                values=(
                    id,
                    titulo,
                    diretor,
                    distribuidora,
                    tempo,
                    situacao,
                    beneficiado,
                    telefone,
                    dt_emprestimo,
                    dt_devolucao
                ),
                tags=('evenrow',)
            )

        else:
            tabela_dvds.insert(
                '',
                END,
                values=(
                    id,
                    titulo,
                    diretor,
                    distribuidora,
                    tempo,
                    situacao,
                    beneficiado,
                    telefone,
                    dt_emprestimo,
                    dt_devolucao
                ),
                tags=('oddrow',)
            )

        count += 1


def pesquisar_autor_artista_cd():
    autores_artistas = db.pesquisar_autor_artista_cd(
        entrada_pesquisa_artista_autor.get().strip())

    for autor_artista in tabela_autores_artistas_cds.get_children():
        tabela_autores_artistas_cds.delete(autor_artista)

    for autor_artista in autores_artistas:
        id = autor_artista[0]
        nome = autor_artista[1]

        count = 0

        if count % 2 == 0:
            tabela_autores_artistas_cds.insert(
                '',
                END,
                values=(
                    id,
                    nome
                ),
                tags=('evenrow',)
            )

        else:
            tabela_autores_artistas_cds.insert(
                '',
                END,
                values=(
                    id,
                    nome
                ),
                tags=('oddrow',)
            )

        count += 1


def pesquisar_diretor_dvd():
    diretores = db.pesquisar_diretor_dvd(
        entrada_pesquisa_diretor_dvd.get().strip())

    for diretor in tabela_diretores_dvds.get_children():
        tabela_diretores_dvds.delete(diretor)

    for diretor in diretores:
        id = diretor[0]
        nome = diretor[1]

        count = 0

        if count % 2 == 0:
            tabela_diretores_dvds.insert(
                '',
                END,
                values=(
                    id,
                    nome
                ),
                tags=('evenrow',)
            )

        else:
            tabela_diretores_dvds.insert(
                '',
                END,
                values=(
                    id,
                    nome
                ),
                tags=('oddrow',)
            )

        count += 1


def pesquisar_distribuidora_cd():
    distribuidoras = db.pesquisar_distribuidora_cd(
        entrada_pesquisa_distribuidora_cd.get().strip())

    for distribuidora in tabela_distribuidoras_cds.get_children():
        tabela_distribuidoras_cds.delete(distribuidora)

    for distribuidora in distribuidoras:
        id = distribuidora[0]
        nome = distribuidora[1]

        count = 0

        if count % 2 == 0:
            tabela_distribuidoras_cds.insert(
                '',
                END,
                values=(
                    id,
                    nome
                ),
                tags=('evenrow',)
            )

        else:
            tabela_distribuidoras_cds.insert(
                '',
                END,
                values=(
                    id,
                    nome
                ),
                tags=('oddrow',)
            )

        count += 1


def pesquisar_distribuidora_dvd():
    distribuidoras = db.pesquisar_distribuidora_dvd(
        entrada_pesquisa_distribuidora_dvd.get().strip())

    for distribuidora in tabela_distribuidoras_dvds.get_children():
        tabela_distribuidoras_dvds.delete(distribuidora)

    for distribuidora in distribuidoras:
        id = distribuidora[0]
        nome = distribuidora[1]

        count = 0

        if count % 2 == 0:
            tabela_distribuidoras_dvds.insert(
                '',
                END,
                values=(
                    id,
                    nome
                ),
                tags=('evenrow',)
            )

        else:
            tabela_distribuidoras_dvds.insert(
                '',
                END,
                values=(
                    id,
                    nome
                ),
                tags=('oddrow',)
            )

        count += 1


def situacao_livro_on_click(e):
    if situacao_livro.get() == 'Disponível':
        beneficiado_livro.delete(0, END)
        telefone_contato.delete(0, END)

        data_emprestimo.configure(state=NORMAL)
        data_emprestimo.delete(0, END)
        data_devolucao.configure(state=NORMAL)
        data_devolucao.delete(0, END)

        beneficiado_livro.configure(state=DISABLED)
        telefone_contato.configure(state=DISABLED)
        data_emprestimo.configure(state=DISABLED)
        data_devolucao.configure(state=DISABLED)

    else:
        beneficiado_livro.configure(state=NORMAL)
        telefone_contato.configure(state=NORMAL)
        data_emprestimo.configure(state='readonly')
        data_devolucao.configure(state='readonly')


def situacao_livro_editar_excluir_on_click(e):
    if situacao_livro_editar_excluir.get() == 'Disponível':
        beneficiado_livro_editar_excluir.delete(0, END)
        telefone_contato_editar_excluir_livro.delete(0, END)

        dt_emprestimo_livro_editar_excluir.configure(state=NORMAL)
        dt_emprestimo_livro_editar_excluir.delete(0, END)
        dt_devolucao_livro_editar_excluir.configure(state=NORMAL)
        dt_devolucao_livro_editar_excluir.delete(0, END)

        beneficiado_livro_editar_excluir.configure(state=DISABLED)
        telefone_contato_editar_excluir_livro.configure(state=DISABLED)
        dt_emprestimo_livro_editar_excluir.configure(state=DISABLED)
        dt_devolucao_livro_editar_excluir.configure(state=DISABLED)

    else:
        beneficiado_livro_editar_excluir.configure(state=NORMAL)
        telefone_contato_editar_excluir_livro.configure(state=NORMAL)
        dt_emprestimo_livro_editar_excluir.configure(state='readonly')
        dt_devolucao_livro_editar_excluir.configure(state='readonly')


def situacao_dvd_on_click(e):
    if situacao_dvd_registro.get() == 'Disponível':
        beneficiado_dvd_registro.delete(0, END)
        telefone_dvd_registro.delete(0, END)

        dt_emprestimo_dvd_registro.configure(state=NORMAL)
        dt_emprestimo_dvd_registro.delete(0, END)
        dt_devolucao_dvd_registro.configure(state=NORMAL)
        dt_devolucao_dvd_registro.delete(0, END)

        beneficiado_dvd_registro.configure(state=DISABLED)
        telefone_dvd_registro.configure(state=DISABLED)
        dt_emprestimo_dvd_registro.configure(state=DISABLED)
        dt_devolucao_dvd_registro.configure(state=DISABLED)

    else:
        beneficiado_dvd_registro.configure(state=NORMAL)
        telefone_dvd_registro.configure(state=NORMAL)
        dt_emprestimo_dvd_registro.configure(state='readonly')
        dt_devolucao_dvd_registro.configure(state='readonly')


def situacao_dvd_editar_excluir_on_click(e):
    if situacao_editar_excluir_dvd.get() == 'Disponível':
        beneficiado_editar_excluir_dvd.delete(0, END)
        telefone_editar_excluir_dvd.delete(0, END)

        dt_emprestimo_editar_excluir_dvd.configure(state=NORMAL)
        dt_emprestimo_editar_excluir_dvd.delete(0, END)
        dt_devolucao_editar_excluir_dvd.configure(state=NORMAL)
        dt_devolucao_editar_excluir_dvd.delete(0, END)

        beneficiado_editar_excluir_dvd.configure(state=DISABLED)
        telefone_editar_excluir_dvd.configure(state=DISABLED)
        dt_emprestimo_editar_excluir_dvd.configure(state=DISABLED)
        dt_devolucao_editar_excluir_dvd.configure(state=DISABLED)

    else:
        beneficiado_editar_excluir_dvd.configure(state=NORMAL)
        telefone_editar_excluir_dvd.configure(state=NORMAL)
        dt_emprestimo_editar_excluir_dvd.configure(state='readonly')
        dt_devolucao_editar_excluir_dvd.configure(state='readonly')


def situacao_cd_on_click(e):
    if situacao_cd_registro.get() == 'Disponível':
        beneficiado_cd_registro.delete(0, END)
        telefone_cd_registro.delete(0, END)

        dt_emprestimo_cd_registro.configure(state=NORMAL)
        dt_emprestimo_cd_registro.delete(0, END)
        dt_emprestimo_cd_registro.configure(state=NORMAL)
        dt_devolucao_cd_registro.delete(0, END)

        beneficiado_cd_registro.configure(state=DISABLED)
        telefone_cd_registro.configure(state=DISABLED)
        dt_emprestimo_cd_registro.configure(state=DISABLED)
        dt_devolucao_cd_registro.configure(state=DISABLED)

    else:
        beneficiado_cd_registro.configure(state=NORMAL)
        telefone_cd_registro.configure(state=NORMAL)
        dt_emprestimo_cd_registro.configure(state='readonly')
        dt_devolucao_cd_registro.configure(state='readonly')


def situacao_cd_editar_excluir_on_click(e):
    if situacao_cd_editar_excluir.get() == 'Disponível':
        beneficiado_cd_editar_excluir.delete(0, END)
        telefone_cd_editar_excluir.delete(0, END)

        dt_emprestimo_cd_editar_excluir.configure(state=NORMAL)
        dt_emprestimo_cd_editar_excluir.delete(0, END)
        dt_devolucao_cd_editar_excluir.configure(state=NORMAL)
        dt_devolucao_cd_editar_excluir.delete(0, END)

        beneficiado_cd_editar_excluir.configure(state=DISABLED)
        telefone_cd_editar_excluir.configure(state=DISABLED)
        dt_emprestimo_cd_editar_excluir.configure(state=DISABLED)
        dt_devolucao_cd_editar_excluir.configure(state=DISABLED)

    else:
        beneficiado_cd_editar_excluir.configure(state=NORMAL)
        telefone_cd_editar_excluir.configure(state=NORMAL)
        dt_emprestimo_cd_editar_excluir.configure(state='readonly')
        dt_devolucao_cd_editar_excluir.configure(state='readonly')


root = Tk()
root.title('Livraria')
root.geometry('500x500')

pesquisa_livro = LabelFrame(
    root,
    text='Pesquisar Livro',
    font='Arial 12'
)

pesquisa_livro.columnconfigure(0, weight=0)
pesquisa_livro.columnconfigure(1, weight=2)
pesquisa_livro.columnconfigure(2, weight=0)

pesquisa_livro.pack(
    expand=False,
    fill=X,
    padx=10,
    pady=10
)

opcao_pesquisa_livro = ttk.Combobox(
    pesquisa_livro,
    values=(
        'Título (Todos)',
        'Autor (Todos)',
        'Editora (Todos)',
        'Título (Disponíveis)',
        'Autor (Disponíveis)',
        'Editora (Disponíveis)',
        'Título (Emprestados)',
        'Autor (Emprestados)',
        'Editora (Emprestados)',
        'Título (Empréstimo Expirado)',
        'Autor (Empréstimo Expirado)',
        'Editora (Empréstimo Expirado)',
        'Beneficiado'
    ),
    state='readonly',
    font='Arial 12'
)
opcao_pesquisa_livro.current(0)
opcao_pesquisa_livro.bind('<<ComboboxSelected>>', muda_opcao_pesquisa_livro)
opcao_pesquisa_livro.grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

entrada_pesquisa_livro = AutocompleteCombobox(
    pesquisa_livro,
    font='Arial 12',
    completevalues=db.titulo_livros()
)
entrada_pesquisa_livro.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

botao_pesquisar_livro = Button(
    pesquisa_livro,
    font='Arial 12',
    text='Pesquisar',
    relief=GROOVE,
    command=pesquisar_livros
)
botao_pesquisar_livro.grid(
    row=0,
    column=2,
    padx=10,
    pady=10,
    sticky=EW
)

pesquisa_autor = LabelFrame(
    root,
    text='Pesquisar Autor',
    font='Arial 12'
)

pesquisa_autor.columnconfigure(0, weight=1)
pesquisa_autor.columnconfigure(1, weight=0)

entrada_pesquisa_autor = AutocompleteCombobox(
    pesquisa_autor,
    font='Arial 12',
    completevalues=db.nome_autores()
)
entrada_pesquisa_autor.grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

botao_pesquisar_autor = Button(
    pesquisa_autor,
    font='Arial 12',
    text='Pesquisar',
    relief=GROOVE,
    command=pesquisar_autor
)
botao_pesquisar_autor.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)
pesquisa_editora = LabelFrame(
    root,
    text='Pesquisar Editora',
    font='Arial 12'
)

pesquisa_editora.columnconfigure(0, weight=1)
pesquisa_editora.columnconfigure(1, weight=0)

entrada_pesquisa_editora = AutocompleteCombobox(
    pesquisa_editora,
    font='Arial 12',
    completevalues=db.nome_editoras()
)
entrada_pesquisa_editora.grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

botao_pesquisar_editora = Button(
    pesquisa_editora,
    font='Arial 12',
    text='Pesquisar',
    relief=GROOVE,
    command=pesquisar_editora
)
botao_pesquisar_editora.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

pesquisa_dvd = LabelFrame(
    root,
    text='Pesquisar DVD',
    font='Arial 12'
)

pesquisa_dvd.columnconfigure(0, weight=0)
pesquisa_dvd.columnconfigure(1, weight=2)
pesquisa_dvd.columnconfigure(2, weight=0)

opcao_pesquisa_dvd = ttk.Combobox(
    pesquisa_dvd,
    values=(
        'Título (Todos)',
        'Diretor (Todos)',
        'Distribuidora (Todos)',
        'Título (Disponíveis)',
        'Diretor (Disponíveis)',
        'Distribuidora (Disponíveis)',
        'Título (Emprestados)',
        'Diretor (Emprestados)',
        'Distribuidora (Emprestados)',
        'Título (Empréstimo Expirado)',
        'Diretor (Empréstimo Expirado)',
        'Distribuidora (Empréstimo Expirado)',
        'Beneficiado'
    ),
    state='readonly',
    font='Arial 12'
)

opcao_pesquisa_dvd.grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)
opcao_pesquisa_dvd.current(0)
opcao_pesquisa_dvd.bind('<<ComboboxSelected>>', muda_opcao_pesquisa_dvd)

entrada_pesquisa_dvd = AutocompleteCombobox(
    pesquisa_dvd,
    font='Arial 12',
    completevalues=db.titulos_dvds()
)
entrada_pesquisa_dvd.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

botao_pesquisar_dvd = Button(
    pesquisa_dvd,
    font='Arial 12',
    text='Pesquisar',
    relief=GROOVE,
    command=pesquisar_dvd
)
botao_pesquisar_dvd.grid(
    row=0,
    column=2,
    padx=10,
    pady=10,
    sticky=EW
)

pesquisa_cd = LabelFrame(
    root,
    text='Pesquisar CD',
    font='Arial 12'
)

pesquisa_cd.columnconfigure(0, weight=0)
pesquisa_cd.columnconfigure(1, weight=2)
pesquisa_cd.columnconfigure(2, weight=0)

opcao_pesquisa_cd = ttk.Combobox(
    pesquisa_cd,
    values=(
        'Título (Todos)',
        'Artista/Autor (Todos)',
        'Distribuidora (Todos)',
        'Título (Disponíveis)',
        'Artista/Autor (Disponíveis)',
        'Distribuidora (Disponíveis)',
        'Título (Emprestados)',
        'Artista/Autor (Emprestados)',
        'Distribuidora (Emprestados)',
        'Título (Empréstimo Expirado)',
        'Artista/Autor (Empréstimo Expirado)',
        'Distribuidora (Empréstimo Expirado)',
        'Beneficiado'
    ),
    state='readonly',
    font='Arial 12'
)

opcao_pesquisa_cd.grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)
opcao_pesquisa_cd.current(0)
opcao_pesquisa_cd.bind('<<ComboboxSelected>>', muda_opcao_pesquisa_cd)

entrada_pesquisa_cd = AutocompleteCombobox(
    pesquisa_cd,
    font='Arial 12',
    completevalues=db.titulos_cds()
)

entrada_pesquisa_cd.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

botao_pesquisar_cd = Button(
    pesquisa_cd,
    font='Arial 12',
    text='Pesquisar',
    relief=GROOVE,
    command=pesquisar_cd
)

botao_pesquisar_cd.grid(
    row=0,
    column=2,
    padx=10,
    pady=10,
    sticky=EW
)

pesquisa_artista_autor_cd = LabelFrame(
    root,
    text='Pesquisar Artista/Autor CD',
    font='Arial 12'
)

pesquisa_artista_autor_cd.columnconfigure(0, weight=1)
pesquisa_artista_autor_cd.columnconfigure(1, weight=0)

entrada_pesquisa_artista_autor = AutocompleteCombobox(
    pesquisa_artista_autor_cd,
    font='Arial 12',
    completevalues=db.nome_autores_artistas_cds()
)
entrada_pesquisa_artista_autor.grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

botao_pesquisar_artista_autor = Button(
    pesquisa_artista_autor_cd,
    font='Arial 12',
    text='Pesquisar',
    relief=GROOVE,
    command=pesquisar_autor_artista_cd
)
botao_pesquisar_artista_autor.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

pesquisa_diretor_dvd = LabelFrame(
    root,
    text='Pesquisar Diretor DVD',
    font='Arial 12'
)

pesquisa_diretor_dvd.columnconfigure(0, weight=1)
pesquisa_diretor_dvd.columnconfigure(1, weight=0)

entrada_pesquisa_diretor_dvd = AutocompleteCombobox(
    pesquisa_diretor_dvd,
    font='Arial 12',
    completevalues=db.nome_diretores_dvds()
)
entrada_pesquisa_diretor_dvd.grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

botao_pesquisar_diretor_dvd = Button(
    pesquisa_diretor_dvd,
    font='Arial 12',
    text='Pesquisar',
    relief=GROOVE,
    command=pesquisar_diretor_dvd
)
botao_pesquisar_diretor_dvd.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)


pesquisa_distribuidora_cd = LabelFrame(
    root,
    text='Pesquisar Distribuidora CD',
    font='Arial 12'
)

pesquisa_distribuidora_cd.columnconfigure(0, weight=1)
pesquisa_distribuidora_cd.columnconfigure(1, weight=0)

entrada_pesquisa_distribuidora_cd = AutocompleteCombobox(
    pesquisa_distribuidora_cd,
    font='Arial 12',
    completevalues=db.nome_distribuidoras_cds()
)
entrada_pesquisa_distribuidora_cd.grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

botao_pesquisar_distribuidora_cd = Button(
    pesquisa_distribuidora_cd,
    font='Arial 12',
    text='Pesquisar',
    relief=GROOVE,
    command=pesquisar_distribuidora_cd
)
botao_pesquisar_distribuidora_cd.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

pesquisa_distribuidora_dvd = LabelFrame(
    root,
    text='Pesquisar Distribuidora DVD',
    font='Arial 12'
)

pesquisa_distribuidora_dvd.columnconfigure(0, weight=1)
pesquisa_distribuidora_dvd.columnconfigure(1, weight=0)

entrada_pesquisa_distribuidora_dvd = AutocompleteCombobox(
    pesquisa_distribuidora_dvd,
    font='Arial 12',
    completevalues=db.nome_distribuidoras_dvds()
)
entrada_pesquisa_distribuidora_dvd.grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

botao_pesquisar_distribuidora_dvd = Button(
    pesquisa_distribuidora_dvd,
    font='Arial 12',
    text='Pesquisar',
    relief=GROOVE,
    command=pesquisar_distribuidora_dvd
)
botao_pesquisar_distribuidora_dvd.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

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

tabela_livros['columns'] = (
    'id',
    'titulo',
    'autor',
    'editora',
    'n_paginas',
    'situacao',
    'beneficiado',
    'telefone',
    'data_emprestimo',
    'data_devolucao'
)
tabela_livros.column('#0', width=0, stretch=NO)

tabela_livros.column('id', anchor=CENTER, width=100)
tabela_livros.column('titulo', anchor=W, width=140)
tabela_livros.column('autor', anchor=W, width=140)
tabela_livros.column('editora', anchor=W, width=140)
tabela_livros.column('n_paginas', anchor=CENTER, width=100)
tabela_livros.column('situacao', anchor=W, width=140)
tabela_livros.column('beneficiado', anchor=W, width=140)
tabela_livros.column('telefone', anchor=CENTER, width=140)
tabela_livros.column('data_emprestimo', anchor=CENTER, width=140)
tabela_livros.column('data_devolucao', anchor=CENTER, width=140)

tabela_livros.heading('#0', text='', anchor=W)
tabela_livros.heading('id', text='ID', anchor=CENTER)
tabela_livros.heading('titulo', text='Título', anchor=W)
tabela_livros.heading('autor', text='Autor(a)', anchor=W)
tabela_livros.heading('editora', text='Editora', anchor=W)
tabela_livros.heading('n_paginas', text='Nº Páginas', anchor=CENTER)
tabela_livros.heading('situacao', text='Situação', anchor=W)
tabela_livros.heading('beneficiado', text='Beneficiado', anchor=W)
tabela_livros.heading('telefone', text='Telefone', anchor=CENTER)
tabela_livros.heading('data_emprestimo', text='Data Emprestimo', anchor=CENTER)
tabela_livros.heading('data_devolucao', text='Data Devolução', anchor=CENTER)

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

tabela_dvds = ttk.Treeview(
    table_frame,
    yscrollcommand=tree_scrool.set,
    selectmode=EXTENDED,
    columns=(
        'id',
        'titulo',
        'diretor',
        'distribuidora',
        'tempo',
        'situacao',
        'beneficiado',
        'telefone',
        'dt_emprestimo',
        'dt_devolucao'
    )
)

tabela_dvds.column('#0', width=0, stretch=NO)

tabela_dvds.column('id', anchor=CENTER, width=100)
tabela_dvds.column('titulo', anchor=W, width=140)
tabela_dvds.column('diretor', anchor=W, width=140)
tabela_dvds.column('distribuidora', anchor=W, width=140)
tabela_dvds.column('tempo', anchor=CENTER, width=100)
tabela_dvds.column('situacao', anchor=W, width=140)
tabela_dvds.column('beneficiado', anchor=W, width=140)
tabela_dvds.column('telefone', anchor=CENTER, width=140)
tabela_dvds.column('dt_emprestimo', anchor=CENTER, width=140)
tabela_dvds.column('dt_devolucao', anchor=CENTER, width=140)

tabela_dvds.heading('#0', text='', anchor=W)
tabela_dvds.heading('id', text='ID', anchor=CENTER)
tabela_dvds.heading('titulo', text='Título', anchor=W)
tabela_dvds.heading('diretor', text='Diretor(a)', anchor=W)
tabela_dvds.heading('distribuidora', text='Distribuidora', anchor=W)
tabela_dvds.heading('tempo', text='Tempo', anchor=CENTER)
tabela_dvds.heading('situacao', text='Situação', anchor=W)
tabela_dvds.heading('beneficiado', text='Beneficiado', anchor=W)
tabela_dvds.heading('telefone', text='Telefone', anchor=CENTER)
tabela_dvds.heading('dt_emprestimo', text='Data Emprestimo', anchor=CENTER)
tabela_dvds.heading('dt_devolucao', text='Data Devolução', anchor=CENTER)

tabela_dvds.tag_configure('oddrow', background='white')
tabela_dvds.tag_configure('evenrow', background='lightblue')

tabela_dvds.bind('<ButtonRelease-1>', selecionar_dvd)

tabela_cds = ttk.Treeview(
    table_frame,
    yscrollcommand=tree_scrool.set,
    selectmode=EXTENDED,
    columns=(
        'id',
        'titulo',
        'artista_autor',
        'distribuidora',
        'tempo',
        'situacao',
        'beneficiado',
        'telefone',
        'dt_emprestimo',
        'dt_devolucao'
    )
)

tabela_cds.column('#0', width=0, stretch=NO)

tabela_cds.column('id', anchor=CENTER, width=100)
tabela_cds.column('titulo', anchor=W, width=140)
tabela_cds.column('artista_autor', anchor=W, width=140)
tabela_cds.column('distribuidora', anchor=W, width=140)
tabela_cds.column('tempo', anchor=CENTER, width=100)
tabela_cds.column('situacao', anchor=W, width=140)
tabela_cds.column('beneficiado', anchor=W, width=140)
tabela_cds.column('telefone', anchor=CENTER, width=140)
tabela_cds.column('dt_emprestimo', anchor=CENTER, width=140)
tabela_cds.column('dt_devolucao', anchor=CENTER, width=140)

tabela_cds.heading('#0', text='', anchor=W)
tabela_cds.heading('id', text='ID', anchor=CENTER)
tabela_cds.heading('titulo', text='Título', anchor=W)
tabela_cds.heading('artista_autor', text='Artista/Autor', anchor=W)
tabela_cds.heading('distribuidora', text='Distribuidora', anchor=W)
tabela_cds.heading('tempo', text='Tempo', anchor=CENTER)
tabela_cds.heading('situacao', text='Situação', anchor=W)
tabela_cds.heading('beneficiado', text='Beneficiado', anchor=W)
tabela_cds.heading('telefone', text='Telefone', anchor=CENTER)
tabela_cds.heading('dt_emprestimo', text='Data Emprestimo', anchor=CENTER)
tabela_cds.heading('dt_devolucao', text='Data Devolução', anchor=CENTER)

tabela_cds.tag_configure('oddrow', background='white')
tabela_cds.tag_configure('evenrow', background='lightblue')

tabela_cds.bind('<ButtonRelease-1>', selecionar_cd)

tabela_autores_artistas_cds = ttk.Treeview(
    table_frame,
    yscrollcommand=tree_scrool.set,
    selectmode=EXTENDED,
    columns=(
        'id',
        'artista_autor'
    )
)

tabela_autores_artistas_cds.column('#0', width=0, stretch=NO)

tabela_autores_artistas_cds.column('id', anchor=CENTER, width=100)
tabela_autores_artistas_cds.column('artista_autor', anchor=W, width=140)

tabela_autores_artistas_cds.heading('#0', text='', anchor=W)

tabela_autores_artistas_cds.heading('id', text='ID', anchor=CENTER)
tabela_autores_artistas_cds.heading(
    'artista_autor', text='Artista/Autor', anchor=W)

tabela_autores_artistas_cds.tag_configure('oddrow', background='white')
tabela_autores_artistas_cds.tag_configure('evenrow', background='lightblue')

tabela_autores_artistas_cds.bind(
    '<ButtonRelease-1>', selecionar_artista_autor_cd)

tabela_diretores_dvds = ttk.Treeview(
    table_frame,
    yscrollcommand=tree_scrool.set,
    selectmode=EXTENDED,
    columns=(
        'id',
        'diretor'
    )
)

tabela_diretores_dvds.column('#0', width=0, stretch=NO)

tabela_diretores_dvds.column('id', anchor=CENTER, width=100)
tabela_diretores_dvds.column('diretor', anchor=W, width=140)

tabela_diretores_dvds.heading('#0', text='', anchor=W)

tabela_diretores_dvds.heading('id', text='ID', anchor=CENTER)
tabela_diretores_dvds.heading('diretor', text='Diretor(a)', anchor=W)

tabela_diretores_dvds.tag_configure('oddrow', background='white')
tabela_diretores_dvds.tag_configure('evenrow', background='lightblue')

tabela_diretores_dvds.bind('<ButtonRelease-1>', selecionar_diretor_dvd)

tabela_distribuidoras_cds = ttk.Treeview(
    table_frame,
    yscrollcommand=tree_scrool.set,
    selectmode=EXTENDED,
    columns=(
        'id',
        'distribuidora'
    )
)

tabela_distribuidoras_cds.column('#0', width=0, stretch=NO)

tabela_distribuidoras_cds.column('id', anchor=CENTER, width=100)
tabela_distribuidoras_cds.column('distribuidora', anchor=W, width=140)

tabela_distribuidoras_cds.heading('#0', text='', anchor=W)

tabela_distribuidoras_cds.heading('id', text='ID', anchor=CENTER)
tabela_distribuidoras_cds.heading(
    'distribuidora', text='Distribuidora', anchor=W)

tabela_distribuidoras_cds.tag_configure('oddrow', background='white')
tabela_distribuidoras_cds.tag_configure('evenrow', background='lightblue')

tabela_distribuidoras_cds.bind(
    '<ButtonRelease-1>', selecionar_distribuidora_cd)

tabela_distribuidoras_dvds = ttk.Treeview(
    table_frame,
    yscrollcommand=tree_scrool.set,
    selectmode=EXTENDED,
    columns=(
        'id',
        'distribuidora'
    )
)

tabela_distribuidoras_dvds.column('#0', width=0, stretch=NO)

tabela_distribuidoras_dvds.column('id', anchor=CENTER, width=100)
tabela_distribuidoras_dvds.column('distribuidora', anchor=W, width=140)

tabela_distribuidoras_dvds.heading('#0', text='', anchor=W)

tabela_distribuidoras_dvds.heading('id', text='ID', anchor=CENTER)
tabela_distribuidoras_dvds.heading(
    'distribuidora', text='Distribuidora', anchor=W)

tabela_distribuidoras_dvds.tag_configure('oddrow', background='white')
tabela_distribuidoras_dvds.tag_configure('evenrow', background='lightblue')

tabela_distribuidoras_dvds.bind(
    '<ButtonRelease-1>', selecionar_distribuidora_dvd)

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

autor_entry_registro_livro = AutocompleteCombobox(
    livro_register_frame,
    font='Arial 12',
    completevalues=db.nome_autores()
)
autor_entry_registro_livro.grid(row=1, column=1, padx=10, pady=10, sticky=EW)

editora_label_registro_livro = Label(
    livro_register_frame,
    text='Editora',
    font='Arial 12'
)
editora_label_registro_livro.grid(row=2, column=0, padx=10, pady=10)

editora_entry_registro_livro = AutocompleteCombobox(
    livro_register_frame,
    font='Arial 12',
    completevalues=db.nome_editoras()
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

Label(
    livro_register_frame,
    text='Situação',
    font='Arial 12'
).grid(
    row=4,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

situacao_livro = ttk.Combobox(
    livro_register_frame,
    values=(
        'Disponível',
        'Emprestado'
    ),
    state='readonly',
    font='Arial 12'
)
situacao_livro.current(0)
situacao_livro.bind('<<ComboboxSelected>>', situacao_livro_on_click)
situacao_livro.grid(
    row=4,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    livro_register_frame,
    text='Beneficiado',
    font='Arial 12'
).grid(
    row=5,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

beneficiado_livro = Entry(
    livro_register_frame,
    font='Arial 12',
    state=DISABLED
)
beneficiado_livro.grid(
    row=5,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    livro_register_frame,
    text='Tel. Contato',
    font='Arial 12'
).grid(
    row=6,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

telefone_contato = Entry(
    livro_register_frame,
    font='Arial 12',
    state=DISABLED
)
telefone_contato.grid(
    row=6,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    livro_register_frame,
    text='Data de Empréstimo',
    font='Arial 12'
).grid(
    row=7,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

data_emprestimo = DateEntry(
    livro_register_frame,
    locale='pt_BR',
    date_pattern='dd/mm/y',
    font='Arial 12',
    state=DISABLED
)
data_emprestimo.grid(
    row=7,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    livro_register_frame,
    text='Data de Devolução',
    font='Arial 12'
).grid(
    row=8,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

data_devolucao = DateEntry(
    livro_register_frame,
    locale='pt_BR',
    date_pattern='dd/mm/y',
    font='Arial 12',
    state=DISABLED
)
data_devolucao.grid(
    row=8,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

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

autor_entry_registro_autor = AutocompleteCombobox(
    autor_register_frame,
    font='Arial 12',
    completevalues=db.nome_autores()
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

editora_entry_registro_editora = AutocompleteCombobox(
    editora_register_frame,
    font='Arial 12',
    completevalues=db.nome_editoras()
)
editora_entry_registro_editora.grid(
    row=0, column=1, padx=10, pady=10, sticky=EW)

dvd_register_frame = Frame(
    table_frame
)

dvd_register_frame.columnconfigure(1, weight=1)

Label(
    dvd_register_frame,
    text='Título',
    font='Arial 12'
).grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

titulo_dvd_registro = Entry(
    dvd_register_frame,
    font='Arial 12'
)
titulo_dvd_registro.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    dvd_register_frame,
    text='Diretor(a)',
    font='Arial 12'
).grid(
    row=1,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

diretor_dvd_registro = AutocompleteCombobox(
    dvd_register_frame,
    font='Arial 12',
    completevalues=db.nome_diretores_dvds()
)
diretor_dvd_registro.grid(
    row=1,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    dvd_register_frame,
    text='Distribuidora',
    font='Arial 12'
).grid(
    row=2,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

distribuidora_dvd_registro = AutocompleteCombobox(
    dvd_register_frame,
    font='Arial 12',
    completevalues=db.nome_distribuidoras_dvds()
)
distribuidora_dvd_registro.grid(
    row=2,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    dvd_register_frame,
    text='Tempo',
    font='Arial 12'
).grid(
    row=3,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

tempo_dvd_registro = Entry(
    dvd_register_frame,
    font='Arial 12'
)
tempo_dvd_registro.grid(
    row=3,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    dvd_register_frame,
    text='Situação',
    font='Arial 12'
).grid(
    row=4,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

situacao_dvd_registro = ttk.Combobox(
    dvd_register_frame,
    values=(
        'Disponível',
        'Emprestado'
    ),
    state='readonly',
    font='Arial 12',
)
situacao_dvd_registro.current(0)
situacao_dvd_registro.bind('<<ComboboxSelected>>', situacao_dvd_on_click)
situacao_dvd_registro.grid(
    row=4,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    dvd_register_frame,
    text='Beneficado',
    font='Arial 12'
).grid(
    row=5,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

beneficiado_dvd_registro = Entry(
    dvd_register_frame,
    state=DISABLED,
    font='Arial 12'
)
beneficiado_dvd_registro.grid(
    row=5,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    dvd_register_frame,
    text='Telefone',
    font='Arial 12'
).grid(
    row=6,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

telefone_dvd_registro = Entry(
    dvd_register_frame,
    state=DISABLED,
    font='Arial 12'
)
telefone_dvd_registro.grid(
    row=6,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    dvd_register_frame,
    text='Data Empréstimo',
    font='Arial 12'
).grid(
    row=7,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

dt_emprestimo_dvd_registro = DateEntry(
    dvd_register_frame,
    locale='pt_BR',
    date_pattern='dd/mm/y',
    font='Arial 12',
    state=DISABLED
)
dt_emprestimo_dvd_registro.grid(
    row=7,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    dvd_register_frame,
    text='Data Devolução',
    font='Arial 12'
).grid(
    row=8,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

dt_devolucao_dvd_registro = DateEntry(
    dvd_register_frame,
    locale='pt_BR',
    date_pattern='dd/mm/y',
    font='Arial 12',
    state=DISABLED
)
dt_devolucao_dvd_registro.grid(
    row=8,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

cd_register_frame = Frame(
    table_frame
)

cd_register_frame.columnconfigure(1, weight=1)

Label(
    cd_register_frame,
    text='Título',
    font='Arial 12'
).grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

titulo_cd_registro = Entry(
    cd_register_frame,
    font='Arial 12'
)
titulo_cd_registro.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    cd_register_frame,
    text='Aritsta/Autor',
    font='Arial 12'
).grid(
    row=1,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

artista_autor_cd_registro = AutocompleteCombobox(
    cd_register_frame,
    font='Arial 12',
    completevalues=db.nome_autores_artistas_cds()
)
artista_autor_cd_registro.grid(
    row=1,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    cd_register_frame,
    text='Distribuidora',
    font='Arial 12'
).grid(
    row=2,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

distribuidora_cd_registro = AutocompleteCombobox(
    cd_register_frame,
    font='Arial 12',
    completevalues=db.nome_distribuidoras_cds()
)
distribuidora_cd_registro.grid(
    row=2,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    cd_register_frame,
    text='Tempo',
    font='Arial 12'
).grid(
    row=3,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

tempo_cd_registro = Entry(
    cd_register_frame,
    font='Arial 12'
)
tempo_cd_registro.grid(
    row=3,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    cd_register_frame,
    text='Situação',
    font='Arial 12'
).grid(
    row=4,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

situacao_cd_registro = ttk.Combobox(
    cd_register_frame,
    values=(
        'Disponível',
        'Emprestado'
    ),
    state='readonly',
    font='Arial 12',
)
situacao_cd_registro.current(0)
situacao_cd_registro.bind('<<ComboboxSelected>>', situacao_cd_on_click)
situacao_cd_registro.grid(
    row=4,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    cd_register_frame,
    text='Beneficado',
    font='Arial 12'
).grid(
    row=5,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

beneficiado_cd_registro = Entry(
    cd_register_frame,
    state=DISABLED,
    font='Arial 12'
)
beneficiado_cd_registro.grid(
    row=5,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    cd_register_frame,
    text='Telefone',
    font='Arial 12'
).grid(
    row=6,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

telefone_cd_registro = Entry(
    cd_register_frame,
    state=DISABLED,
    font='Arial 12'
)
telefone_cd_registro.grid(
    row=6,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    cd_register_frame,
    text='Data Empréstimo',
    font='Arial 12'
).grid(
    row=7,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

dt_emprestimo_cd_registro = DateEntry(
    cd_register_frame,
    locale='pt_BR',
    date_pattern='dd/mm/y',
    font='Arial 12',
    state=DISABLED
)
dt_emprestimo_cd_registro.grid(
    row=7,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    cd_register_frame,
    text='Data Devolução',
    font='Arial 12'
).grid(
    row=8,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

dt_devolucao_cd_registro = DateEntry(
    cd_register_frame,
    locale='pt_BR',
    date_pattern='dd/mm/y',
    font='Arial 12',
    state=DISABLED
)
dt_devolucao_cd_registro.grid(
    row=8,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

autor_artista_cd_register_frame = Frame(
    table_frame
)

autor_artista_cd_register_frame.columnconfigure(0, weight=0)
autor_artista_cd_register_frame.columnconfigure(1, weight=1)

Label(
    autor_artista_cd_register_frame,
    text='Autor',
    font='Arial 12'
).grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

nome_autor_artista_registro = AutocompleteCombobox(
    autor_artista_cd_register_frame,
    font='Arial 12',
    completevalues=db.nome_autores_artistas_cds()
)
nome_autor_artista_registro.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

diretor_dvd_register_frame = Frame(
    table_frame
)

diretor_dvd_register_frame.columnconfigure(0, weight=0)
diretor_dvd_register_frame.columnconfigure(1, weight=1)

Label(
    diretor_dvd_register_frame,
    text='Diretor(a)',
    font='Arial 12'
).grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

nome_diretor_dvd_registro = AutocompleteCombobox(
    diretor_dvd_register_frame,
    font='Arial 12',
    completevalues=db.nome_diretores_dvds()
)
nome_diretor_dvd_registro.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

distribuidora_cd_register_frame = Frame(
    table_frame
)

distribuidora_cd_register_frame.columnconfigure(0, weight=0)
distribuidora_cd_register_frame.columnconfigure(1, weight=1)

Label(
    distribuidora_cd_register_frame,
    text='Distribuidora',
    font='Arial 12'
).grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

nome_distribuidora_cd_registro = AutocompleteCombobox(
    distribuidora_cd_register_frame,
    font='Arial 12',
    completevalues=db.nome_distribuidoras_cds()
)
nome_distribuidora_cd_registro.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

distribuidora_dvd_register_frame = Frame(
    table_frame
)

distribuidora_dvd_register_frame.columnconfigure(0, weight=0)
distribuidora_dvd_register_frame.columnconfigure(1, weight=1)

Label(
    distribuidora_dvd_register_frame,
    text='Distribuidora',
    font='Arial 12'
).grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

nome_distribuidora_dvd_registro = AutocompleteCombobox(
    distribuidora_dvd_register_frame,
    font='Arial 12',
    completevalues=db.nome_distribuidoras_dvds()
)
nome_distribuidora_dvd_registro.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

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
    command=adicionar_registro,
    font='Arial 12'
)
button_add.grid(row=0, column=0, padx=10, pady=10, sticky=EW)

button_cancel = Button(
    button_register_frame,
    text='Cancelar',
    relief=GROOVE,
    command=cancelar_registro,
    font='Arial 12'
)
button_cancel.grid(row=0, column=1, padx=10, pady=10, sticky=EW)

drop_down_register = ttk.Combobox(
    button_register_frame,
    values=(
        'Livro',
        'Autor',
        'Editora',
        'DVD',
        'CD',
        'Autor/Artista CD',
        'Diretor(a) DVD',
        'Distribuidora CD',
        'Distribuidora DVD'
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

autor_entry_editar_excluir_livro = AutocompleteCombobox(
    editar_excluir_livro,
    font='Arial 12',
    completevalues=db.nome_autores()
)
autor_entry_editar_excluir_livro.grid(
    row=1, column=1, padx=10, pady=10, sticky=EW)

editora_label_editar_excluir_livro = Label(
    editar_excluir_livro,
    text='Editora',
    font='Arial 12'
)
editora_label_editar_excluir_livro.grid(row=2, column=0, padx=10, pady=10)

editora_entry_editar_excluir_livro = AutocompleteCombobox(
    editar_excluir_livro,
    font='Arial 12',
    completevalues=db.nome_editoras()
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

Label(
    editar_excluir_livro,
    text='Situação',
    font='Arial 12'
).grid(
    row=4,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

situacao_livro_editar_excluir = ttk.Combobox(
    editar_excluir_livro,
    values=(
        'Disponível',
        'Emprestado'
    ),
    state='readonly',
    font='Arial 12'
)
situacao_livro_editar_excluir.current(0)
situacao_livro_editar_excluir.bind(
    '<<ComboboxSelected>>', situacao_livro_editar_excluir_on_click)
situacao_livro_editar_excluir.grid(
    row=4,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    editar_excluir_livro,
    text='Beneficiado',
    font='Arial 12'
).grid(
    row=5,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

beneficiado_livro_editar_excluir = Entry(
    editar_excluir_livro,
    font='Arial 12',
    state=DISABLED
)
beneficiado_livro_editar_excluir.grid(
    row=5,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    editar_excluir_livro,
    text='Tel. Contato',
    font='Arial 12'
).grid(
    row=6,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

telefone_contato_editar_excluir_livro = Entry(
    editar_excluir_livro,
    font='Arial 12',
    state=DISABLED
)
telefone_contato_editar_excluir_livro.grid(
    row=6,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    editar_excluir_livro,
    text='Data de Empréstimo',
    font='Arial 12'
).grid(
    row=7,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

dt_emprestimo_livro_editar_excluir = DateEntry(
    editar_excluir_livro,
    locale='pt_BR',
    date_pattern='dd/mm/y',
    font='Arial 12',
    state=DISABLED
)
dt_emprestimo_livro_editar_excluir.grid(
    row=7,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    editar_excluir_livro,
    text='Data de Devolução',
    font='Arial 12'
).grid(
    row=8,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

dt_devolucao_livro_editar_excluir = DateEntry(
    editar_excluir_livro,
    locale='pt_BR',
    date_pattern='dd/mm/y',
    font='Arial 12',
    state=DISABLED
)
dt_devolucao_livro_editar_excluir.grid(
    row=8,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

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
    command=editar_livro,
    font='Arial 12'
)
botao_editar_livro.grid(row=0, column=0, padx=10, pady=10, sticky=EW)

botao_excluir_livro = Button(
    botoes_editar_excluir_livro,
    text='Excluir',
    relief=GROOVE,
    command=excluir_livro,
    font='Arial 12'
)
botao_excluir_livro.grid(row=0, column=1, padx=10, pady=10, sticky=EW)

botao_cancelar_edicao_livro = Button(
    botoes_editar_excluir_livro,
    text='Cancelar',
    relief=GROOVE,
    command=cancelar_edicao_livro,
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

autor_entry_editar_excluir_autor = AutocompleteCombobox(
    editar_excluir_autor,
    font='Arial 12',
    completevalues=db.nome_autores()
)
autor_entry_editar_excluir_autor.grid(
    row=0, column=1, padx=10, pady=10, sticky=EW)

botoes_editar_excluir_autor = Frame(
    table_frame
)

botoes_editar_excluir_autor.columnconfigure(0, weight=1)
botoes_editar_excluir_autor.columnconfigure(1, weight=1)

botao_editar_autor = Button(
    botoes_editar_excluir_autor,
    text='Editar',
    relief=GROOVE,
    command=editar_autor,
    font='Arial 12'
)
botao_editar_autor.grid(row=0, column=0, padx=10, pady=10, sticky=EW)

botao_cancelar_edicao_autor = Button(
    botoes_editar_excluir_autor,
    text='Cancelar',
    relief=GROOVE,
    command=cancelar_edicao_autor,
    font='Arial 12'
)
botao_cancelar_edicao_autor.grid(row=0, column=1, padx=10, pady=10, sticky=EW)

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

editora_entry_editar_excluir_editora = AutocompleteCombobox(
    editar_excluir_editora,
    font='Arial 12',
    completevalues=db.nome_editoras()
)
editora_entry_editar_excluir_editora.grid(
    row=0, column=1, padx=10, pady=10, sticky=EW)

botoes_editar_excluir_editora = Frame(
    table_frame
)

botoes_editar_excluir_editora.columnconfigure(0, weight=1)
botoes_editar_excluir_editora.columnconfigure(1, weight=1)

botao_editar_editora = Button(
    botoes_editar_excluir_editora,
    text='Editar',
    relief=GROOVE,
    command=editar_editora,
    font='Arial 12'
)
botao_editar_editora.grid(row=0, column=0, padx=10, pady=10, sticky=EW)

botao_cancelar_edicao_editora = Button(
    botoes_editar_excluir_editora,
    text='Cancelar',
    relief=GROOVE,
    command=cancelar_edicao_editora,
    font='Arial 12'
)
botao_cancelar_edicao_editora.grid(
    row=0, column=1, padx=10, pady=10, sticky=EW)

editar_excluir_dvd = Frame(
    table_frame
)

editar_excluir_dvd.columnconfigure(0, weight=0)
editar_excluir_dvd.columnconfigure(1, weight=1)

Label(
    editar_excluir_dvd,
    text='Título',
    font='Arial 12'
).grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

titulo_editar_excluir_dvd = Entry(
    editar_excluir_dvd,
    font='Arial 12'
)
titulo_editar_excluir_dvd.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    editar_excluir_dvd,
    text='Diretor(a)',
    font='Arial 12'
).grid(
    row=1,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

diretor_editar_excluir_dvd = AutocompleteCombobox(
    editar_excluir_dvd,
    font='Arial 12',
    completevalues=db.nome_diretores_dvds()
)
diretor_editar_excluir_dvd.grid(
    row=1,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    editar_excluir_dvd,
    text='Distribuidora',
    font='Arial 12'
).grid(
    row=2,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

distribuidora_editar_excluir_dvd = AutocompleteCombobox(
    editar_excluir_dvd,
    font='Arial 12',
    completevalues=db.nome_distribuidoras_dvds()
)
distribuidora_editar_excluir_dvd.grid(
    row=2,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    editar_excluir_dvd,
    text='Tempo',
    font='Arial 12'
).grid(
    row=3,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

tempo_editar_excluir_dvd = Entry(
    editar_excluir_dvd,
    font='Arial 12'
)
tempo_editar_excluir_dvd.grid(
    row=3,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    editar_excluir_dvd,
    text='Situação',
    font='Arial 12'
).grid(
    row=4,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

situacao_editar_excluir_dvd = ttk.Combobox(
    editar_excluir_dvd,
    values=(
        'Disponível',
        'Emprestado'
    ),
    font='Arial 12',
    state='readonly'
)
situacao_editar_excluir_dvd.current(0)
situacao_editar_excluir_dvd.bind(
    '<<ComboboxSelected>>', situacao_dvd_editar_excluir_on_click)
situacao_editar_excluir_dvd.grid(
    row=4,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    editar_excluir_dvd,
    text='Beneficiado',
    font='Arial 12'
).grid(
    row=5,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

beneficiado_editar_excluir_dvd = Entry(
    editar_excluir_dvd,
    font='Arial 12',
    state=DISABLED
)
beneficiado_editar_excluir_dvd.grid(
    row=5,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    editar_excluir_dvd,
    text='Telefone',
    font='Arial 12'
).grid(
    row=6,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

telefone_editar_excluir_dvd = Entry(
    editar_excluir_dvd,
    font='Arial 12'
)
telefone_editar_excluir_dvd.grid(
    row=6,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    editar_excluir_dvd,
    text='Data de Empréstimo',
    font='Arial 12'
).grid(
    row=7,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

dt_emprestimo_editar_excluir_dvd = DateEntry(
    editar_excluir_dvd,
    locale='pt_BR',
    date_pattern='dd/mm/y',
    font='Arial 12',
    state=DISABLED
)
dt_emprestimo_editar_excluir_dvd.grid(
    row=7,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    editar_excluir_dvd,
    text='Data de devolução',
    font='Arial 12'
).grid(
    row=8,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

dt_devolucao_editar_excluir_dvd = DateEntry(
    editar_excluir_dvd,
    locale='pt_BR',
    date_pattern='dd/mm/y',
    font='Arial 12',
    state=DISABLED
)
dt_devolucao_editar_excluir_dvd.grid(
    row=8,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

botoes_editar_excluir_dvd = Frame(
    table_frame
)

botoes_editar_excluir_dvd.columnconfigure(0, weight=1)
botoes_editar_excluir_dvd.columnconfigure(1, weight=1)
botoes_editar_excluir_dvd.columnconfigure(2, weight=1)

botao_editar_dvd = Button(
    botoes_editar_excluir_dvd,
    text='Editar',
    font='Arial 12',
    relief=GROOVE,
    command=editar_dvd
)
botao_editar_dvd.grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

botao_excluir_dvd = Button(
    botoes_editar_excluir_dvd,
    text='Excluir',
    font='Arial 12',
    relief=GROOVE,
    command=excluir_dvd
)
botao_excluir_dvd.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

botao_cancelar_edicao_dvd = Button(
    botoes_editar_excluir_dvd,
    text='Cancelar',
    font='Arial 12',
    relief=GROOVE,
    command=cancelar_edicao_dvd
)
botao_cancelar_edicao_dvd.grid(
    row=0,
    column=2,
    padx=10,
    pady=10,
    sticky=EW
)

editar_excluir_cd = Frame(
    table_frame
)

editar_excluir_cd.columnconfigure(0, weight=0)
editar_excluir_cd.columnconfigure(1, weight=1)

Label(
    editar_excluir_cd,
    text='Título',
    font='Arial 12'
).grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

titulo_cd_editar_excluir = Entry(
    editar_excluir_cd,
    font='Arial 12'
)
titulo_cd_editar_excluir.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    editar_excluir_cd,
    text='Autor/Artista',
    font='Arial 12'
).grid(
    row=1,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

autor_artista_cd_editar_excluir = AutocompleteCombobox(
    editar_excluir_cd,
    font='Arial 12',
    completevalues=db.nome_autores_artistas_cds()
)
autor_artista_cd_editar_excluir.grid(
    row=1,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    editar_excluir_cd,
    text='Distribuidora',
    font='Arial 12'
).grid(
    row=2,
    column=0,
    padx=10,
    pady=10,
    stick=EW
)

distribuidora_cd_editar_excluir = AutocompleteCombobox(
    editar_excluir_cd,
    font='Arial 12',
    completevalues=db.nome_distribuidoras_cds()
)
distribuidora_cd_editar_excluir.grid(
    row=2,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    editar_excluir_cd,
    text='Tempo',
    font='Arial 12'
).grid(
    row=3,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

tempo_cd_editar_excluir = Entry(
    editar_excluir_cd,
    font='Arial 12'
)
tempo_cd_editar_excluir.grid(
    row=3,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    editar_excluir_cd,
    text='Situação',
    font='Arial 12'
).grid(
    row=4,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

situacao_cd_editar_excluir = ttk.Combobox(
    editar_excluir_cd,
    values=(
        'Disponível',
        'Emprestado'
    ),
    font='Arial 12',
    state='readonly',
)
situacao_cd_editar_excluir.bind(
    '<<ComboboxSelected>>', situacao_cd_editar_excluir_on_click)
situacao_cd_editar_excluir.current(0)
situacao_cd_editar_excluir.grid(
    row=4,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    editar_excluir_cd,
    text='Beneficiado',
    font='Arial 12'
).grid(
    row=5,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

beneficiado_cd_editar_excluir = Entry(
    editar_excluir_cd,
    font='Arial 12'
)
beneficiado_cd_editar_excluir.grid(
    row=5,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    editar_excluir_cd,
    text='Telefone',
    font='Arial 12'
).grid(
    row=6,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

telefone_cd_editar_excluir = Entry(
    editar_excluir_cd,
    font='Arial 12'
)
telefone_cd_editar_excluir.grid(
    row=6,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    editar_excluir_cd,
    text='Data de Empréstimo',
    font='Arial 12'
).grid(
    row=7,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

dt_emprestimo_cd_editar_excluir = DateEntry(
    editar_excluir_cd,
    locale='pt_BR',
    date_pattern='dd/mm/y',
    font='Arial 12',
    state=DISABLED
)
dt_emprestimo_cd_editar_excluir.grid(
    row=7,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

Label(
    editar_excluir_cd,
    text='Data de Devolução',
    font='Arial 12'
).grid(
    row=8,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

dt_devolucao_cd_editar_excluir = DateEntry(
    editar_excluir_cd,
    locale='pt_BR',
    date_pattern='dd/mm/y',
    font='Arial 12',
    state=DISABLED
)
dt_devolucao_cd_editar_excluir.grid(
    row=8,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

botoes_editar_excluir_cd = Frame(
    table_frame
)

botoes_editar_excluir_cd.columnconfigure(0, weight=1)
botoes_editar_excluir_cd.columnconfigure(1, weight=1)
botoes_editar_excluir_cd.columnconfigure(2, weight=1)

botao_editar_cd = Button(
    botoes_editar_excluir_cd,
    text='Editar',
    font='Arial 12',
    relief=GROOVE,
    command=editar_cd
)
botao_editar_cd.grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

botao_excluir_cd = Button(
    botoes_editar_excluir_cd,
    text='Excluir',
    font='Arial 12',
    relief=GROOVE,
    command=excluir_cd
)
botao_excluir_cd.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

botao_cancelar_edicao_cd = Button(
    botoes_editar_excluir_cd,
    text='Cancelar',
    font='Arial 12',
    relief=GROOVE,
    command=cancelar_edicao_cd
)
botao_cancelar_edicao_cd.grid(
    row=0,
    column=2,
    padx=10,
    pady=10,
    sticky=EW
)

editar_excluir_autor_artista_cd = Frame(
    table_frame
)

editar_excluir_autor_artista_cd.columnconfigure(0, weight=0)
editar_excluir_autor_artista_cd.columnconfigure(1, weight=1)

Label(
    editar_excluir_autor_artista_cd,
    text='Autor',
    font='Arial 12'
).grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

nome_autor_artista_editar_excluir_cd = AutocompleteCombobox(
    editar_excluir_autor_artista_cd,
    font='Arial 12',
    completevalues=db.nome_autores_artistas_cds()
)
nome_autor_artista_editar_excluir_cd.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

botoes_editar_excluir_autor_artista_cd = Frame(
    table_frame
)

botoes_editar_excluir_autor_artista_cd.columnconfigure(0, weight=1)
botoes_editar_excluir_autor_artista_cd.columnconfigure(1, weight=1)

botao_editar_autor_artista_cd = Button(
    botoes_editar_excluir_autor_artista_cd,
    text='Editar',
    font='Arial 12',
    relief=GROOVE,
    command=editar_artista_autor_cd
)
botao_editar_autor_artista_cd.grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

botao_cancelar_edicao_autor_artista_cd = Button(
    botoes_editar_excluir_autor_artista_cd,
    text='Cancelar',
    font='Arial 12',
    relief=GROOVE,
    command=cancelar_edicao_artista_autor_cd
)
botao_cancelar_edicao_autor_artista_cd.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

editar_excluir_diretor_dvd = Frame(
    table_frame
)

editar_excluir_diretor_dvd.columnconfigure(0, weight=0)
editar_excluir_diretor_dvd.columnconfigure(1, weight=1)

Label(
    editar_excluir_diretor_dvd,
    text='Diretor(a)',
    font='Arial 12'
).grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

nome_diretor_dvd_editar_excluir = AutocompleteCombobox(
    editar_excluir_diretor_dvd,
    font='Arial 12',
    completevalues=db.nome_diretores_dvds()
)
nome_diretor_dvd_editar_excluir.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

botoes_editar_excluir_diretor_dvd = Frame(
    table_frame
)

botoes_editar_excluir_diretor_dvd.columnconfigure(0, weight=1)
botoes_editar_excluir_diretor_dvd.columnconfigure(1, weight=1)

botao_editar_diretor_dvd = Button(
    botoes_editar_excluir_diretor_dvd,
    text='Editar',
    font='Arial 12',
    relief=GROOVE,
    command=editar_diretor_dvd
)
botao_editar_diretor_dvd.grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

botao_cancelar_edicao_diretor_dvd = Button(
    botoes_editar_excluir_diretor_dvd,
    text='Cancelar',
    font='Arial 12',
    relief=GROOVE,
    command=cancelar_edicao_diretor_dvd
)
botao_cancelar_edicao_diretor_dvd.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

editar_excluir_distribuidora_cd = Frame(
    table_frame
)

editar_excluir_distribuidora_cd.columnconfigure(0, weight=0)
editar_excluir_distribuidora_cd.columnconfigure(1, weight=1)

Label(
    editar_excluir_distribuidora_cd,
    text='Distribuidora',
    font='Arial 12'
).grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

nome_distribuidora_cd_editar_excluir = AutocompleteCombobox(
    editar_excluir_distribuidora_cd,
    font='Arial 12',
    completevalues=db.nome_distribuidoras_cds()
)
nome_distribuidora_cd_editar_excluir.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

botoes_editar_excluir_distribuidora_cd = Frame(
    table_frame
)

botoes_editar_excluir_distribuidora_cd.columnconfigure(0, weight=1)
botoes_editar_excluir_distribuidora_cd.columnconfigure(1, weight=1)

botao_editar_distribuidora_cd = Button(
    botoes_editar_excluir_distribuidora_cd,
    text='Editar',
    font='Arial 12',
    relief=GROOVE,
    command=editar_distribuidora_cd
)
botao_editar_distribuidora_cd.grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

botao_cancelar_edicao_distribuidora_cd = Button(
    botoes_editar_excluir_distribuidora_cd,
    text='Cancelar',
    font='Arial 12',
    relief=GROOVE,
    command=cancelar_edicao_distribuidora_cd
)
botao_cancelar_edicao_distribuidora_cd.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

editar_excluir_distribuidora_dvd = Frame(
    table_frame
)

editar_excluir_distribuidora_dvd.columnconfigure(0, weight=0)
editar_excluir_distribuidora_dvd.columnconfigure(1, weight=1)

Label(
    editar_excluir_distribuidora_dvd,
    text='Distribuidora',
    font='Arial 12'
).grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

nome_distribuidora_dvd_editar_excluir = AutocompleteCombobox(
    editar_excluir_distribuidora_dvd,
    font='Arial 12',
    completevalues=db.nome_distribuidoras_dvds()
)
nome_distribuidora_dvd_editar_excluir.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

botoes_editar_excluir_distribuidora_dvd = Frame(
    table_frame
)

botoes_editar_excluir_distribuidora_dvd.columnconfigure(0, weight=1)
botoes_editar_excluir_distribuidora_dvd.columnconfigure(1, weight=1)

botao_editar_distribuidora_dvd = Button(
    botoes_editar_excluir_distribuidora_dvd,
    text='Editar',
    font='Arial 12',
    relief=GROOVE,
    command=editar_distribuidora_dvd
)
botao_editar_distribuidora_dvd.grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky=EW
)

botao_cancelar_edicao_distribuidora_dvd = Button(
    botoes_editar_excluir_distribuidora_dvd,
    text='Cancelar',
    font='Arial 12',
    relief=GROOVE,
    command=cancelar_edicao_distribuidora_dvd
)
botao_cancelar_edicao_distribuidora_dvd.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky=EW
)

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
    command=adicionar_novo,
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
        'Editoras',
        'DVD\'s',
        'CD\'s',
        'Artistas/Autores CD\'s',
        'Diretores DVD\'s',
        'Distribuidoras DVD\'s',
        'Distribuidoras CD\'s'
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
