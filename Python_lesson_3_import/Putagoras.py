for i in range(1,100):
    for j in range(i,100):
        for n in range(j,100):
            if n**2 == j**2 + i**2:
                print(i, j, n)
                print(" ")


