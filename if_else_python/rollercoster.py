print("Hey Welcome to Rollercosters!")

height = int(input("how hight are you? :  "))
age = int(input("how old are you? :  ")) 
ticket = 500




if 120 < height < 210:
    print(f"You can go! ")
    if age < 7:
        print(f"not permitted under age 7")
    elif 7 <= age <= 18:
        print(f"Your ride is free")
    elif 45 <= age <= 47:
        print(f"Your ride is with 10% discount!",(ticket-(ticket/10)))
    else:
        print(f"Your price is", ticket, "AMD")

else:
    print(f"you can't go")
