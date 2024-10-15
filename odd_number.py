"""
author:abhirami b
date:15-15-24\
to print n odd numbers
"""

limit=int(input("Enter your limit:"))
odd_number=1
count=0
while count<limit:
    print(odd_number,"\t",end="")
    count+=1
    odd_number+=2