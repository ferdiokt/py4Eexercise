# Compute the largest and the smallest program

largest = None
smallest = None

# Loop to keep inputting until user enter done
while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        inum = int(num)
    except:
        print('Invalid input')
        continue

    # Conditional statement for the largest and smallest
    if largest is None or inum > largest:
        largest = inum
    if smallest is None or inum < smallest:
        smallest = inum

# Output
print("Maximum is", largest)
print("Minimum is", smallest)
