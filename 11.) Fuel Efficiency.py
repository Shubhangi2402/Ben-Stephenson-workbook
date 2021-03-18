#Fuel Efficiency
# 1 Mile(1.6 KM)-> 1 gallon(3.785 lit)    US
# 1 litre per -> kilometer CANADA
value = float(input('Enter the fuel efficiency in american units :'))
fvalue = float(1/(.0042*value))
print('The equivalent fuel efficiency in Canadian units is', "{:.2f}".format(fvalue))