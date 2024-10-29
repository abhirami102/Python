"""
author:abhirami
date:29-10-24
"""
string_input=input("Enter the string:")
vowels="aeiouAEIOU"
vowels_count=0
for char in string_input:
    if char in vowels:
        vowels_count+=1
print(f"The no of vowels in {string_input}={vowels_count}")