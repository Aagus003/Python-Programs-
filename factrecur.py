def fact(n):
	if(n==1):
		return(1)
	elif(n==0):
		return (0)
	elif(n<0):
		return("There is no factorial for -ve numbers")
	else:
		return(n*fact(n-1))
a=int(input("Enter the number: "))
print(fact(a))