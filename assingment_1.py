print("meet")

a =int(input("enter value :"))
b =int(input("enter value :"))
print("sum is = ",(a+b))

n =int(input("enter value :"))
if n%2 == 0:
    print("even")
else:
    print("odd")
    
year =int(input("enter value:"))
if(year % 4==0 and year % 100 !=0)or (year % 400==0):
    print("leap year")
else:
    print("not a leap year")
    
import math
print("PI=",math.pi)

PI =3.14159
print("constant value =",PI)

n=int(input("enter value:"))
print("square =",n*n)

import math
r =float(input("enter radius:"))
area = math.pi*r*r
print("area=",area)

a=10
b=3.5
c="hello"
print(type(a))
print(type(b))
print(type(c))

import math
print("square rootr of 25=",math.sqrt(25))

a=int(input("enter base:"))
b=int(input("enter power:"))
print("result =",pow(a,b))

n=int(input("enter value:"))
if n>0:
    print("positive")
elif n<0:
    print("negative")
else:
    print("zero")