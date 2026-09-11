"""write a program to store
seven fruits in list 
entered by user"""

fruit=[]
f1  = input("enter fruit name:")
fruit.append(f1)
f2  = input("enter fruit name:")
fruit.append(f2)
f3  = input("enter fruit name:")
fruit.append(f3)
f4  = input("enter fruit name:")
fruit.append(f4)
f5  = input("enter fruit name:")
fruit.append(f5)
f6  = input("enter fruit name:")
fruit.append(f6)
f7  = input("enter fruit name:")
fruit.append(f7)
print(fruit)


"""write a program to accept marks
of student and display them in a
in store manners"""


marks=[]
f1  = int (input("enter marks here:"))
marks.append(f1)
f2  = int (input("enter marks here:"))
marks.append(f2)
f3  = int (input("enter marks here:"))
marks.append(f3)
f4  = int (input("enter marks here:"))
marks.append(f4)
f5  = int (input("enter marks here:"))
marks.append(f5)
f6  = int (input("enter marks here:"))
marks.append(f6)
marks.sort()
print(marks)



"""check that tuple cannot be change
in python"""


a = (63,674,"pankaj")
a[2] = "hafiz"

"""write a program to sum a list 
with 4 number """

l=[4,5,3,6]
print(sum(l))

"""write a program to count the number
of zero in the following tuple"""

a = (4,0,0,0,0,32,7,5,4,)
n= a. count(0)
print(n)