largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        try:
           num = int(num)
        except:
            print("Invalid input")
            continue
        if (largest is None):
            largest = num
        elif (num > largest):
            if(largest < smallest):
               smallest = largest
            largest = num
        elif (smallest is None or num < smallest):
            smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)