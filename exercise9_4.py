# Program to read through a file and figure out who has sent the
# greatest number of mail messages
# Input file name, default is mbox-short.txt
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# Creating an empty dictionary
di = dict()

# For loops to fill the dictionary with the email address
for line in handle:
    line = line.rstrip()
    if line == '':
        continue

    wds = line.split()
    if not line.startswith("From "):
        continue

    email = wds[1]
    di[email] = di.get(email, 0) + 1

# Loops to find the address who sent the greatest amount of mail
largest = -1
winner = None
for k, v in di.items():
    if v > largest:
        largest = v
        winner = email

print(winner, largest)
