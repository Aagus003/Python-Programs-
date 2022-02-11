 def add(a,b):
        c=a+b
        return c
def sub(a,b):
        c=a-b
        return c
def multi(a,b):
        c=a*b
        return c
def divi(a,b): 
        c=a/b
        return c
def exp(a,b):
        c=a**b
        return c
 
a=int(input("enter the 1st number: "))
b=int(input("enter the 2nd number: "))
print("enter the operation")
choice=input("add,substract,multiply,divide,exponent: ")
if (choice=="add"):
        print ("Result = ",add(a,b))
elif (choice=="substract"):
        print ("Result = ",sub(a,b))
elif (choice=="multiply"):
        print ("Result = ",multi(a,b))
elif (choice=="divide"):
        print ("Result = ",divi(a,b))
elif (choice=="exponent"):
        print ("Result = ",exp(a,b))
else:
        print("invalid input")