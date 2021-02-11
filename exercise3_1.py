# Program to compute gross pay with condition

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

# Count regular and overtime pay
reg = hrs*rate
ovt = (40*rate)+((hrs-40)*rate*1.5)

# Conditional statement
if hrs > 40:
    print('Pay:', str(ovt))
else:
    print('Pay:', str(reg))
