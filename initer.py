import uuid


class init:
    def __init__(self, json={}):
        self.json = json

    def __call__(self, cls):
        for js in self.json:
            setattr(cls, js, self.json[js])
        setattr(cls, "__id__", str(uuid.uuid4()))
        cls = cls()
        return cls