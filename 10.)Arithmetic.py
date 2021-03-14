#Arithmetic
#Import math library
import math
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
sum = a+b
diff = b-a
pdt = a*b
qt = a//b
rem = a % b
lg = math.log(a, 10)
pw = pow(a, b)
print('The sum of a and b is ', sum)
print('The difference when b is subtracted from a is ', diff)
print('The product of a and b ', pdt)
print('The quotient when a is divided by b is', qt)
print('The remainder when a is divided by b is', rem)
print('The result of log10a is ', lg)
print('The result of a^b is', pw)