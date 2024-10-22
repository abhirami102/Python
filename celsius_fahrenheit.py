"""
Author:Abhirami B
date:22-10-24
to convert celsius to fahrenheit and fahrenheit top celsius
"""


temperature=int(input("Enter temperature:"))
temp=input("Is this (c)elsius or (F)ahrenheit?:")
if temp=="c":
   f=(9/5*temperature)+32
   print(temperature,"celsius is", f,"fahrenheit")
else:
   c=5/9*(temperature-32)
   print(temperature,"fahrenheit is", c, "celsius")
