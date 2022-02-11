list=[]
n=int(input("enter the size of the list:"))
i=0
flag=0
for i in range(0,n):
     num=int(input("enter the elements:"))
     list.append(num)
print(list)
a=int(input("enter the element to be searched:"))
for i in range(0,n):
        if(list[i]==a):
                flag=flag+1
                break;
if (flag==0):
        print("Element not found")
else:
        print(a,"found at",i+1)