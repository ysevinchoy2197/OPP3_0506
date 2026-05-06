class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.__password = password

    def login(self, pw):
        return pw == self.__password

    def change_password(self, old, new):
        if old == self.__password:
            self.__password = new
            print("Password changed")
        else:
            print(False)

    def info(self):
        print(self.username, self._email)

