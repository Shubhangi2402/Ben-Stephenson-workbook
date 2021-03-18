a = float(input('Enter your height in feet: '))
b = float(input('Enter your height in inches: '))
f = float(a*30.48 + b*2.54)
print("Your height is","{:.2f}".format(f),"cm")