import re

logs = """
INFO Login Success
WARNING Suspicious Activity
ERROR Database Failure
CRITICAL Server Down
"""

pattern = re.compile(
    r'ERROR|WARNING|CRITICAL'
)

matches = pattern.findall(logs)

print(matches)
