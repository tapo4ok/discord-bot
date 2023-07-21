import datetime
import loger
import sys
import discord
from discord.ext import commands
import Webhook as wb
import configs
import weblib
import lang as lan
import random
import oper
import lib
import os
import acount
import json
import ctypes
import admin
from cammand import loader as comlod
print(sys.argv)
current_time = datetime.datetime.now().strftime("%H:%M:%S").replace(":", "-")
log = loger.loger(f"logs/bot-{current_time}.log")
os.system("")
clarcoder = oper.clarcoder
lang = lan.land("configs/lang.json")
lang.getkang()


current_directory = os.getcwd() + "/"


def change_wallpaper(image_path):
    bytes = [0x0014, 0x01, 0x02]
    ctypes.windll.user32.SystemParametersInfoW(bytes[0], 0, image_path, bytes[1] | bytes[2])


configss = json.loads(open("configs/bat.json", encoding="utf-8").read())


command_prefix = configss["command_prefix"]
bot = commands.Bot(command_prefix=command_prefix, intents=discord.Intents.all())
lod = comlod.lod()
loader = comlod.loader()
acountp = acount.ac(bot)


@bot.event
async def on_ready():
    with lang.get("4000-0000-0000-0000") as txt:
        activity = discord.Activity(type=discord.ActivityType.playing, name=txt.text[0][0].format(len(bot.guilds)))
        await bot.change_presence(activity=activity)
        log.loging('Bot is ready')
    

@clarcoder
class MusicPlayer:
    def __init__(self, ctx):
        self.ctx = ctx
        self.voice_client = None
        self.queue = []

    async def join(self):
        if not self.voice_client:
            async with await self.ctx.author.voice.channel.connect() as voice_client:
                self.voice_client = voice_client

    async def leave(self):
        if self.voice_client:
            await self.voice_client.disconnect()
            self.voice_client = None


players = {}


@clarcoder
class helper:
    def __init__(self):
        self.funcs = []

    def func(self, func):
        class funcs:
            def __init__(self, name, args):
                self.name = name
                self.args = args
        self.funcs.append(funcs(func.__name__, str(func.__code__.co_varnames).replace("(", "[").replace(")", "]").replace("'ctx', ", "").replace("'", "")))
        return func

    def get(self):
        const = "```"
        for fn in self.funcs:
            const += f"{command_prefix}{fn.name}: {fn.args}\n"
        return const + "```"


helper = helper()
# com


@lod.command("кто", lod)
@helper.func
async def kto(messege, content):
    txt = lang.get("5000-0000-0000-0000")
    nameew = ""
    while True:
        nemb = random.choice(messege.guild.members)
        if not (nemb == bot.user):
            nameew = str(nemb)
            break
        if not (nemb == bot.user):
            nameew = str(nemb)
            break
    await messege.channel.send(txt.text["prefix"] + lib.compil(random.choice(txt.text["list"]), {"user": nameew, "arg": content, "author": messege.author}) + txt.text["sufix"])


@lod.command("скажи", lod)
@helper.func
async def AA113123(messege, content):
    await messege.channel.send(random.choice(["да", "нет", "хохохо"]))


@lod.command("спать", lod)
@helper.func
async def spat(messege, content):
    activity = discord.Activity(type=discord.ActivityType.playing, name="бот спит")
    await bot.change_presence(activity=activity)
    await messege.channel.send("спокойной ночи")
    await bot.http.close()
    await bot.close()


# com


@bot.command(name='join', aliases=['j'])
@helper.func
async def join(ctx):
    if ctx.guild.id not in players:
        players[ctx.guild.id] = MusicPlayer(ctx)

    player = players[ctx.guild.id]
    await player.join()


@bot.command(name='a')
@helper.func
async def awadad(ctx, role_id, user_id):
    role = ctx.guild.get_role(int(role_id))
    if role is not None:
        member = ctx.guild.get_member(int(user_id))
        if member is not None:
            if role in member.roles:
                await ctx.send(f"The user {member.name} has the role {role.name}.")
            else:
                await ctx.send(f"The user {member.name} does not have the role {role.name}.")
        else:
            await ctx.send("Invalid user ID.")
    else:
        await ctx.send("Invalid role ID.")

@bot.command(name='leave', aliases=['l'])
@helper.func
async def leave(ctx):
    if ctx.guild.id in players:
        player = players[ctx.guild.id]
        await player.leave()
        del players[ctx.guild.id]


@bot.command(name='spam')
@helper.func
async def sp2222(ctx, count: int, *, messege):
    if await admin.chec(ctx, admin.get_prem(ctx.command.name)):
        for o in range(count):
            await ctx.send(f"{messege} {o}")


