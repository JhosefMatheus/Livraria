from db_manager import db_manager

db = db_manager()

print(db.get_data('cds.csv'))
