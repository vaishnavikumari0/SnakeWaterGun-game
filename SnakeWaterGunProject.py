#Snake , Water , Gun : Project
import random
def gameWin(comp,User):
    if comp==User:
        return None
    elif comp =='w':
        if User=='g':
            return False
        if User=='s':
            return True
    elif comp=='s':
        if User=='w':
            return False
        if User=='g':
            return True
    elif comp=='g':
        if User=='w':
            return True
        if User=='s':
            return False

a=print("Computer Turn: Snake(s), Water(w),Gun(g)?")
randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'

User=input("Your Turn: Snake(s),Water(w),Gun(g)?")
a=gameWin(comp,User)

print(f"Computer chose  {comp}")
print(f"You chose  {User}")
if a == None:
    print("The game is a Tie!")
elif a:
    print("You Win!")
else:
    print("you Lose!")