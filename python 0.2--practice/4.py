"""write a program to create a dictionary of 
hindi words with values as their english
translation . provide user with an option 
to look it up """

words={
    "help":"madad",
    "what":"kya",
    "how":"kaise",
    "why":"kyu",
    "you":"tum"
}
word=input("enter the word you  want meaning of :")
print(words[word])


"""write a program to input eight numbers
from the user and display all the unique
number(once)"""
s=set()
n=input("enter number  :")
s.add (int(n))
n=input("enter number  :")
s.add (int(n))
n=input("enter number  :")
s.add (int(n))
n=input("enter number  :")
s.add (int(n))
n=input("enter number  :")
s.add (int(n))
n=input("enter number  :")
s.add (int(n))
n=input("enter number  :")
s.add (int(n))
n=input("enter number  :")
s.add (int(n))
print(s)


"""can we have a set with 18 (int)and
'18 (str)as a value in it ?'"""

s= set()
s.add(18)
s.add("18")
print(s)


"""what will be the lenght of 
following set s:"""

s = set ()
s.add(20)
s. add (20.0)
s.add('20')

"""create empty dictionary allow 4
friends to enter their favorite
lamguage as value and use key as their 
names; what will be happend to the program in
probleb 6?"""

d= {}
name= input ("enter friend name:")
lang=input("enter language name :")
d.update({name:lang})

name= input ("enter friend name:")
lang=input("enter language name :")
d.update({name:lang})

name= input ("enter friend name:")
lang=input("enter language name :")
d.update({name:lang})

name= input ("enter friend name:")
lang=input("enter language name :")
d.update({name:lang})

print (d)


