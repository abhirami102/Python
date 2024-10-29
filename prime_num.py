"""
Author:abhirami
Date:29-1024
"""


check_prime=int(input("Enter a number:"))
isprime=True
for i in range (2,check_prime):
    if check_prime%i==0:
        isprime=False
        break
if isprime:
    print(f"The given number {check_prime} is prime")
else:
    print(f"The given number {check_prime} is not a prime")