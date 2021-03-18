# 1 penny or cent
# 1 nickel = 5 pennies
# dimes = 10
# quarters = 25
# lonnies = 100
# toonies = 200

a = int(input("Enter the amount which you have to pay in cents"))
t = int(a / 200)
print("",t,"toonies")
a = (a % 200) #remaining cents to be paid
l = int(a/100)
print("",l," loonies")
a = (a % 100)
q = int(a/25)
print("",q,"quarters")
a = a % 25
d = int(a/10)
print("",d,"dimes")
a = a % 10
n = int(a/5)
print("",n,"nickels")
a = a % 5
print("",a,"pennies")
