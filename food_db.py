import sqlite3


def add_components(name, cal, prot, fats, carbs):
    db = sqlite3.connect('users_db.db')
    sql = db.cursor()

    sql.execute(
        f"INSERT INTO food (name_food, calories, protein, fats, carb) VALUES ('{name}','{cal}', '{prot}', '{fats}',"
        f" '{carbs}')")
    db.commit()

    sql.close()
    db.close()


def deleting(name):
    db = sqlite3.connect('users_db.db')
    sql = db.cursor()

    sql.execute(f"DELETE FROM food WHERE name_food = '{name}'")
    db.commit()

    sql.close()
    db.close()


def save_values(cal, prot, fats, carbs):
    db = sqlite3.connect('users_db.db')
    sql = db.cursor()

    sql.execute(f"INSERT INTO foods_values (calories, proteins, fats, carbs) VALUES ('{cal}', '{prot}', '{fats}',"
                f" '{carbs}')")
    db.commit()

    sql.close()
    db.close()


def return_values():
    db = sqlite3.connect('users_db.db')
    sql = db.cursor()

    sql.execute(f"SELECT calories, proteins, fats, carbs FROM foods_values")
    elem = sql.fetchone()

    return elem

    sql.close()
    db.close()


def save_water(val):
    db = sqlite3.connect('users_db.db')
    sql = db.cursor()

    sql.execute(f"INSERT INTO foods_values (water) VALUES ('{val}')")
    db.commit()

    sql.close()
    db.close()


def return_water():
    db = sqlite3.connect('users_db.db')
    sql = db.cursor()

    sql.execute(f"SELECT carbs, water FROM foods_values")
    elem = sql.fetchone()[0]

    return elem

    sql.close()
    db.close()