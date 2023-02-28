#declaring a set
a= {1,2,3,4,1} 
'''print(a)     #in set values are not repeated so 1 will come only one time 
print(type(a))



c = {}  #in this manner we cannot declare a set , it will be a dictorary
print(type(c))'''



#declaring of empty set 
from ctypes import Union


b= set() #empty set is declared in this manner
#print(b)
#print(type(b))
#adding elements in empty set
b.add(1)
b.add(7)
b.add(1)
b.add((1,2,3,4,5,6,7,8,9,0))  #tuple can be added in the set as the elements cannot be modified same as in set elements cannot be modified
#b.add({1,2,3}) #list cannot be added in the set
#b.add(yu = { 6:7}) dictonary cannot be added in set as its value can be modified

print(b) 

#print the len of a set
print(len(b))

#removes an element from the set
b.remove(7)
print(b)

print(b.pop())
print(b)
print(b.union({67,7}))
print(b.intersection({1,2,34}))
print(b.clear())
