import csv


class db_manager:
    def __init__(self):
        pass

    def get_data(self, file_name):
        with open(file_name, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)

            next(csv_reader)

            return list(csv_reader)

    def add_livro(self, titulo, autor, editora, n_pag, situacao, beneficiado, telefone, dt_emprestimo, dt_devolucao):
        file = open('livros.csv')
        reader = csv.reader(file)

        id = len(list(reader))

        with open('livros.csv', mode='a+', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            csv_writer.writerow([id, titulo, autor, editora, n_pag,
                                 situacao, beneficiado, telefone, dt_emprestimo, dt_devolucao])

        self.add_autor(autor)

        self.add_editora(editora)

    def add_autor(self, autor):
        file = open('autores_livros.csv')
        reader = csv.reader(file)

        id = len(list(reader))

        if autor not in self.nome_autores():
            with open('autores_livros.csv', mode='a+', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)

                csv_writer.writerow([id, autor])

    def add_editora(self, editora):
        file = open('editoras_livros.csv')
        reader = csv.reader(file)

        id = len(list(reader))

        if editora not in self.nome_editoras():
            with open('editoras_livros.csv', mode='a+', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)

                csv_writer.writerow([id, editora])

    def add_dvd(self, titulo, diretor, distribuidora, tempo, situacao, beneficiado, telefone, dt_emprestimo, dt_devolucao):
        file = open('dvds.csv')
        reader = csv.reader(file)

        id = len(list(reader))

        with open('dvds.csv', mode='a+', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            csv_writer.writerow([id, titulo, diretor, distribuidora, tempo,
                                 situacao, beneficiado, telefone, dt_emprestimo, dt_devolucao])

        self.add_diretor_dvd(diretor)
        self.add_distribuidora_dvd(distribuidora)

    def add_cd(self, titulo, artista_autor, distribuidora, tempo, situacao, beneficiado, telefone, dt_emprestimo, dt_devolucao):
        file = open('cds.csv')
        reader = csv.reader(file)

        id = len(list(reader))

        with open('cds.csv', mode='a+', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            csv_writer.writerow([id, titulo, artista_autor, distribuidora, tempo,
                                 situacao, beneficiado, telefone, dt_emprestimo, dt_devolucao])

        self.add_autor_artista_cd(artista_autor)
        self.add_distribuidora_cd(distribuidora)

    def add_diretor_dvd(self, diretor):
        file = open('diretores_dvds.csv')
        reader = csv.reader(file)

        id = len(list(reader))

        if diretor not in self.nome_diretores_dvds():
            with open('diretores_dvds.csv', mode='a+', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)

                csv_writer.writerow([id, diretor])

    def add_autor_artista_cd(self, autor_artista):
        file = open('autores_artistas_cds.csv')
        reader = csv.reader(file)

        id = len(list(reader))

        if autor_artista not in self.nome_autores_artistas_cds():
            with open('autores_artistas_cds.csv', mode='a+', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)

                csv_writer.writerow([id, autor_artista])

    def add_distribuidora_dvd(self, distribuidora):
        file = open('distribuidoras_dvds.csv')
        reader = csv.reader(file)

        id = len(list(reader))

        if distribuidora not in self.nome_diretores_dvds():
            with open('distribuidoras_dvds.csv', mode='a+', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)

                csv_writer.writerow([id, distribuidora])

    def add_distribuidora_cd(self, distribuidora):
        file = open('distribuidoras_cds.csv')
        reader = csv.reader(file)

        id = len(list(reader))

        if distribuidora not in self.nome_distribuidoras_cds():
            with open('distribuidoras_cds.csv', mode='a+', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)

                csv_writer.writerow([id, distribuidora])

    def nome_autores(self):
        with open('autores_livros.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)

            next(csv_reader)

            return [line[1] for line in csv_reader]

    def nome_editoras(self):
        with open('editoras_livros.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            next(csv_reader)

            return [line[1] for line in csv_reader]

    def titulo_livros(self):
        with open('livros.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            next(csv_reader)

            return [line[1] for line in csv_reader]

    def nome_diretores_dvds(self):
        with open('diretores_dvds.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            next(csv_reader)

            return [line[1] for line in csv_reader]

    def nome_autores_artistas_cds(self):
        with open('autores_artistas_cds.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            next(csv_reader)

            return [line[1] for line in csv_reader]

    def nome_distribuidoras_dvds(self):
        with open('distribuidoras_dvds.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            next(csv_reader)

            return [line[1] for line in csv_reader]

    def nome_distribuidoras_cds(self):
        with open('distribuidoras_cds.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            next(csv_reader)

            return [line[1] for line in csv_reader]
