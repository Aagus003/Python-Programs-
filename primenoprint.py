a = int(input("Enter the first number:"))
b = int(input("Enter the Second Number:"))
print("Prime Numbers are : ")
for i in range(a ,b+1):
    flag=1
    for j in range(2, (i//2)+1):
        if i % j == 0:
            flag=0
            break
    #else:
    if flag==1 and i!=1:
        print(i)