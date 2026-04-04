#len()-number or elements
from array import array
arr = array ('i',[10,20,30,40,50])
print(len(arr))

#Add element
arr = [10, 20, 30]
arr.append(40)
print(arr)

#Remove element
arr = [10, 20, 30, 40]
arr.remove(20)
print(arr)

#insert at position
arr = array('i',[10,20,40])
arr.insert(2,30)
print(arr)

#remove and return last element
arr = array('i',[10,20,30,40])
x=arr.pop()
print("prmoned:",x)
print(arr)

#find index of element
arr=array('i',[10,20,30,40,])
print(arr.index(30))

#count occurrences
arr=array('i',[10,20,30,20,40])
print(arr.count(20))

#reverse array
arr=array('i',[10,20,30,40])
arr.reverse()
print(arr)