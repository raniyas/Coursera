count = 0
sum = 0.0

while True:
    i = input("Enter a number: ")
    if (i=="done"):
        break
    else:
        try:
            i = float(i)
        except:
            print("Invalid input")
            continue
        count = count +1
        sum = sum +i
        
print(sum, count , sum/count)