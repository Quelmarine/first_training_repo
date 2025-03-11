small = 15
medium = 20
big = 25
ps = 2
pm = 3
cheese = 1
bill = 0
X = input('Pick any Pizza sizse, "S" "M" "L" :   ')

if X == 'S':
    bill = small
    pep = input(f"Do you need any pepperoni on your Pizza? Y/N :   ") 
    if pep == 'Y':
        bill = bill + ps

    extra_cheese = input(f"Do you want extra cheese? Y/N :   ")
    if extra_cheese == 'Y':
            bill = bill + cheese
    print(f"Thanks for the order, your bill is {bill} $")
else:
    print(f"Thanks for the order, your bill is {bill} $")


if X == 'M':
    bill = medium
    pep = input(f"Do you need any pepperoni on your Pizza? Y/N :   ") 
    if pep == 'Y':
        bill = bill + pm

    extra_cheese = input(f"Do you want extra cheese? Y/N :   ")
    if extra_cheese == 'Y':
            bill = bill + cheese
    print(f"Thanks for the order, your bill is {bill} $")
else:
    print(f"Thanks for the order, your bill is {bill} $")

if X == 'L':
    bill = big
    pep = input(f"Do you need any pepperoni on your Pizza? Y/N :   ") 
    if pep == 'Y':
        bill = bill + pm

    extra_cheese = input(f"Do you want extra cheese? Y/N :   ")
    if extra_cheese == 'Y':
            bill = bill + cheese
    print(f"Thanks for the order, your bill is {bill} $")
else:
    print(f"Thanks for the order, your bill is {bill} $")

#else:
#    print("not written yet!")