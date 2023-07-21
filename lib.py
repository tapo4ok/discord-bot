def compil(text, args):
    for txt in args:
        text = text.replace(f"%{txt}%", str(args[txt]))
    return text