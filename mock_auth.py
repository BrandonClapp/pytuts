from getpass import getpass
import sys

users = [
    {"name": "brandon", "password": "hello"},
    {"name": "alex", "password": "secret"},
]


def find_user(username):
    user = [user for user in users if user["name"] == username]
    if len(user) == 1:
        return user[0]
    else:
        return None


username = input("username: ")
password = getpass("password: ")

found_user = find_user(username)
is_authenticated = False

if found_user is not None and found_user["password"] == password:
    is_authenticated = True

if is_authenticated:
    print("Authentication success.")
    print(f"Welcome, {found_user['name']}")
else:
    print("Login failed.")
    sys.exit(1)

age = input("Enter your age: ")
found_user["age"] = age

while True:
    command = input("> ")
    if command == "help":
        print("Available commands: age, exit")
    if command == "age":
        print(found_user["age"])
    if command == "exit":
        sys.exit(1)
