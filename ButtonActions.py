from tkinter.constants import BOTH, X


class ButtonActions:
    def __init__(self):
        pass

    def change_table(self, drop_down, register_frame, button_register_frame, table_frame, tabela_livros, tabela_autores, tabela_editoras):
        register_frame.pack_forget()
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

    def add_click(self, table_frame, tabela_livros, tabela_autores, tabela_editoras, register_frame, button_register_frame):
        table_frame['text'] = 'Novo'

        tabela_livros.pack_forget()
        tabela_autores.pack_forget()
        tabela_editoras.pack_forget()

        register_frame.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

        button_register_frame.pack(
            expand=False,
            fill=X,
            padx=10,
            pady=10
        )

    def cancel_register_click(self, table_frame, register_frame, button_register_frame, tabela_livros):
        table_frame['text'] = 'Livros'

        register_frame.pack_forget()
        button_register_frame.pack_forget()

        tabela_livros.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )
