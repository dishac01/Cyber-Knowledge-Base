# 🔍 Sneaky Patch - TryHackMe Writeup

## Room Information

**Platform:** TryHackMe
**Room:** Sneaky Patch
**Difficulty:** Easy

## Objective

The goal of this challenge is to investigate the system for signs of suspicious kernel activity, identify an unusual module loaded into the Linux kernel, and recover the hidden flag.

---

## Investigation Process

### Step 1: Enumerate Loaded Kernel Modules

I started by listing all currently loaded kernel modules using:

```bash
lsmod
```

This command displays modules that are actively loaded into the Linux kernel.

While reviewing the output, I noticed a module named:

```text
spatch
```

This entry immediately caught my attention because it did not resemble a standard Linux kernel component.

### Why It Looked Suspicious

* Unfamiliar module name
* Not commonly found on Linux systems
* Relatively small module size
* Similar naming pattern to the room title

These indicators suggested it was worth investigating further.

---

## Step 2: Gather Module Information

To obtain additional details about the module, I used:

```bash
modinfo spatch
```

The command returned metadata associated with the module, including:

* Module filename
* Version information
* Description
* Author information (if available)

Most importantly, it revealed the exact location of the module file on disk.

---

## Step 3: Examine the Module File

After locating the kernel object file, I switched to a privileged shell:

```bash
sudo su
```

Next, I inspected the module contents using:

```bash
strings /lib/modules/6.8.0-1016-aws/kernel/drivers/misc/spatch.ko
```

The `strings` utility extracts readable text embedded within binary files, making it useful for basic malware and forensic analysis.

---

## Step 4: Identify Encoded Data

While reviewing the output, I found a long hexadecimal string hidden inside the module:

```text
54484d7b73757033725f736e33346b795f643030727d0a
```

This appeared to be encoded data rather than normal module content.

---

## Step 5: Decode the Value

The extracted string was converted from hexadecimal format into readable text.

After decoding, the hidden flag was revealed.

---

## Flag

```text
THM{sup3r_sn34ky_d00r}
```

---

## Commands Used

```bash
lsmod
modinfo spatch
sudo su
strings /lib/modules/6.8.0-1016-aws/kernel/drivers/misc/spatch.ko
```

---

## Lessons Learned

* Kernel modules should always be reviewed when investigating potentially compromised systems.
* Unknown or custom modules may indicate malicious activity.
* `lsmod` provides a quick overview of loaded kernel components.
* `modinfo` helps identify module locations and metadata.
* `strings` is a useful tool for extracting hidden information from binary files.
* Encoded content such as hexadecimal strings is commonly used to conceal data.

---

## Conclusion

This room demonstrated a simple but effective Linux forensic workflow. By enumerating loaded kernel modules, identifying an unusual component, and inspecting its binary contents, I was able to uncover hidden data and retrieve the challenge flag. The exercise highlighted the importance of investigating unfamiliar kernel modules during incident response and system analysis.
