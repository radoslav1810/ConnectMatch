import re
from project.database import Database


class Registration:
    def __init__(self):
        self._email = None
        self.password = None
        self.register_successfully = False
        self.database = Database()
        self.database.load_reg_data()


    def get_user_input(self):
        self._email = input("Enter your email: ")
        self.password = input("Your password must contain at least one uppercase letter, one digit, and one special character: ")
        return self._email,self.password


    def validate_email(self):
        pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
        match = re.match(pattern, self._email)
        if not match:
            raise ValueError("Invalid email format")

    def validate_password(self):
        pattern = "^(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
        match = re.match(pattern, self.password)
        if not match:
            raise ValueError(
                "Password must contain at least one uppercase letter, one digit, and one special character.")

    def register_user(self):
        try:
            self.get_user_input()
            self.validate_email()
            self.validate_password()
            if self._email not in self.database.users:
                self.database.users[self._email] = self.password
                self.database.store_reg_data()
                print("User saved successfully")
                self.register_successfully = True
            else:
                print("We have already registered a user with this email.")

        except ValueError as e:
            print(f"Error: {e}")













