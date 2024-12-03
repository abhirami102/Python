###recursion
n1=int(input("enter n1"))
n2=int(input("enter n2"))
def multiplication (n1,n2):
    if n2==1:
        return n1
    else:
        return n1+multiplication(n1,n2-1)
multiplication(n1,n2)
print(multiplication(n1,n2))
