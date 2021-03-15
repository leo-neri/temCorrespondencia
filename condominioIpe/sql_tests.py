import sqlite3

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()


def execute(command: str):
    cur.execute(command)
    results = cur.fetchall()
    print(results)


execute("SELECT name FROM sqlite_master WHERE type ='table';")
execute("SELECT * FROM temCorrespondencia_morador")
execute("SELECT * FROM temCorrespondencia_encomenda")

con.commit()
con.close()
