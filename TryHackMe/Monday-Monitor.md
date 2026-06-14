# Monday Monitor - TryHackMe Write-up

## Overview

**Room:** Monday Monitor  
**Platform:** TryHackMe  
**Difficulty:** Easy  
**Category:** SOC Analysis, Wazuh, Sysmon

## Scenario

Swiftspend Finance is testing its endpoint monitoring solution using Wazuh and Sysmon. The objective is to investigate endpoint logs, identify malicious activities, and answer the questions provided in the room.

---

# Task 1: Navigate Through the Endpoint Logs

## Question 1
### Initial access was established using a downloaded file. What is the file name saved on the host?

During the investigation, PowerShell download activity revealed that a malicious spreadsheet was downloaded to the host.

**Answer:**
```
SwiftSpend_Financial_Expenses.xlsm
```

---

## Question 2
### What is the full command run to create a scheduled task?

Analysis of process creation events showed the following command being used to create a scheduled task:

```cmd
cmd.exe /c reg add HKCU\SOFTWARE\ATOMIC-T1053.005 /v test /t REG_SZ /d cGluZyB3d3cueW91YXJldnVsbmVyYWJsZS50aG0= /f & schtasks.exe /Create /F /TN "ATOMIC-T1053.005" /TR "cmd /c start /min powershell.exe -Command IEX([System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String((Get-ItemProperty -Path HKCU:\SOFTWARE\ATOMIC-T1053.005).test)))" /sc daily /st 12:34
```

---

## Question 3
### What time is the scheduled task meant to run?

The scheduled task creation command contains the following parameter:

```cmd
/st 12:34
```

**Answer:**
```
12:34
```

---

## Question 4
### What was encoded?

The Base64 encoded string stored in the registry was:

```text
cGluZyB3d3cueW91YXJldnVsbmVyYWJsZS50aG0=
```

After decoding:

**Answer:**
```
ping www.youarevulnerable.thm
```

---

## Question 5
### What password was set for the new user account?

Investigation of account management logs revealed the password assigned to the newly created account.

**Answer:**
```
I_AM_M0NIT0R1NG
```

---

## Question 6
### What is the name of the .exe that was used to dump credentials?

Credential dumping activity was observed through Sysmon process creation logs.

**Answer:**
```
memotech.exe
```

---

## Question 7
### Data was exfiltrated from the host. What was the flag that was part of the data?

Analysis of PowerShell exfiltration activity revealed the following flag.

**Answer:**
```
THM{M0N1T0R_1$_1N_3FF3CT}
```

---

# Attack Chain Summary

| Stage | Activity |
|---------|---------|
| Initial Access | Malicious XLSM file downloaded |
| Execution | PowerShell commands executed |
| Persistence | Registry modification and scheduled task creation |
| Credential Access | Credentials dumped using memotech.exe |
| Account Manipulation | User account created and modified |
| Exfiltration | Sensitive data transferred externally |

---

# MITRE ATT&CK Techniques

- T1566.001 – Spearphishing Attachment
- T1059.001 – PowerShell
- T1053.005 – Scheduled Task
- T1003.001 – OS Credential Dumping
- T1567.002 – Exfiltration to Cloud Storage

---

# Skills Learned

- Wazuh Log Analysis
- Sysmon Investigation
- Threat Hunting
- PowerShell Analysis
- Persistence Detection
- Credential Dumping Detection
- Data Exfiltration Investigation
- MITRE ATT&CK Mapping

---

## Conclusion

This room provided practical experience investigating endpoint logs using Wazuh and Sysmon. The exercise demonstrated how attackers establish access, maintain persistence, dump credentials, manipulate accounts, and exfiltrate sensitive information while emphasizing the importance of effective endpoint monitoring and threat hunting.
