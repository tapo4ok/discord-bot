import json
import configparser
config = configparser.ConfigParser()
config.read('configs/permissions.properties')
properties_data = {}
for section in config.sections():
    properties_data[section] = {}
    for option in config.options(section):
        properties_data[section][option] = config.get(section, option)
permissions = properties_data["permissions"]
splitpermissions = properties_data["splitpermissions"]


def get_prem(id):
    if id in permissions:
        return int(permissions[id])
    else:
        return 0


def sget_prem(id):
    if id in permissions:
        return int(permissions[id])
    else:
        return 0


async def chec(ctx, level):
    admins = json.loads(open("configs/admins.json").read())
    try:
        if str(ctx.author.id) in admins and (
                admins[str(ctx.author.id)]["permissionslevel"] > level or admins[str(ctx.author.id)]["permissionslevel"] == level):
            return True
    except:
        pass
    if level == 0:
        return True
    await ctx.channel.send("недостаточно прав")
    return False