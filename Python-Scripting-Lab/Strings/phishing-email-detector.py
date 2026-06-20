email = input()

suspicious_words = [
    "urgent",
    "verify",
    "click here",
    "password"
]

for word in suspicious_words:

    if word in email.lower():
        print("Potential Phishing Email")
        break
