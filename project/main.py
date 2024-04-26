

from project.registration import Registration
from project.database import Database
from project.login import Login
from  project.profile import User_Profile_Data
reg = Registration()
log = Login()
user = User_Profile_Data()
database = Database()
current_profile = ""
is_in_profile = False


while True:
    is_registered = input("Do you have already an account? (yes or no): ").lower()
    if is_registered in ["yes", "no"]:
        break

if is_registered == "no":
    while True:
        registration_instance = Registration()
        registration_instance.register_user()
        if registration_instance.register_successfully:
            break

else:
    while True:
        reset_password_choice = input("Do you want to reset your password? (yes/no): ").lower()
        if reset_password_choice in ["yes", "no"]:
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

    if reset_password_choice == "yes":
        log.forgotten_password()

    for attempt in range(Login.MAX_LOGIN_ATTEMPTS):
        if attempt == Login.MAX_LOGIN_ATTEMPTS:
            log.lock_program()
            break
        if log.login:
            enter_in_profile = True
            break
        log.get_user_input()
        current_profile = log._email
        try:
            log.validate_login_credentials()
            is_in_profile = True
        except ValueError as e:
            print(f"{e}")



if is_in_profile:
    while True:
        change_profile_data = input("Do want to change your data: ").lower()
        if change_profile_data in ["yes","no"]:
            break
    if change_profile_data == "yes":
        current_data = user.enter_profile_data()
        database.profile_data[current_profile] = current_data
        database.store_user_data()
    while True:
        want_to_see_data = input("Do you want to see your profile (yes,no): ").lower()
        if want_to_see_data in ["yes", "no"]:
            break

    if want_to_see_data == "yes":
        if current_profile in database.profile_data:
            values_to_print = database.profile_data[current_profile]

            print("Username:", values_to_print[0])
            print("Years:", values_to_print[1])
            print("Gender:", values_to_print[2])
            print("Interests:", ", ".join(map(str, values_to_print[3])))

while True:
    see_best_match = input("Do you want to see your best match (yes/no): ").lower()
    if see_best_match in ["yes", "no"]:
        break
    else:
        print("Please choose between yes or no ")

if see_best_match == "yes":
    if current_profile in database.profile_data:
        user_data = database.profile_data[current_profile]

        interests_for_match = set(user_data[3])
        best_match = None
        max_common_interests = 0

        for other_user, other_data in database.profile_data.items():
            if other_user != current_profile:
                common_interests = set(other_data[3]) & interests_for_match
                if len(common_interests) > max_common_interests:
                    max_common_interests = len(common_interests)
                    best_match = other_data[0]

        if best_match:
            print(f"The best match for {database.profile_data[current_profile][0]} based on interests is {best_match}.")
        else:
            print(f"No suitable match found for {database.profile_data[current_profile][3]}.")
