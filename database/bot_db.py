import random
import sqlite3



def sql_creatr():
    global db, cursor
    db = sqlite3.connect('bot.sqlite3')
    cursor = db.cursor()

    if db:
        print('база данных потключина!')

    db.execute(
        'CREATE TABLE IF NOT EXISTS anketa'
        'id INTEGER PRIMARY KEU AUTOINCREMENT, '
        'teligram_id INTEGER UNIQE, '
        'username VARCHAR (50), '
        ' name_mentor VARCHAR (50), '
        ' direction VARCHAR(50), '
        ' age_mentor INTEGER, '
        ' group INTEGER) '
    )
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