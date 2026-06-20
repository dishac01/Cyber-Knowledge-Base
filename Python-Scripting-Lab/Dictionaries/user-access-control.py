users = {
    "admin": "Full Access",
    "analyst": "Limited Access",
    "guest": "Read Only"
}

username = input("Enter user: ")

if username in users:
    print(users[username])
else:
    print("User not found")
