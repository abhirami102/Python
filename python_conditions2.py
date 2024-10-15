"""
author:abhirami
date:15-10-24
to check whether the given number is positive
"""

number=int(input("Enter a number:"))
if number>0:
    print("The given",number,"is positive")
elif number<0:
    print("The given",number,"is negative")
else:
    print("The given number is zero")