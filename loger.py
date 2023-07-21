import datetime


class loger:
    def __init__(self, log):
        self.logfile = log

    def loging(self, text):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        text = f"{current_time}- {text}"
        with open(self.logfile, "a", encoding="utf-8") as file:
            file.write(text + "\n")
            print(text)