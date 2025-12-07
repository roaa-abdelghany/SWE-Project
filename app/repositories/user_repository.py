import csv
import os
from models.user import User

USERS_FILE = "users.csv"

class UserRepository:
    @staticmethod
    def add_user(user: User):
        file_exists = os.path.isfile(USERS_FILE)
        with open(USERS_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["fullname", "email", "password"])
            writer.writerow([user.fullname, user.email, user.password])

    @staticmethod
    def find_user_by_email_and_password(email, password):
        if not os.path.isfile(USERS_FILE):
            return None
        with open(USERS_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["email"] == email and row["password"] == password:
                    return User(row["fullname"], row["email"], row["password"])
        return None
