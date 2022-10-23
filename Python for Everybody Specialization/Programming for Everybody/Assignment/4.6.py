def computepay(h, r):
    
    if(h<=40):
        pay = h*r
    else:
        pay = 40*r + ((h-40)*r)*(3/2)
    
    return pay

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate per Hour"))

p = computepay(hrs, rate)

print("Pay", p)