#Its prime number code
"""prime = int(input("Enter Number which you want check: "))
#for i in range(2 , prime):
    #if prime % i == 0:
    #   print("Not prime")
    #    break
#else:
 #  print("prime")"""
#square rooot of array
"""from array import *
vals = array('i', [1, 2, 3, 4, 5, 6])
newarr = array(vals.typecode, (a for a in vals))
sqrarr = array(vals.typecode, (a*a for a in vals))
for x in sqrarr:
 print("The value is new: "+str(x))"""
#two array addition and concationation
"""
from numpy import*
#array thorugh numpy
arr1 = array([1, 2, 3, 4, 5, 6])
arr2 = array([2, 3, 4, 5, 6, 6])
arra3 = arr1+arr2
arra4 = arr1.view()
print(arra3)
print(arra4)
print(concatenate([arr1, arr2]))
print(id(arra4))"""
#sum fucntions appply on array
"""
print(concatenate([arr1, arr2]))
print(min(arra3))
print(sum(arra3))
#use linespace function
linearr = linspace(1,10,10)
print(linearr)"""
#user input Array and user input lenght
"""from array import *
flag = 1
#Empty array decleration
vals = array('i', [])
while flag == 1:
    n = int(input("enter the length  of array"))
    if n > 0:
        flag = 0
        for i in range(n):
    
            x = int(input("Enter next value"))
            vals.append(x)
    else:
        print("The length is cant be negative,please Enter Again")
print(vals)
search = int(input("Enter the value which want to search"))
count = 0
for i in vals:
    if i == search:
        print(count)
        break
    count += 1"""
#Shollow copy and Deep copy
"""
from numpy import*
#At shollow copy,still both arrays depanded on each other
arra1 = array([1, 2, 3, 4, 5])
arra2 = arra1.view()
arra1[0] = 7
print(arra1)
print(arra2)
#Deep copy,both arrays dont depand on each other,now deep copy through that
arra1 = array([1, 2, 3, 4, 5])
arra2 = arra1.copy()
arra1[0] = 7
print(arra1)
print(arra2)"""