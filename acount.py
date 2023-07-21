import json
import db
import initer


class ac:
    def __init__(self, bot):
        self.bot = bot
        self.db = db.db("acounts/acounts.db")

    async def loader(self, messege):
        ss = self.db.get()
        if str(messege.author.id) in ss:
            ss[str(messege.author.id)]["score"] += 1

        else:
            ss[str(messege.author.id)] = {
                "score": 0,
                "warns": 0,
                "permissions": 0,
                "whiles": False,
                "black": False,
                "complaints": 0
            }
        self.db.set(ss)
        return ss[str(messege.author.id)]

    async def get(self, id):
        if str(id) in self.db.get():
            return self.db.get()[str(id)]
        else:
            return {"data": f"acount no found {id}"}

    async def set(self, id: int, data):
        a = self.db.get()
        a[str(id)] = data
        self.db.set(a)