import sys
import json
import admin


class lod:
    def __init__(self):
        self.commands = {}

    class command:
        def __init__(self, name: str, com):
            self.name = name
            self.com = com

        def __call__(self, cls):
            self.com.commands[self.name] = cls
            return cls


class loader:
    def __init__(self):
        self.list = {}
        self.bot = None

    def compile(self, lo: lod, bot):
        self.list = lo.commands
        self.bot = bot

    async def process_commands(self, message):
        global current_time
        js = json.loads(open("configs/names.json").read())["names"]
        js.append(self.bot.user.name)
        for chech in js:
            if message.content.startswith(f"{chech} "):
                command = str(message.content).replace(f"{chech} ", '')
                for com in self.list:
                    if com in command:
                        if await admin.chec(message, admin.get_prem(self.list[com].__name__)):
                            return await self.list[com](message, command.replace(f"{com} ", ''))
