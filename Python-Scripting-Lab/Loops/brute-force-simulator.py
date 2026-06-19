correct_password = "admin123"

wordlist = [
    "password",
    "123456",
    "admin123",
    "welcome"
]

for password in wordlist:
    print(f"Trying {password}")

    if password == correct_password:
        print("Password Found!")
        break
