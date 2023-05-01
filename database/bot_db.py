import random
import sqlite3



def sql_creatr():
    global db, cursor
    db = sqlite3.connect('bot.sqlite3')
    cursor = db.cursor()

    if db:
        print('база данных потключина!')

    db.execute(
        'CREATE TABLE IF NOT EXISTS users'
        '(teligram_id INTEGER PRIMARY KEU , '
        'username VARCHAR (50), '
        'fullname VARCHAR (50))'
    )
    db.commit()


async def sql_command_all_uses():
    return cursor.execute('SELECT * FROM uses').fetchall

async def sql_command_inster_user(telegram_id, username, fullname):
    cursor.execute('INSERT INTO users VALUES  (?, ?, ?)', (telegram_id, username, fullname))
    db.commit()


async def sql_command_inster(state):
  async with state.proxy() as data:
      cursor.execute('INSERT INTO anketa VALUES '
                     '(null, ?, ?, ?, ?, ?, ?)', tuple(data.valuse()))
      db.commit()

async def sql_command_random():
    users = cursor.execute('SELECT * FROM anketa').fetchall()
    random_user = random.choice(users)
    return random_user

async def sql_command_all():
    return cursor.execute('SELECT * FROM aketa').fetchall()

async def sql_command_delete(id):
    cursor.execute('DELETE FROM anketa WHERE ID == ?', (id,))
    db.commit()