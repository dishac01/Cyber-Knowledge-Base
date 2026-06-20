logs = """
INFO Login Success
ERROR Invalid Password
WARNING Suspicious Activity
ERROR Database Failure
"""

errors = 0

for line in logs.split("\n"):

    if "ERROR" in line:
        errors += 1

print(errors)
