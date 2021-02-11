# Program to convert score to grade

score = float(input("Enter Score: "))

# Give error output if score is out of range
try:
    if score > 1:
        print('Value is out of range')
    elif score < 0:
        print('Value is out of range')
except:
    print('Must input a number')
    quit()

# Conditional statement for grade
if score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
else:
    print('F')
