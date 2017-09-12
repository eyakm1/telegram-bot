class User:
    def __init__(self, id, is_bot, first_name, last_name='', username='', language_code=''):
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code