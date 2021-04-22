class User():
    def __init__(self, username, nickname, email, password):
        self.username = username
        self.nickname = nickname
        self.email = email
        self.password = password

    def to_json(self):
        return {
            'username': self.username,
            'nickname': self.nickname,
            'email': self.email,
            'password': self.password
        }
