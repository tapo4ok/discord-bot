import json
import oper
clarcoder = oper.clarcoder


@clarcoder
class land:
    def __init__(self, file):
        self.file = file
        self.joson = {}

    def getkang(self):
        self.joson = json.loads(open(self.file, encoding="utf-8").read())

    def get(self, lang):
        @clarcoder
        class get:
            def __init__(self, text):
                self.text = text

            def __enter__(self):
                return self

            def __exit__(self, exc_type, exc_value, traceback):
                pass

        return get(self.joson[lang])