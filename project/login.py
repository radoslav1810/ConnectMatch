

import time
from project.database import Database




class Login:
    MAX_LOGIN_ATTEMPTS = 3
    BAN_DURATION_SECONDS = 180

    def __init__(self):
        self.database = Database()
        self._email = None
        self.password = None
        self.failed_attempts = 0
        self.locked_until = 0
        self.login = False


    def get_user_input(self):
        self._email = input("Enter your email: ")
        self.password = input("Enter your password: ")

    def validate_login_credentials(self):
        try:
            self.database.load_reg_data()
            self.check_user_existence()
            self.check_password_match()
            print("Login successful!")
            self.login = True
            self.failed_attempts = 0

        except ValueError as e:
            self.failed_attempts += 1
            print(f"Error: {e}")
            if self.failed_attempts == self.MAX_LOGIN_ATTEMPTS:
                self.lock_program()



    def lock_program(self):
        self.locked = True
        self.locked_until = time.time() + self.BAN_DURATION_SECONDS
        print(f"You have reached the maximum number of attempts \n The program is locked for {self.BAN_DURATION_SECONDS} seconds.")



    def check_user_existence(self):
        if self._email not in self.database.users:
            raise ValueError("User not found. Please register first.")

    def check_password_match(self):
        if self.database.users.get(self._email) != self.password:
            raise ValueError("Incorrect password. Please try again.")

    def forgotten_password(self):
        self._email = input("Enter your email: ")
        self.database.load_reg_data()
        if self._email in self.database.users:
            new_password = input("Enter new password: ")
            self.database.users[self._email] = new_password
            self.database.store_reg_data()
            print("Password updated successfully!")
        else:
            print("Email not found. Please register first.")

