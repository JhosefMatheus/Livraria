from tkinter.constants import BOTH


class ButtonActions:
    def __init__(self):
        pass

    def mostra_livros(self, books_table, authors_table, publishing_companys_table, tree_scrool):
        authors_table.pack_forget()
        publishing_companys_table.pack_forget()
        books_table.pack(expand=True, fill=BOTH)
        tree_scrool.config(command=books_table.yview)

    def mostra_autores(self, books_table, authors_table, publishing_companys_table, tree_scrool):
        books_table.pack_forget()
        publishing_companys_table.pack_forget()
        authors_table.pack(expand=True, fill=BOTH)
        tree_scrool.config(command=authors_table.yview)

    def mostra_editoras(self, books_table, authors_table, publishing_companys_table, tree_scrool):
        books_table.pack_forget()
        authors_table.pack_forget()
        publishing_companys_table.pack(expand=True, fill=BOTH)
        tree_scrool.config(command=publishing_companys_table.yview)
