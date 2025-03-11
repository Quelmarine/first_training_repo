
weight_as_int = int(input("Type your weight: "))
height_as_float = float(input("Type your height: "))


bmi = (float(weight_as_int) / float(height_as_float ** 2))
bmi = round(bmi, 1)
#print (bmi)


if bmi < 18.5:
    print(f"Your BMI is {bmi} and you're underweight")
elif 18.5 <= bmi < 25:
    print(f"Your BMI is {bmi} and you have normal weight")
elif 25 <= bmi < 30:
    print(f"Your BMI is {bmi} and you have slightly overweight")
elif 30 <= bmi < 35:
    print(f"Your BMI is {bmi} and you have overweight") 
else:
    print(f"Your BMI is {bmi} and you're clinically obese") 