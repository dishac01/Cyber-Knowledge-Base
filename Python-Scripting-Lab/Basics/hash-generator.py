import hashlib

text = input("Enter text: ")

hash_value = hashlib.md5(text.encode()).hexdigest()

print(hash_value)
