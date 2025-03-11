### FIBONACCI


def fibonacci(n):
    if n <=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


n = int(input(("Enter any Number I'll count ti'll that a Fibonacci sequance:   ")))

for i in range(n):
    print(fibonacci(i))