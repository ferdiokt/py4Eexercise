# Program to get a number from a text
text = "X-DSPAM-Confidence:    0.8475"

# Find the position of '0' character
pos = text.find("0")
# Get the number starting from the posisiton
num = text[pos:]
f_num = float(num)

print(f_num)
