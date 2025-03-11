print("Hey Welcome to rollercoaster!")

height = int(input("What's your height? :  "))
age = int(input("how old are you? :  ")) 
ticket = 500




if 120 <= height <= 210:

    if age < 7:
        print(f"not permitted under age 7")
    elif 7 <= age <= 18:
        print(f"Your ride is free, if you want a photo then it will be 300 AMD")
    elif 45 <= age <= 47:
        print(f"Your ride is with 10% discount!",(ticket-(ticket/10)), "AMD, if you want a photo then it will be", ((ticket-(ticket/10)+300), "AMD"))
    else:
        print(f"Your price is", ticket, "AMD IF you want a picture overall will be",(ticket+300), "AMD")

else:
    print(f"you can't go")
   