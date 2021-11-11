import sqlite3

db = sqlite3.connect('users_db.db')
sql = db.cursor()


def add_components(name, cal, prot, fats, carbs):
    db = sqlite3.connect('users_db.db')
    sql = db.cursor()

    sql.execute(
        f"INSERT INTO food (name_food, calories, protein, fats, carb) VALUES ('{name}','{cal}', '{prot}', '{fats}',"
        f" '{carbs}')")
    db.commit()

    sql.close()
    db.close()
