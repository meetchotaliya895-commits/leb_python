def add (a,b):
    print("a=",a)
    print("b=",b)
    return a+b
result = add(2,5)
print("sum=",result)

def student_info(name,roll,marks):
    print("name:",name)
    print("roll no:",roll)
    print("marks:",marks)
    
student_info("ravi", 105, 85)

def simple_interest(p,r,n):
    si=(p*r*n)/100
    print("simple interst:",si)
simple_interest(10000,2,2)
simple_interest(50000,1.2,3)