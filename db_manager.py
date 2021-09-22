import csv


class db_manager:
    def __init__(self):
        pass

    def get_data(self, file_name):
        with open(file_name, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)

            next(csv_reader)

            return list(csv_reader)
