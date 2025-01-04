# import re

# with open(r"C:\Users\Bartek\Desktop\prg-basics\08-FileHandling\email.txt") as file:
#     content = file.read()

# sender_pattern = r"From: (.+)"
# recipient_pattern = r"To: (.+)"
# email_subject = r"Subject: (.+)"
# email_body = r"\n\n(.+)"

# sender = re.search(sender_pattern, content)
# recipient = re.search(recipient_pattern, content)
# subject = re.search(email_subject, content)
# body = re.search(email_body, content, re.S)

# sender_email = sender.group(1) if sender else "Nie znaleziono nadawcy"
# recipient_email = recipient.group(1) if recipient else "Nie znaleziono odbiorcy"
# email_subject = subject.group(1) if subject else "Nie znaleziono tematu"
# email_body = body.group(1) if body else "Nie znaleziono treści"

# print("Nadawca: ", sender_email)
# print("Odbiorca: ", recipient_email)
# print("Temat: ", email_subject)
# print("Treść: ")
# print(email_body)


import re

with open(r'C:\Users\Bartek\Desktop\prg-basics\08-FileHandling\email.txt', 'r') as file:
    content = file.read()

patterns = {
    "Nadawca": r"From: (.+)",
    "Odbiorca": r"To: (.+)",
    "Temat": r"Subject: (.+)",
    "Treść": r"\n\n(.+)"
}

for label, pattern in patterns.items():
    match=re.search(pattern, content, re.S)
    print(f"{label}: {match.group(1) if match else "Nie znaleziono"}")

