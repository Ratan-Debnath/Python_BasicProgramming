#The elif statement works like an if-else-if ladder statement in C.
"""
    Purpose: how to implement if-else-if also called elif statement?
    Language: Python 3
"""
'''
source code @javapoint
The syntax of the elif statement is given below.

if expression 1:
    # block of statements   

elif expression 2:
    # block of statements   

elif expression 3:
    # block of statements   

else:
    # block of statements  
'''''
#Grading System App
marks = int(input("Enter the marks? "))
if marks > 85 and marks <= 100:
   print("Congrats ! you scored grade A ...")
elif marks > 60 and marks <= 85:
   print("You scored grade B + ...")
elif marks > 40 and marks <= 60:
   print("You scored grade B ...")
elif (marks > 30 and marks <= 40):
   print("You scored grade C ...")
else:
   print("Sorry you are fail ?")