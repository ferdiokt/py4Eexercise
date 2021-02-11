# Program to get a certain word from a file
# Input file name, if not use mbox-short.txt as default
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

# For loops to strip the line and get the lines
for line in fh:
    line = line.rstrip()
    if line == '':
        continue

    # Split the lines (default by whitespace) into words
    wds = line.split()
    if len(wds) < 3:
        continue
    if wds[0] != 'From':
        continue

    count += 1
    print(wds[1])

# Output
print("There were", count, "lines in the file with From as the first word")
