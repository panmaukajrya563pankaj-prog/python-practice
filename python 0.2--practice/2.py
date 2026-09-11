""" write a python program to display
 a user entered name followed by 
good afternoon using input() function"""

name = input("enter your name:")
print(f"good afternoon {name}")


"""writ a program to fill in a template
given below with name and date
"""

letter= """dear name,
            you are selected!
            date"""

print(letter.replace("name","pankaj").replace("date","11-09-2026"))


"""write a program to detect 
double space  in string"""

name = " my  name  is pankaj  kumar"
print(name.find("  "))


"""replace the double space
from problem 3 with single space"""

name = "my  name is  pankaj maurya"
print(name.replace("  "," "))


"""write a program to formatethe
following letter using ascape sequence
character"""

letter= "dear pankaj ,\n\t this python course is nice. \nthanks!"
print(letter)