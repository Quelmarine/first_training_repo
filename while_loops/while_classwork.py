#for i in range(1,101):
#    print(f"Vahe {i}")


#i = 1

#while i <= 100:
 #   print(f"Vahe {i}")
  #  i += 1


#while i < 20:
 #   print(f"The number is {i} and sqrt= {i**2}")
 #   i += 1


#for i in range(8, 101, 3):
 #   print(f"The number is {i}")
   
numbers = []

for i in range (4):
    number = (int(input(f"Type any number {i+1} :   ")))
    numbers.append(number)

small_pick = min(numbers)
print(small_pick)