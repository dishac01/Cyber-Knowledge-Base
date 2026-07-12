# TryHackMe - OhSINT Write-up

## Objective

Investigate a single image using publicly available information to answer a series of questions. This room introduces the fundamentals of OSINT by demonstrating how seemingly harmless information shared online can reveal a surprising amount about a person.

---

## Skills Learned

- Image metadata analysis
- EXIF data extraction
- Username enumeration
- Social media investigation
- GitHub reconnaissance
- WiGLE wireless lookup
- Source code inspection

---

## Tools Used

- Kali Linux
- ExifTool
- Google Search
- GitHub
- X (Twitter)
- WiGLE
- Browser Developer Tools

---

## Initial Enumeration

The challenge provides a single image file:

```
WindowsXP.jpg
```

Viewing the image reveals no obvious clues, so the next step is to inspect its metadata.

### Extract Metadata

```bash
exiftool WindowsXP.jpg
```

The metadata exposes a username that becomes the starting point for the OSINT investigation. From here, multiple online profiles associated with that username can be discovered.

---

## Username Investigation

A Google search for the discovered username reveals several public profiles including:

- GitHub
- X (Twitter)
- WordPress Blog

Each platform contains different pieces of information that help answer the room's questions.

---

## GitHub Enumeration

The GitHub profile provides useful information such as:

- User location
- Public repositories
- Contact information

One repository contains the user's public email address.

---

## Twitter Investigation

The Twitter profile includes a post containing a wireless BSSID.

Although the BSSID itself is not the answer, it can be used with WiGLE to identify the wireless network information.

---

## WiGLE Lookup

Using the BSSID obtained from Twitter:

1. Open WiGLE.
2. Search using the BSSID.
3. View the matching wireless network.

This reveals the SSID required for one of the questions.

---

## WordPress Investigation

The user's blog provides additional personal information, including:

- Recent travel information
- Hidden webpage content

Inspecting the page source (or selecting hidden text) reveals another hidden value required to complete the room.

---

## Questions Solved

| Question | Information Source |
|----------|--------------------|
| Avatar | Twitter Profile |
| City | GitHub Profile |
| SSID | Twitter + WiGLE |
| Email Address | GitHub Repository |
| Email Source | GitHub |
| Holiday Location | WordPress Blog |
| Password | Hidden WordPress Content |

---

## Key Takeaways

- Metadata often contains valuable intelligence.
- Usernames are commonly reused across multiple platforms.
- Public GitHub repositories can unintentionally expose sensitive information.
- Wireless identifiers such as BSSIDs can reveal physical locations using public databases.
- Hidden webpage content should always be inspected during reconnaissance.

---

## What I Learned

This room demonstrated how multiple pieces of publicly available information can be correlated to build a complete profile of a target. It reinforced the importance of metadata analysis, username enumeration, and careful inspection of publicly accessible resources.
