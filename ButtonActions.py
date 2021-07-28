from tkinter.constants import BOTH


class ButtonActions:
    def __init__(self):
        pass

    def mostra_livros(self, books_table, authors_table, publishing_companys_table, tree_scrool, data_frame, title_book_label, title_book_entry, author_book_label, author_book_entry, publishing_company_label, publishing_company_entry, n_pages_label, n_pages_entry, owner_book_label, owner_book_entry):
        authors_table.pack_forget()
        publishing_companys_table.pack_forget()
        books_table.pack(expand=True, fill=BOTH)
        tree_scrool.config(command=books_table.yview)

        data_frame['text'] = 'Adicionar/Editar Livro'

        title_book_label.grid(row=0, column=0, padx=10, pady=10)
        title_book_entry.grid(row=0, column=1, padx=10, pady=10)

        author_book_label.grid(row=0, column=2, padx=10, pady=10)
        author_book_entry.grid(row=0, column=3, padx=10, pady=10)

        publishing_company_label.grid(row=0, column=4, padx=10, pady=10)
        publishing_company_entry.grid(row=0, column=5, padx=10, pady=10)

        n_pages_label.grid(row=1, column=0, padx=10, pady=10)
        n_pages_entry.grid(row=1, column=1, padx=10, pady=10)

        owner_book_label.grid(row=1, column=2, padx=10, pady=10)
        owner_book_entry.grid(row=1, column=3, padx=10, pady=10)

    def mostra_autores(self, books_table, authors_table, publishing_companys_table, tree_scrool, data_frame, title_book_label, title_book_entry, author_book_label, author_book_entry, publishing_company_label, publishing_company_entry, n_pages_label, n_pages_entry, owner_book_label, owner_book_entry):
        books_table.pack_forget()
        publishing_companys_table.pack_forget()
        authors_table.pack(expand=True, fill=BOTH)
        tree_scrool.config(command=authors_table.yview)

        data_frame['text'] = 'Editar Autores'

        title_book_label.grid_forget()
        title_book_entry.grid_forget()

        author_book_label.grid(row=0, column=0, padx=10, pady=10)
        author_book_entry.grid(row=0, column=1, padx=10, pady=10)

        publishing_company_label.grid_forget()
        publishing_company_entry.grid_forget()

        n_pages_label.grid_forget()
        n_pages_entry.grid_forget()

        owner_book_label.grid_forget()
        owner_book_entry.grid_forget()

    def mostra_editoras(self, books_table, authors_table, publishing_companys_table, tree_scrool, data_frame, title_book_label, title_book_entry, author_book_label, author_book_entry, publishing_company_label, publishing_company_entry, n_pages_label, n_pages_entry, owner_book_label, owner_book_entry):
        books_table.pack_forget()
        authors_table.pack_forget()
        publishing_companys_table.pack(expand=True, fill=BOTH)
        tree_scrool.config(command=publishing_companys_table.yview)

        data_frame['text'] = 'Editar Editoras'

        title_book_label.grid_forget()
        title_book_entry.grid_forget()

        author_book_label.grid_forget()
        author_book_entry.grid_forget()

        publishing_company_label.grid(row=0, column=0, padx=10, pady=10)
        publishing_company_entry.grid(row=0, column=1, padx=10, pady=10)

        n_pages_label.grid_forget()
        n_pages_entry.grid_forget()

        owner_book_label.grid_forget()
        owner_book_entry.grid_forget()
