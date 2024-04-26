from project.database import Database


class User_Profile_Data:
    INTERESTS = ["sport", "movies", "martial arts", "hiking", "reading book", "watching TV", "cinema", "cocking",
                 "party", "politician"]

    def __init__(self):

        self.username = None
        self.age = None
        self.gender = None
        self.degree = None
        self.school = None
        self.interest = []
        self.current_email = None
        self.database = Database()
        self.database.load_user_data()

    def enter_profile_data(self):
        self.username = input("Write your username:")
        self.enter_age()
        self.enter_gender()
        self.choose_interests()
        return self.username, self.age, self.gender, self.interest

    def enter_age(self):
        while True:
            age_input = input("What is your age:")
            try:
                age = int(age_input)
                if age < 18:
                    print("You can't do this because you are under 18")
                else:
                    self.age = age
                    break
            except ValueError:
                print("Invalid input. Please enter a valid age.")

    def enter_gender(self):
        while True:
            genders = ["Male", "Female"]
            gender_input = input("What is your gender (Male or Female):").capitalize()
            if gender_input in genders:
                self.gender = gender_input
                break
            else:
                print("Invalid gender. Please enter 'Male' or 'Female'.")

    def choose_interests(self):
        print("Choose three interests from the list:")
        for i, interest in enumerate(self.INTERESTS, start=1):
            print(f"{i}. {interest}")
        while len(self.interest) < 5:
            try:
                choice = int(input("Enter the number corresponding to your interest: "))
                if 1 <= choice <= len(self.INTERESTS) and self.INTERESTS[choice - 1] not in self.interest:
                    self.interest.append(self.INTERESTS[choice - 1])
                else:
                    print("Invalid choice. Please select a valid interest.")

            except ValueError:
                print("Invalid input. Please enter a number.")
