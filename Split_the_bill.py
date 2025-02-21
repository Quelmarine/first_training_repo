print ("Hi, I'll help you to split the bill between the members")
bill = int(input("How much is the bill? "))
bill = float(bill * 1.1)

print('')
print("So the bill + service fee will be,", bill, "$")

tip = int(input("How much tip do you want to give? "))
sum = tip + bill

print ("")
print ("So, all together amount is", sum, "$")

mem = int(input("How many are you? "))

print("")
print ("Deviding", sum, "between", mem, "people, each of you will pay", ( "%0.2f" % (sum/mem,)), "$")
#print( "%0.2f" % (bill,) 