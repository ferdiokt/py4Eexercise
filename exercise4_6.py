# Program to compute gross pay with function

# Create function to compute
def computepay(hrs, rate):
    if hrs > 40:
        pay = (40*rate) + ((hrs-40)*rate*0.5)
        return pay
    else:
        pay = hrs*rate
        return pay


# Input and output
h = float(input("Enter Hours:"))
r = float(input("Enter Rate:"))
p = computepay(h, r)
print("Pay", p)
