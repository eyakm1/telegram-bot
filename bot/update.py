import message

class Update:
    def __init__(self, js):
        for i in js:
            if i == 'message':
                m = message.Message(*dict(js['message'].keys()))
            self.__dict__[i] = js[i]
        print(self.__dict__)