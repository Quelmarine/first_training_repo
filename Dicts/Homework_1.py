#dict_1 = {"anun" : "bxdo", "azganun" : "Meladze", "tariq" : 21}

dict_1 = {}

dict_1.update({"Vahe": 28, "Bxdo": 30, "Hmbo": 41})

#print(dict_1)

#dict_1.pop("Hmbo")
print("")
dict_1.update({"Vahe": 'Hay'})

for k, v in dict_1.items():
    print(k,v)



print(dict_1["Vahe"])

print(dict_1.get("Valod"))