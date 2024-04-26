import json


class Database:
    def __init__(self):
        self.users = {}
        self.profile_data = {}
    def load_reg_data(self):
        try:
            with open("reg.data", "r") as file:
                self.users = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.users = {}

    def store_reg_data(self):
        with open("reg.data","w") as file:
            json.dump(self.users,file)


    def load_user_data(self):
        try:
            with open("profile_data","r") as file:
                self.profile_data = json.load(file)
        except (FileNotFoundError,json.JSONDecodeError):
            self.profile_data = {}


    def store_user_data(self):
        with open("profile_data","w") as file:
            json.dump(self.profile_data,file)

