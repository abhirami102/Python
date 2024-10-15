"""
author:abhirami b
date:15-15-24\
to find the sum of digit of a number
"""
number=int(input("Enter the number:"))
sum=0
while number>0:
    r=number%10
    number=number//10
    sum=sum+r
print("sum of digits of the number is:",sum)
