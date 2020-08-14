class User():
    """User class"""

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
        print(f"This is login attempt number {self.login_account} of "
              f"user {user1.name} {user1.surname}!")
        if self.login_account > 4:
            print(f"User {user1.name} {user1.surname} you have exceeded allowed number "
                  f"of login attempts and your account is now locked!")

    def reset_login_attempts(self):
        """Reset login attempt"""
        if self.login_account == 5:
            self.login_account = 0

class Admin(User):
    """Bla bla bla"""

    def __init__(self, name, surname, username, password):
        """Initialize attributes of the parent class."""
        super().__init__(name, surname, username, password)
        self.privileges = Privileges()


class Privileges():
    """Bla bla bla"""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        """Shows admin privileges"""
        a = str(self.privileges)[0:]
        return print(f"{a}")


user1 = Admin("Tomas", "Sivak", "yubjklhu", "Start123")
user1_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
user1.privileges.privileges = user1_privileges
user1.privileges.show_privileges()




