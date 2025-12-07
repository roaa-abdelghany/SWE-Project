import cgi
from repository import UserRepository
from models import User

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
action = form.getvalue("action")

if action == "register":
    fullname = form.getvalue("fullname")
    email = form.getvalue("email")
    password = form.getvalue("password")
    confirm = form.getvalue("confirm_password")

    if password != confirm:
        print("<h3>Passwords do not match!</h3>")
    else:
        user = User(fullname, email, password)
        UserRepository.add_user(user)
        print("<h3>Account created! <a href='signin.html'>Sign in</a></h3>")

elif action == "login":
    email = form.getvalue("email")
    password = form.getvalue("password")

    user = UserRepository.find_user_by_email_and_password(email, password)
    if user:
        print(f"<h3>Login successful! Welcome, {user.fullname}.</h3>")
    else:
        print("<h3>Invalid email or password!</h3>")
