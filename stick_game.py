''' author:abhirami
stick game'''
def stick_game():
    total_no_of_sticks=16
    person1=0
    person2=0
    list=[1,2,3]
    remaining_sticks=total_no_of_sticks
    while True:
        print('pick a set of sticks[1,2,or,3] ')
        person1=int(input("enter the num"))
        remaining_sticks=remaining_sticks-person1
        print("print a set of sticks[1,2,or3]")
        person2=int(input("enter the num"))
        remaining_sticks= remaining_sticks-person2
    if remaining_sticks>0:
        print("the other person wins")
    elif:
        print

stick_game()