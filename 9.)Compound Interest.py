# Compound Interest
r = .04
P = float(input('Enter the amount of money deposited into the account: '))
A1 = float(P*(pow((1+r), 1)))
A2 = float(P*(pow((1+r), 2)))
A3 = float(P*(pow((1+r), 3)))
print('The amount in the savings account after 1,2 and 3 years are', "{:.2f}".format(A1), ',', "{:.2f}".format(A2), ',', "{:.2f}".format(A3), 'respectively')