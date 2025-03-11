import math


def paint_the_wall(X, Y):
    ammount=0
    ammount = (X * Y) / 5
    print("You will need", (math.ceil(ammount)), "to paint")


height  = int(input("enter your wall's Height:  "))
lenght = int(input("enter your wall's Lenght :   "))

paint_the_wall(height, lenght)