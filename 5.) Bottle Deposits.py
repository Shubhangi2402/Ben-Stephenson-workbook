#Bottle deposits
x = float(input('Enter the number of containers holding 1 litre or less: '))
y = float(input('Enter the number of containers holding more than 1 litre: '))
refund = float((x*.10)+(y*.25))
print('The refund received will be $',refund)