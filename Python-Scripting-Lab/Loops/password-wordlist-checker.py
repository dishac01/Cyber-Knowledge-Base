common_passwords = [
    "123456",
    "password",
    "qwerty",
    "admin"
]

password = input("Enter password: ")

for weak in common_passwords:
    if password == weak:
        print("Weak Password")
        break
else:
    print("Password Accepted")
