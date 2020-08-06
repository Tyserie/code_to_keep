class User():
    """Users class"""

    def __init__(self, name, surname, username, password):
        """User basic attributes"""
        self.name = name
        self.surname = surname
        self.username = username
        self.password = password

    def describe_user(self):
        """User's summary info"""
        return print(f"{self.name} {self.surname} \n{self.username} {self.password}")

    def greet_user(self):
        """Say hello to user"""
        return print(f"Hello {self.name} {self.surname}!")

user1 = User("Tomas", "Tyser", "fbcqlky", "Start123")
user2 = User("Stefan", "Tomko", "sku15894", "Kapu$tnica")
user3 = User("Danilo", "Telebakovic", "fkuingyd", "Klepa*89Kk")

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
