# Program to get a certain number from a file
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

total = 0
count = 0

# Loop to strip the text into lines of strings and get the numbers
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    number = line[20:]
    total = total + float(number)
    count += 1

print("Average spam confidence:", str(total/count))
