import requests
import json
import urllib.request, urllib.parse, urllib.error


token = '343449335:AAFxTPTZFOIngsEJR1fHtBaqHFcmYQ7w2HQ'
URL = 'https://api.telegram.org/bot{}/'.format(token)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    print(js)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=5"
    if offset:
        url += '&offset={}'.format(offset)
    js = get_json_from_url(url)
    return js


def get_last_text(updates):
    count_updates=len(updates['result'])
    last_update=count_updates-1
    text = updates['result'][last_update]['message']['text']
    return (text)


def get_last_chat_id(updates):
    count_updates=len(updates['result'])
    last_update=count_updates-1
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return(chat_id)


def send_msg(text, chat_id):
    url = URL + 'sendmessage?text={}&chat_id={}'.format(text, chat_id)
    get_url(url)


def download_file(updates):
    count_updates=len(updates['result'])
    last_update=count_updates-1
    file_id=updates['result'][last_update]['message']['document']['file_id']
    js = get_json_from_url(URL + 'getfile?file_id={}'.format(file_id))
    filepath = js['result']['file_path']
    urllib.request.urlretrieve('https://api.telegram.org/file/bot{}/{}'.format(token, filepath), 'pythonfile.py')


def get_last_update_id(updates):
    updates_ids = []
    for update in updates['result']:
        updates_ids.append(update['update_id'])
    return(max(updates_ids))


def echo_file(file_name):
    download_file(get_updates())
    text = ''
    with open(file_name, 'r') as file:
        for line in file:
            text += line
    send_msg(text, get_last_chat_id(get_updates()))


def check_msg_type(updates):
    count_updates = len(updates['result'])
    last_update = count_updates - 1
    if 'document' in updates['result'][last_update]['message']:
        return 'file'
    else:
        return 'text'


def check_file_mime_type(updates):
    count_updates = len(updates['result'])
    last_update = count_updates - 1
    return updates['result'][last_update]['message']['document']['mime_type']

def main():
    last_update_id = None
    while True:
        print("getting updates")
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            msg_type = check_msg_type(updates)
            if msg_type == 'file':
                if check_file_mime_type(updates) == 'text/x-python':
                    echo_file('pythonfile.py')
                else:
                    send_msg('ОШИБКА: посланный файл не является python скриптом', get_last_chat_id(updates))
            else:
                send_msg('Вышлите код в python файле', get_last_chat_id(updates))

if __name__ == '__main__':
    main()