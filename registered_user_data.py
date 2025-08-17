# Файл содержит класс RegisteredUser, который хранит данные заранее зарегистрированного на сайте пользователя. 
# Эти данные нужны для автотестов, где требуется использовать существующий аккаунт.

class RegisteredUser:
    def __init__(self):
        # Данные уже существующего пользователя (заранее зарегистрирован на сайте)
        self.name = "Анна Родевич"
        self.email = "hanna_radzevich_28_123@yandex.com"
        self.password = "password123"
    
    # Возвращает данные существующего пользователя
    def get_registered_user(self):
        return {"name": self.name, "email": self.email, "password": self.password}
