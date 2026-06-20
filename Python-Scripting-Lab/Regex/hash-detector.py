import re

hash_value = input("Enter hash: ")

if re.fullmatch(r'[a-fA-F0-9]{32}', hash_value):
    print("MD5")

elif re.fullmatch(r'[a-fA-F0-9]{40}', hash_value):
    print("SHA1")

elif re.fullmatch(r'[a-fA-F0-9]{64}', hash_value):
    print("SHA256")

else:
    print("Unknown")
