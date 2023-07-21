import json


def getwhilelist():
    return json.loads(open("configs/hilelist.json", encoding="utf-8").read())["while"]


def getblack():
    return json.loads(open("configs/black.json", encoding="utf-8").read())["black"]