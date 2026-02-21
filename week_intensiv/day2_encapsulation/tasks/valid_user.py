class ValidUser:
    """ЗАДАЧА: Сеттер пароля с проверкой длины >= 8 и наличия цифр"""
    def __init__(self, user, pwd): self.username, self._password = user, pwd
    @property
    def password(self): return "********"
    @password.setter
    def password(self, val):
        if '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' in val:
            self.__password = val
        pass