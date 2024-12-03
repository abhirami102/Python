n=input("enter the phone number:")
def phone_num():
    if len(n)==10 and n[0] in "789":
        print("mobile number is valid")
    else:
        print("mobile number is not valid")
phone_num()
