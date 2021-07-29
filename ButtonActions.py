from tkinter.constants import BOTH


class ButtonActions:
    def __init__(self):
        pass

    def mostra_livros(self, table_frame, tabela_livros, tabela_autores, tabela_editoras):
        tabela_autores.pack_forget()
        tabela_editoras.pack_forget()

        table_frame['text'] = 'Livros'

        tabela_livros.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

    def mostra_autores(self, table_frame, tabela_livros, tabela_autores, tabela_editoras):
        tabela_livros.pack_forget()
        tabela_editoras.pack_forget()

        table_frame['text'] = 'Autores'

        tabela_autores.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

    def mostra_editoras(self, table_frame, tabela_livros, tabela_autores, tabela_editoras):
        tabela_livros.pack_forget()
        tabela_autores.pack_forget()

        table_frame['text'] = 'Editoras'

        tabela_editoras.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )
