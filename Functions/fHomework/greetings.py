#def greet(name):
 #   print(f"Hello {name}!")

#reet()

#def sum(a,b):
#    print(a+b)

#sum(10,4)

#greet("Bxdo")

#def print_args(*args):
 #   for i in args:
  #      print(f" Hey you choosed: {i}")



#print_args("Valod", "Bxdo", "Chxe", "Chut")

#def print_args(*args):
 #   sum =0
  #  for i in args:
   #     sum = sum + i
    
   # print("Your sum would be ", sum)

#print_args(3,5,2,10,7)


def outterfunc(a):
    def innerfunc():
        print("hello from inside!", a)
    innerfunc()

outterfunc("Vahe")