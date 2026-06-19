import hashlib

filename = input("Enter file name: ")

try:
    with open(filename,"rb") as f:
        data = f.read()

    hash_value = hashlib.sha256(data).hexdigest()

    print(hash_value)

except Exception as err:
    print(err)
