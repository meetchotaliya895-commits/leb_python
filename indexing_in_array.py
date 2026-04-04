arr = [10, 20, 30, 40, 50]
print(arr[0])  # first element
print(arr[1])  # second element
print(arr[4])  # fifth element'''

#negative indexing

from array import array
arr = array ('i',[10,20,30,40,50])
print(arr[-1]) 
print(arr[-2])
print(arr[-5])

#modify an element using its index.
arr = [10, 20, 30, 40]
arr[2] = 100
print(arr)

#Loop Through Array Using Index
arr = [5, 10, 15, 20]
i = 0
while i < len(arr):
    print(arr[i])
    i += 1