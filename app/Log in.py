#!/usr/bin/env python3
import cgi
import csv
import os

users_file = "users.csv"

form = cgi.FieldStorage()
action = form.getvalue("action")

print("Content-Type: text/html\n")


# Register
if action == "register":
    fullname = form.getvalue("fullname")
    email = form.getvalue("email")
    password = form.getvalue("password")
    confirm = form.getvalue("confirm_password")

    if password != confirm:
        print("<h3>Passwords do not match!</h3>")
        exit()

    file_exists = os.path.isfile(users_file)

    with open(users_file, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["fullname", "email", "password"])

        writer.writerow([fullname, email, password])

    print("<h3>Account created! <a href='signin.html'>Sign in</a></h3>")


# Login

elif action == "login":
    email = form.getvalue("email")
    password = form.getvalue("password")

    found = False
    if os.path.isfile(users_file):
        with open(users_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["email"] == email and row["password"] == password:
                    found = True
                    break

    if found:
        print("<h3>Login successful! Welcome.</h3>")
    else:
        print("<h3>Invalid email or password!</h3>")
