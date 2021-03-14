#Tax and Tip
x = float(input('Enter the cost of the meal: '))
tax = float((5/100)*x)
tip = float((18/100)*x)
total = float(x+tip+tax)
print('The tax on the meal was ',tax)
print('The tip on the meal was ',tip)
print('The grand total for the meal is ',total)
