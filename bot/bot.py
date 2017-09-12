import requests
import json
import urllib.request, urllib.parse, urllib.error
import user, chat, update

class Bot:

    URL = str()

    def __init__(self, token):
        global URL
        self.token = token
        URL = 'https://api.telegram.org/bot{}/'.format(token)


    def get_url(self, url):
        response = requests.get(url)
        content = response.content.decode("utf8")
        return content

    def get_json_from_url(self, url):
        content = self.get_url(url)
        js = json.loads(content)
        return js

    def get_updates(self, offset=None):
        global URL
        url = URL + "getUpdates?timeout=5"
        if offset:
            url += '&offset={}'.format(offset)
        js = self.get_json_from_url(url)['result'][0]
        updates = update.Update(js)
        return updates
