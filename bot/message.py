import user, chat

class Message:
    def __init__(self, message_id, fromuser, chat, date, text='', document=''):
        self.id = message_id
        self.fromuser = fromuser
        self.date = date
        self.chat = chat
        self.text = text
        self.document = document
