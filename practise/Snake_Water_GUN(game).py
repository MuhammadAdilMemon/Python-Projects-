# Here is the winning logic
# S=0
# W=1
# G=2
#     S  W  G
#  S  D  W  L
#  W  L  D  W
#  G  W  L  D


import random
matrix=[["DRAW","WIN","LOSE"],["LOSE","DRAW","WIN"],["WIN","LOSE","DRAW"]]
cont=True
snake=0
water=1
gun=2
opp=""
print("WELCOME TO THE SNAKE, WATER AND GUN GAME")
while cont is True:
    choice=input("Enter your choice")
    rand=random.randint(0,2)
    if rand==0:
        opp="Snake"
    elif rand==1:
        opp="water"
    else:
        opp="gun"

    if choice=="snake":
        print(opp)
        print(matrix[snake][rand])
    elif choice=="water":
        print(opp)
        print(matrix[water][rand])
    elif choice=="gun":
        print(opp)
        print(matrix[gun][rand])

    cont=input("do you wanna continue?")
    if cont=="n":
        break