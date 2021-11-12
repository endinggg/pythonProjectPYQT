import sqlite3

db = sqlite3.connect('users_db.db')
sql = db.cursor()

sql.execute("SELECT id FROM users")
rows = sql.fetchall()

index_user = (len(rows))
user_count = 0
username = ''


def login(name, password, signal):
    db = sqlite3.connect('users_db.db')
    sql = db.cursor()
    sql.execute(f'SELECT * FROM users WHERE name="{name}";')
    value = sql.fetchall()

    if value != [] and value[0][2] == password:
        return 1
    else:
        signal.emit('Проверьте правильность ввода данных!')
        return 0

    sql.close()
    db.close()


def register(name, password, signal):
    global index_user

    db = sqlite3.connect('users_db.db')
    sql = db.cursor()

    sql.execute(f'SELECT * FROM users WHERE name="{name}";')
    value = sql.fetchall()

    if not value == []:
        signal.emit('Такой ник уже используется!')

    elif not value != []:
        sql.execute(f"INSERT INTO users (name, password, count) VALUES ('{name}', '{password}', '{user_count}')")

        index_user += 1

        signal.emit('Вы успешно зарегистрированы!')
        db.commit()

    sql.close()
    db.close()


def users_parametrs(user_height, user_weight, user_age):
    global user_count

    db = sqlite3.connect('users_db.db')
    sql = db.cursor()

    sql.execute(f"UPDATE users SET height = {user_height}, weight = {user_weight}, age = {user_age}, count = 1 WHERE "
                f"id = '{index_user}'")
    user_count = 1
    db.commit()

    sql.close()
    db.close()


def check_log(name):
    global username

    username = name
    db = sqlite3.connect('users_db.db')
    sql = db.cursor()
    sql.execute(f"SELECT id, count FROM users WHERE name = '{name}'")
    elem = sql.fetchone()[1]

    return elem

    sql.close()
    db.close()


def give_values():
    db = sqlite3.connect('users_db.db')
    sql = db.cursor()
    sql.execute(f"SELECT height, weight, age FROM users WHERE name = '{username}'")
    elem = sql.fetchone()

    return elem

    sql.close()
    db.close()
