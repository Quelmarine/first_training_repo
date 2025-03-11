import random
import math
# 1st part
empty_list = []

for i in range(random.randint(1,10)):
    empty_list.append(i)

print(empty_list)
print ("")

#2nd part

empty_list = ["One", "Two", "Tree", "For", "Five", "Six", "Seven",]


for i in range(len(empty_list)):
    empty_list =  sorted(empty_list)


print(empty_list)
print("")

# 3rd part

empty_list = []

for i in range(10):

    x = random.randint(1,10)
    empty_list.append(x)

print(empty_list) 
print("")

empty_list=list(dict.fromkeys(empty_list))
empty_list.sort()
print(empty_list)
