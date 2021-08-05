from tkinter.constants import BOTH, S, N, X


class ButtonActions:
    def __init__(self):
        pass

    def change_table(self, drop_down, livro_register_frame, button_register_frame, table_frame, tabela_livros, tabela_autores, tabela_editoras):
        livro_register_frame.pack_forget()
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

    def add_click(self, table_frame, tabela_livros, tabela_autores, tabela_editoras, livro_register_frame, button_register_frame):
        table_frame['text'] = 'Novo Livro'

        tabela_livros.pack_forget()
        tabela_autores.pack_forget()
        tabela_editoras.pack_forget()

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

    def cancel_register_click(self, table_frame, drop_down_register, livro_register_frame, autor_register_frame, editora_register_frame, button_register_frame, tabela_livros):
        table_frame['text'] = 'Livros'

        if drop_down_register.get() == 'Livro':
            livro_register_frame.pack_forget()

        elif drop_down_register.get() == 'Autor':
            autor_register_frame.pack_forget()

        elif drop_down_register.get() == 'Editora':
            editora_register_frame.pack_forget()

        button_register_frame.pack_forget()

        tabela_livros.pack(
            expand=True,
            fill=BOTH,
            padx=10,
            pady=10
        )

    def change_register_frame(self, drop_down_register, table_frame, livro_register_frame, autor_register_frame, editora_register_frame, button_register_frame):
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
