###recursion
n1=int(input("enter n1"))
n2=int(input("enter n2"))
def add_numbers(n1,n2):
    if n2==0:
        return n1
    else:
        return add_numbers(n1+1,n2-1)
add_numbers(n1,n2)
print(add_numbers(n1,n2))