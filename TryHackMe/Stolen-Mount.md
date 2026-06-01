**🗂️ Stolen Mount — TryHackMe Writeup**

Room Overview:
In this challenge, I was provided with a .pcapng file containing captured network traffic from an incident involving an NFS (Network File System) server.

The objective was to:
Analyze the packet capture
Investigate attacker activity
Reconstruct transferred files
Identify stolen data
Recover the final flag

Skills Learned:
Network traffic analysis
Wireshark investigation
NFS protocol analysis
TCP stream reconstruction
File carving
CyberChef usage
Digital Forensics fundamentals
Understanding the Scenario

The challenge description mentioned:
The attacker targeted an NFS server and a packet capture was recorded during the incident.

This immediately suggested that the investigation should focus on NFS-related traffic.

**What is NFS?**
NFS (Network File System) allows systems to share files across a network as if those files were stored locally.
Attackers often target NFS shares because sensitive files may be exposed through misconfigurations or unauthorized access.

**Step 1: Open the PCAP File**
I loaded the provided .pcapng file into Wireshark for analysis.
The first goal was identifying communication involving the NFS server.

**Step 2: Investigate NFS Traffic**
Since the challenge specifically referenced NFS activity, I began examining the packets associated with NFS communication.
One useful approach was following the TCP stream to reconstruct data exchanged between the attacker and the NFS server.

Why Follow TCP Streams?
Following a TCP stream helps reconstruct the original communication between two systems.

This allows investigators to:
View transferred content
Recover files
Understand attacker actions
Identify exfiltrated data

**Step 3: Extract Transferred Data**
After identifying the relevant stream, I inspected the raw packet contents.
The transferred data appeared to contain file contents that had been accessed from the NFS share.
I exported the relevant stream data and copied the extracted content for further analysis.

**Step 4: Reconstruct Files**
The recovered data contained encoded or fragmented file content.

To reconstruct the files:
Extract the raw data.
Paste it into CyberChef.
Decode or convert the data as needed.
Save the reconstructed output.

This allowed me to recover the files transferred during the attack.

**Step 5: Analyze Recovered Files**

After reconstructing the files, I examined their contents for:
Credentials
Sensitive information
Hidden text
Flag fragments

One of the recovered files contained the information required to obtain the challenge flag.

**Investigation Workflow**
PCAP File
    ↓
Wireshark Analysis
    ↓
Locate NFS Traffic
    ↓
Follow TCP Stream
    ↓
Extract Raw Data
    ↓
Reconstruct Files
    ↓
Analyze Contents
    ↓
Recover Flag

**Key Concepts Learned**:
NFS Enumeration

When investigating packet captures involving NFS:
Identify NFS-related traffic
Track file access requests
Reconstruct transferred files
Examine exported shares
TCP Stream Reconstruction

Following TCP streams helps reveal:
File transfers
Commands
Credentials
Sensitive data
File Carving

File carving involves rebuilding files from raw data recovered during forensic investigations.

This is commonly used in:
Incident response
Network forensics
Malware analysis
Digital investigations
Useful Tools
Tool	Purpose
Wireshark	Packet analysis
CyberChef	Data decoding
Strings	Extract readable text
Hex Editors	Analyze raw data

**Final Flag: THM{n0t_s3cur3_f1l3_sh4r1ng}**

**Conclusion**
This room provided practical experience in network forensics and packet analysis. By examining NFS traffic inside a packet capture, reconstructing transferred files, and analyzing recovered content, I was able to understand how attackers can access and exfiltrate sensitive data through exposed network file shares.
