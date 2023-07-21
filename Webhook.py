import requests
import json


class webhook:
    def __init__(self, WEBHOOK_URL):
        self.WEBHOOK_URL = f"https://discord.com/api/webhooks/{WEBHOOK_URL}"

    def send(self, content, name):
        requests.post(self.WEBHOOK_URL, headers={'Content-Type': 'application/json'}, data=json.dumps({'content': content, 'username': name}))

    def __aenter__(self):
        return self

    def __aexit__(self, exc_type, exc_value, traceback):
        pass