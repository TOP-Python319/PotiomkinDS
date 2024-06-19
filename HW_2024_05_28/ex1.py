class PasswordInvalidError(Exception):
    """Пользовательский базовый класс исключений"""
    

class PasswordLengthError(PasswordInvalidError):
    """Исключение при недостаточной длине пароля"""
    def __str__(self) -> str:
        return 'Пароль должен состоять из не менее 8 символов'


class PasswordContainUpperError(PasswordInvalidError):
    """Исключение при отсутствии в пароле заглавных букв"""
    def __str__(self) -> str:
        return 'Пароль должен содержать хотя бы одну заглавную букву'


class PasswordContainDigitError(PasswordInvalidError):
    """Исключение при отсутствии в пароле цифр"""
    def __str__(self) -> str:
        return 'Пароль должен содержать хотя бы одну цифру'


class User:
    """Инициализватор класса пользователя"""
    def __init__(self, username: str, password: str=None):
        self.username = username
        self.password = password
    """Метод проверки валидности и установки пароля"""
    def set_password(self, password: str):
        if len(password) < 8:
            raise PasswordLengthError()
        elif not any(char.isupper() for char in password):
            raise PasswordContainUpperError()
        elif not any(char.isdigit() for char in password):
            raise PasswordContainDigitError()
        self.password = password



assert issubclass(PasswordInvalidError, Exception)
assert issubclass(PasswordLengthError, PasswordInvalidError)
assert issubclass(PasswordContainUpperError, PasswordInvalidError)
assert issubclass(PasswordContainDigitError, PasswordInvalidError)   

user = User("johndoe")

try:
    user.set_password("weakpwd")
except PasswordLengthError as e:
    print(e)

try:
    user.set_password("strongpassword8")
except PasswordContainUpperError as e:
    print(e)

try:
    user.set_password("Safepassword")
except PasswordContainDigitError as e:
    print(e)

user.set_password("SecurePass123")
assert user.password == 'SecurePass123'


################################################

# Пароль должен состоять из не менее 8 символов
# Пароль должен содержать хотя бы одну заглавную букву
# Пароль должен содержать хотя бы одну цифру