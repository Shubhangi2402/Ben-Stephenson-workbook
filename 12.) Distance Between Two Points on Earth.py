from math import sin, cos, radians, acos
t1 = radians(float(input('Enter the value of latitude 1: ')))
g1 = radians(float(input('Enter the value of longitude 1: ')))
t2 = radians(float(input('Enter the value of latitude 2: ')))
g2 = radians(float(input('Enter the value of longitude 2: ')))
r = float((sin(t1)*sin(t2)+cos(t1)*cos(t2)*cos(g1-g2)))
s = float(6371.01*acos(r))
print('The distance between the points following the surface of the earth is',"{:.2f}".format(s),"km")