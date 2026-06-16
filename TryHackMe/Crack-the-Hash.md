# 🔐 Crack The Hash - TryHackMe Writeup

## Task 1 - Level 1

### Hash 1

```text
48bb6e862e54f2a795ffc4e541caed4d
```

I first identified the hash type using an online hash identifier. The hash was recognized as MD5. After searching the hash in an online hash database, the plaintext password was recovered.

### Answer

```text
easy
```

---

### Hash 2

```text
CBFDAC6008F9CAB4083784CBD1874F76618D2A97
```

The hash length indicated SHA1. Using an online cracking database, I located the corresponding plaintext value.

### Answer

```text
password123
```

---

### Hash 3

```text
1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032
```

The hash was identified as SHA256. Searching the hash through available cracking resources revealed the original password.

### Answer

```text
letmein
```

---

### Hash 4

```text
$2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom
```

This was a bcrypt hash, which could not be cracked using simple online databases.

I saved the hash to a file and used Hashcat with the RockYou wordlist.

```bash
hashcat -m 3200 hash.txt rockyou.txt
```

After the attack completed, Hashcat recovered the password.

### Answer

```text
bleh
```

---

### Hash 5

Continue using the same process:

1. Identify hash type.
2. Choose the correct cracking mode.
3. Use CrackStation, Hashes.com, John, or Hashcat depending on the algorithm.
4. Submit the recovered password.

---

## Tools Used

* CrackStation
* Hashes.com
* Hash Identifier
* Hashcat
* RockYou Wordlist

## Conclusion

This room introduced basic password cracking techniques using both online hash databases and offline cracking tools. It highlighted the importance of hash identification before selecting an appropriate cracking method.

