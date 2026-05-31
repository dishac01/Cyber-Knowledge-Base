**🕵️ Hide and Seek - TryHackMe Writeup**

Room Overview:
The Hide and Seek room focuses on Linux persistence mechanisms and basic digital forensics investigation. The objective is to locate multiple hidden flag fragments left by an attacker across different persistence locations and combine them to obtain the final flag.

Skills Learned:
Linux persistence techniques
Incident response investigation
Systemd service analysis
Cron job enumeration
SSH key persistence detection
Shell startup script analysis
MOTD persistence hunting
Base64 and Hex decoding


**Task 1: Investigating Systemd Services**
Clue
"I run with the big dogs, booting up alongside the system."

This clue points toward systemd services, which automatically start during system boot.

Enumeration
ls -la /lib/systemd/system/

A suspicious service file was discovered. (cipher.service)

cat /lib/systemd/system/cipher.service

The service contained an encoded string that was decoded to reveal a fragment of the flag.

echo NHRoIHBhcnQgLSBoMW5nXyAK | base64 -d

4th part - h1ng_

What I Learned

Attackers can create malicious systemd services to ensure their malware executes automatically after every reboot.


**Task 2: Investigating Cron Jobs**
Clue
"Time is on my side, always running like clockwork."

This clue refers to cron jobs, which execute commands on a scheduled basis.

Enumeration
sudo crontab -l -u root

A suspicious scheduled task containing encoded data was identified.

After decoding the content, another flag fragment was obtained.

What I Learned

Cron jobs are commonly abused for persistence because they allow attackers to repeatedly execute payloads at specific intervals.


**Task 3: Investigating SSH Key Persistence**
Clue
"A secret handshake gets me in every time."

This clue suggests SSH key authentication.

Enumeration
cat /home/zeroday/.ssh/authorized_keys

A suspicious entry was found within the authorized keys configuration.

Decoding the hidden data revealed another flag fragment.

What I Learned

Attackers frequently add their own SSH public keys to maintain passwordless access to compromised systems.


**Task 4: Investigating Shell Startup Files**
Clue
"Whenever you set the stage, I make my entrance."

This clue points toward shell startup files such as .bashrc.

Enumeration
cat /home/specter/.bashrc

A hidden command containing encoded information was discovered.

After decoding the content, another flag fragment was recovered.

What I Learned

Shell startup files execute automatically whenever a user opens a terminal, making them attractive persistence locations.


**Task 5: Investigating MOTD Scripts**
Clue
"I love welcome messages."

This clue refers to the Message of the Day (MOTD) mechanism.

Enumeration
cat /etc/update-motd.d/00-header

An encoded string was hidden inside the MOTD script.

Decoding the string revealed the final flag fragment.

What I Learned

MOTD scripts execute during login and are often overlooked during security reviews, making them useful for stealthy persistence.


**Key Persistence Locations Identified:**
Persistence Method	Location
Systemd Service	/lib/systemd/system/
Cron Job	Root Crontab
SSH Keys	~/.ssh/authorized_keys
Login Script	~/.bashrc
MOTD Script	/etc/update-motd.d/

**Final Flag**
THM{y0u_g0t_3v3ryth1ng_d0wn}


Conclusion

This room provided practical experience in identifying common Linux persistence mechanisms used by attackers. It reinforced the importance of examining startup services, scheduled tasks, SSH configurations, login scripts, and MOTD files during incident response and threat hunting activities.
