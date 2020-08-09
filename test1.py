class User():
    """Users class"""

    def __init__(self, name, surname, username, password):
        """User basic attributes"""
        self.name = name
        self.surname = surname
        self.username = username
        self.password = password
        self.login_account = 0

    def describe_user(self):
        """User's summary info"""
        return print(f"{self.name} {self.surname} \n{self.username} {self.password}")

    def greet_user(self):
        """Say hello to user"""
        return print(f"Hello {self.name} {self.surname}!")

    def increment_login_attempts(self):
        """Increment login attempts"""
        self.login_account += 1

    def reset_login_attempts(self):
        """Reset login attempt"""
        if self.login_account == 5:
            self.login_account = 0

user1 = User("Tomas", "Sivak", "yubjklhu", "Start123")
#user1.describe_user()
#user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"{user1.login_account}")
user1.reset_login_attempts()
print(f"{user1.login_account}")

#user2 = User("Stefan", "Tomko", "sku15894", "Kapu$tnica")
#user3 = User("Danilo", "Telebakovic", "fkuingyd", "Klepa*89Kk")
#user2.describe_user()
#user2.greet_user()
#user3.describe_user()
#user3.greet_user()
