# program to read through the mbox-short.txt and
# figure out the distribution by hour of the day for each of the messages.
# Input file name, default is mbox-short.txt
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# Creating dictionary for the hour
di = dict()

for line in handle:
    line = line.rstrip()
    if line == '':
        continue

    wds = line.split()
    if not line.startswith("From "):
        continue

    # Take the hour value from the list
    hour = wds[5][:2]
    di[hour] = di.get(hour, 0) + 1

# Creating the tuples with key and value inside a list
lst = []
for key, val in di.items():
    newtup = (key, val)
    lst.append(newtup)

# Sorting the list
lst = sorted(lst)
for key, val in lst:
    print(key, val)
