# FOR Loop  
for i in range(6):
    print(i)
    
# Example 1 : Print ODD Number in (0 to 20) using FOR Loop.
print("ODD Number is : ")
for i in range(20):
    if i % 2 != 0:
        print(i)
               
# Example 2 : Print EVEN Number in (0 to 20) using FOR Loop.
print("EVEN Number is : ")
for i in range(20):
    if i % 2 == 0:
        print(i)
        
# Example 3 : Print Table of 5.
print("Table of 5 is : ")
for i in range(1, 11):
    print("5 x", i,"=", i*5)
    
# Example 4 : Print List Element number using for loop.
number = [11, 22, 33, 44, 55, 66]
for n in number:
    print("n =", n)

# Example 5 : Print name letter by letter.
name = "Atmiya"   
for i in name:
    print(i)

# Example 6 : Sum of Number from 1 to 5.
total = 0
for i in range(6):
    total += i
print("total =", total)

# Example 7 : For loop using break and continue statement.
print("Using break statement")  
for i in range(5):
    if i == 3:
        break  
    print(i)

print("using continue statement ")
for i in range(5):
    if i == 3:
        continue
    print(i)