@bot.command()
@helper.func
async def gethelp(ctx):
    await ctx.send(helper.get())


@bot.command(name='acount_get')
@helper.func
async def acount_get(ctx, id):
    if await admin.chec(ctx, admin.get_prem(ctx.command.name)):
        if str(id) in acountp.db.get():
            x = f"{json.dumps(acountp.db.get()[str(id)])}\n"
            ct = acountp.db.get()[str(id)]
            for a in ct:
                x += f"{a}: {ct[a]}\n"
        else:
            x = {"data": f"acount no found {id}"}
            await ctx.send(x)


@bot.command(name='acount_set')
@helper.func
async def acount_set(ctx, id, *, messege):
    if await admin.chec(ctx, admin.get_prem(ctx.command.name)):
        js = {}
        js[str(id)] = json.loads(messege)
        acountp.db.set(js)
        await ctx.send("ac set")


@bot.command()
@helper.func
async def stop(ctx):
    if await admin.chec(ctx, admin.get_prem(ctx.command.name)):
        activity = discord.Activity(type=discord.ActivityType.playing, name="бот уходит на тех обслуживания")
        await bot.change_presence(activity=activity)
        await ctx.send("bot stoped")
        await bot.http.close()
        await bot.close()


@bot.command()
@helper.func
async def get_avatar_urlid(ctx, user_id):
    if await admin.chec(ctx, admin.get_prem(ctx.command.name)):
        user = await bot.fetch_user(user_id)
        avatar_url = user.avatar_url
        await ctx.send(avatar_url)


@bot.command()
@helper.func
async def get_avatar_urluser(ctx, member: discord.Member):
    if await admin.chec(ctx, admin.get_prem(ctx.command.name)):
        avatar_url = member.avatar_url
        await ctx.send(avatar_url)


@bot.command()
@helper.func
async def send_dm(ctx, user_id, *, message):
    var1 = lang.get("6000-0000-0000-0000").text
    var2 = lang.get("7000-0000-0000-0000").text
    if await admin.chec(ctx, admin.get_prem(ctx.command.name)):
        try:
            user = await bot.fetch_user(user_id)
            if user.id in configs.getwhilelist():
                await ctx.send(var2.format(user.name))
                log.loging(var2.format(user.name))
                return
            await user.send(message)
            for o in webhooks:
                o.send(var1.format(user.name, ctx.author), "logs")
            await ctx.send(var1.format(user.name))
            log.loging(var1.format(user.name))
        except Exception as e:
            print(e)
            await ctx.send(e)


@bot.command()
@helper.func
async def send_dm_spam(ctx, user_id, *, message):
    var1 = lang.get("6000-0000-0000-0000").text
    var2 = lang.get("7000-0000-0000-0000").text
    if await admin.chec(ctx, admin.get_prem(ctx.command.name)):
        try:
            user = await bot.fetch_user(user_id)
            if user.id in configs.getwhilelist():
                await ctx.send(var2.format(user.name))
                log.loging(var2.format(user.name))
                return
            for _ in range(5):
                await user.send(message)
            for o in webhooks:
                o.send(var1.format(user.name, ctx.author), "logs")
            await ctx.send(var1.format(user.name, ctx.author))
            log.loging(var1.format(user.name, ctx.author))
        except Exception as e:
            print(e)
            await ctx.send(e)


webhooks = []
for ks in ["1119987943654825994/3OObKy26fv_BU6Qk3CJt-dLJVdMWGLBzgWVjb_1QcbnDnQup5OuGWQvGNIrfK7ib73cZ"]:
    webhooks.append(wb.webhook(ks))

loader.compile(lod, bot)


@bot.event
@helper.func
async def on_message(message):
    with lang.get("3000-0000-0000-0000") as txt:
        if message.author == bot.user:
            return
        if message.channel.type == discord.ChannelType.private:
            author = message.author
            content = message.content
            if not author.id in configs.getblack():
                for webhook in webhooks:
                    webhook.send(str(txt.text).format(author.name, content, author.id), "logs")
            log.loging(str(txt.text).format(author.name, content, author.id))

        await acountp.loader(message)
        await loader.process_commands(message)
        await bot.process_commands(message)


@bot.event
async def on_error(event, *args, **kwargs):
    log.loging(f"Ошибка обработки события: {str(sys.exc_info())}")


def run():
    log.loging("token get")
    lib = weblib.get(configss["weblib.get"])
    with lib.get(configss["id"]) as TOKEN:
        log.loging("bot runing")
        bot.run(str(TOKEN.text))
