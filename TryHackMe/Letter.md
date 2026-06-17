# ✉️ Letter - TryHackMe Writeup

# Task 1 - OSINT Time

The room provides a ZIP archive containing:

```text
letter.png
newspaper_clipping.png
note.txt
```

The objective is to determine:

1. The postal code on the damaged envelope.
2. The full name and age of the person mentioned in the note.

---

## Question 1

### What is the postal code of the delivery address on the envelope?

### Initial Observation

Opening `letter.png`, most of the address is damaged and unreadable.

However, there is a sequence of orange bars printed near the bottom of the envelope.

```text
..||||| |.||.| ||..|| |||..| .||.||
```

Since the envelope is French, I investigated whether French postal services use barcode systems for sorting mail.

I discovered that French postal barcodes encode postal code digits using combinations of dots and vertical bars.

### Decoding the Barcode

Using a French postal barcode reference table:

```text
0 = ..||||
1 = .|.|||
2 = .||.||
3 = .|||.|
4 = |..|||
5 = |.|.||
6 = |.||.|
7 = ||..||
8 = ||.|.|
9 = |||..|
```

The barcode translates to:

```text
06792
```

French postal codes are interpreted in reverse order, resulting in:

```text
29760
```

### Answer

```text
29760
```

---

## Question 2

### What is the flag?

### Analyzing the Note

The note is written in French and contains several useful clues.

After translating it, the important details are:

* It refers to Édouard.
* It mentions his great-grandfather.
* It describes him as the youngest member of a rescue team.
* It references a historical maritime incident.

### Investigating the Newspaper Clipping

The newspaper clipping comes from:

```text
L'Ouest-Éclair
```

The article discusses a maritime disaster that occurred in Brittany, France.

Researching the event led to the historic Penmarc'h lifeboat disaster of 1925.

### Connecting the Clues

The envelope was addressed to:

```text
Édouard G.
```

Using the disaster records and crew member information, I searched for the youngest rescuer involved in the incident.

The note specifically mentions:

> "the youngest member of the team"

Cross-referencing the historical records with the surname clue eventually revealed the individual's full identity and age.

### Flag

```text
THM{Yves-Marie_Gourlaouen_15}
```

---

# Tools Used

```text
Google Search
Translation Tools
Historical Archives
French Postal Barcode References
OSINT Research Techniques
```

---

# Key Takeaways

* Small details inside images can provide valuable clues.
* Postal markings and barcodes can reveal hidden information.
* Historical newspaper archives are useful OSINT resources.
* Translating foreign-language content is often necessary during investigations.
* Combining multiple independent clues can lead to a complete solution.

---

# Conclusion

Letter is a beginner-friendly OSINT challenge that focuses on research rather than exploitation. By analyzing a damaged envelope, decoding a French postal barcode, translating a handwritten note, and investigating historical records, it was possible to reconstruct the missing information and solve the challenge.

