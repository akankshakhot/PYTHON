
p = int(input("enter the principal amount:"))
r = float(input("enter the rate of interest:"))
n = float(input("enter the number of years:"))
a = p*(pow((1+r/100), n))
print("the amount is:", a)
ci = a-p
print("the compound interest is:", ci)
