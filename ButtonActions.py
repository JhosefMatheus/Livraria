from tkinter.constants import BOTH, BOTTOM, EW, X


class ButtonActions:
    def __init__(self):
        pass

    def change_table(self, drop_down, table_frame, tabela_livros, tabela_autores, tabela_editoras, fields_register_frame, label_titulo, entry_titulo, label_autor, entry_autor, label_editora, entry_editora, label_n_pages, entry_n_pages, label_proprietario, entry_proprietario, button_register_frame, button_adicionar, button_cancelar):
        label_titulo.grid_forget()
        entry_titulo.grid_forget()

        label_autor.grid_forget()
        entry_autor.grid_forget()

        label_editora.grid_forget()
        entry_editora.grid_forget()

        label_n_pages.grid_forget()
        entry_n_pages.grid_forget()

        label_proprietario.grid_forget()
        entry_n_pages.grid_forget()

        fields_register_frame.pack_forget()

        button_adicionar.grid_forget()
        button_cancelar.grid_forget()

        button_register_frame.pack_forget()

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

    def adicionar(self, table_frame, tabela_livros, tabela_autores, tabela_editoras, fields_register_frame, label_titulo, entry_titulo, label_autor, entry_autor, label_editora, entry_editora, label_n_pages, entry_n_pages, label_proprietario, entry_proprietario, button_register_frame, button_adicionar, button_cancelar):
        table_frame['text'] = 'Cadastrar'

        tabela_livros.pack_forget()
        tabela_autores.pack_forget()
        tabela_editoras.pack_forget()

        fields_register_frame.pack(
            fill=BOTH,
            expand=True,
            padx=10,
            pady=10
        )

        label_titulo.grid(row=0, column=0, padx=10, pady=10)
        entry_titulo.grid(row=0, column=1, padx=10, pady=10)

        label_autor.grid(row=1, column=0, padx=10, pady=10)
        entry_autor.grid(row=1, column=1, padx=10, pady=10)

        label_editora.grid(row=2, column=0, padx=10, pady=10)
        entry_editora.grid(row=2, column=1, padx=10, pady=10)

        label_n_pages.grid(row=3, column=0, padx=10, pady=10)
        entry_n_pages.grid(row=3, column=1, padx=10, pady=10)

        label_proprietario.grid(row=4, column=0, padx=10, pady=10)
        entry_proprietario.grid(row=4, column=1, padx=10, pady=10)

        button_register_frame.pack(
            fill=X,
            expand=False,
            padx=10,
            pady=10,
            side=BOTTOM
        )

        button_register_frame.columnconfigure(0, weight=1)
        button_register_frame.columnconfigure(1, weight=1)

        button_adicionar.grid(row=0, column=0, padx=10, pady=10, sticky=EW)
        button_cancelar.grid(row=0, column=1, padx=10, pady=10, sticky=EW)
