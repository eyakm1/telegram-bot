class Chat:
    def __init__(self, id, type, title='', username='', first_name='', last_name='', all_members_are_administrators=True):
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.all_members_are_administrators = all_members_are_administrators
