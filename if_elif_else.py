"""
author:abhirami b
date:15-10-24
to determine the largest of two number or if they are equal
"""

number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number:"))

if number1>number2:
    print(number1,"is the largest")
elif number2>number1:
    print(number2,"is the largest")
else:
    print("The numbers are equal")