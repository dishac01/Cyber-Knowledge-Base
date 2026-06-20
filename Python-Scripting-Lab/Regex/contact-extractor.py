import re

text = input("Paste text:\n")

phone_pattern = re.compile(
    r'\d{3}-\d{3}-\d{4}'
)

email_pattern = re.compile(
    r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
)

phones = phone_pattern.findall(text)
emails = email_pattern.findall(text)

print("\n========== REPORT ==========")

print(f"\nPhone Numbers Found: {len(phones)}")

for phone in phones:
    print(phone)

print(f"\nEmail Addresses Found: {len(emails)}")

for email in emails:
    print(email)
