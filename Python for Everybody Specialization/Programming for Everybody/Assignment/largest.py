
largest = None
for i in range(10):
    if largest is None:
        largest = i
    elif i > largest:
        largest = i

print("largest: ", largest)

smallest = None
for i in range(10):
    if smallest is None:
        smallest = i
    elif i < smallest:
        smallest = i

print("smallest: ", smallest)