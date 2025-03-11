
from re import split
import random


names= (str(input("Give me everybody's names separated by comma (,) :   ")))


print(names)


names_list = names.split(",")

guess = random.randint(0,len(names_list))


print (names_list[guess])