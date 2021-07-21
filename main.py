from DBHelper import DBHelper
from colorama import Fore, Style

data_base = DBHelper()

while True:
    print('Opções:\n\t1 - Mostrar Tabela\n\t2 - Inserir Dado\n\t3 - Atualizar dado\n\t4 - Excluir dado\n\t5 - Sair')
    escolha = int(input('Escolha: '))

    if escolha == 1:

        while True:
            print('\tOpções:\n\t\t1 - Mostra a tabela livros\n\t\t2 - Mostrar a tabela autores\n\t\t3 - Mostrar a tabela editoras\n\t\t4 - Voltar')
            escolha_tabela = int(input('Escolha a tabela: '))

            if escolha_tabela == 1:
                data_base.mostrar_tabela('books')
                break

            elif escolha_tabela == 2:
                data_base.mostrar_tabela('authors')
                break

            elif escolha_tabela == 3:
                data_base.mostrar_tabela('publishing_companys')
                break

            elif escolha_tabela == 4:
                break

            else:
                print(Fore.RED + 'Escolha inválida!' + Style.RESET_ALL)

    elif escolha == 2:
        titulo_livro = input('Título: ')
        autor_livro = input('Autor(a): ')
        editora_livro = input('Editora: ')
        num_paginas_livro = int(input('Nº de páginas: '))
        proprietario_livro = input('Proprietario: ')

        data_base.add_valores(titulo_livro, autor_livro,
                              editora_livro, num_paginas_livro, proprietario_livro)

    elif escolha == 3:
        pass

    elif escolha == 4:
        pass

    elif escolha == 5:
        print(Fore.RED + 'Saindo do programa...' + Style.RESET_ALL)
        break

    else:
        print(Fore.RED + 'Escolha inválida!' + Style.RESET_ALL)
