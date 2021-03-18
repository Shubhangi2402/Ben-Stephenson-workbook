a = float(input('Enter measurement in feet: '))
b = a*12
m = int(b/63360)
b = b % 63360 #remaining in inches
y = int(b/36)
b = b % 36
print("Equivalent distance is","{:.2f}".format(m),'miles',"{:.2f}".format(y),'yards',"{:.2f}".format(b),'inches')


