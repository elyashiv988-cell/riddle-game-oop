class Player:
    def __init__(self, username:str):
        self.__username=username

    @property
    def username(self):
        return self.__username

    def get_username(self):
        return self.__username

    def rename(self, new_username):
        if len(new_username.strip())>2:
            self.__username=new_username
