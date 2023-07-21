import json
import sqlite3


class db:
    def __init__(self, db):
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mytable (
                id TEXT PRIMARY KEY,
                data TEXT
            )
        ''')
        self.conn = conn
        self.cursor = cursor

    def get(self):
        self.cursor.execute("SELECT * FROM mytable")
        rows = self.cursor.fetchall()
        datas = {}
        for row in rows:
            datas[row[0]] = json.loads(row[1])
        return datas

    def set(self, data):
        for com in data:
            self.cursor.execute("INSERT OR REPLACE INTO mytable (id, data) VALUES (?, ?)", (str(com), str(json.dumps(data[com]))))
        self.conn.commit()

    def close(self):
        self.conn.close()


#bd = db("acounts.db")
#ss = bd.get()
#print(ss)
#ss["wewqeewe"] = {}
#print(ss)
#bd.set(ss)
#print(bd.get())