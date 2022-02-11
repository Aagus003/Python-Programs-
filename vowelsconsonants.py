string=str(input("enter the string:"))
v=0
c=0
q=0
w=1
for i in string:
        if(i=="a" or i=="e" or i=="i" or i=="u"):
                v=v+1
        elif(i==" "):
                w=w+1
        elif(i=="?"):
                q=q+1
        else:
                c=c+1
print("vowels =",v)
print("consonants =",c)
print("words =",w)
print("question mark",q)