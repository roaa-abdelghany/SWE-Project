import csv
import os

ADMIN_FILE = "data/Admin_login.csv"

class AdminRepository:
    @staticmethod
    def find_admin(email, password):
        if not os.path.exists(ADMIN_FILE):
            os.makedirs("data", exist_ok=True)
            with open(ADMIN_FILE, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["email", "password"])
                writer.writerow(["admin@cosmetics.com", "admin123"])
            return None
        
        with open(ADMIN_FILE, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["email"].strip() == email.strip() and row["password"].strip() == password.strip():
                    return row
        return None