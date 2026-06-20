import re

logs = """
Failed login from 192.168.1.10
Connection from 10.10.10.5
"""

pattern = re.compile(
    r'\d+\.\d+\.\d+\.\d+'
)

ips = pattern.findall(logs)

print(ips)
