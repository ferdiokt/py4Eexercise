# Importing regular expression
import re

# File input
# Default input is the assignment file
fname = input('Enter file name:')
if len(fname) < 1:
    fname = 'regex_sum_1157190.txt'
    handle = open(fname)
else:
    handle = open(fname)

# Made a list variable to contain the number
numlist = list()
for line in handle:
    # Removing blank line
    line = line.rstrip()
    # Regex function to find all the number in the line
    stuff = re.findall('[0-9]+', line)
    # To skip any blank line
    if len(stuff) < 1:
        continue
    # To add the number extracted to the list
    for i in stuff:
        num = int(i)
        numlist.append(num)

print('The sum of all extracted number from the file is:', sum(numlist))
