from db_manager import db_manager

db = db_manager()

livros_disponiveis = db.get_dvds_emprestimo_expirado()

print(livros_disponiveis)
