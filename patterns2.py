'''name=str(input("Enter name :"))
length=len(name)
for i in range(length):
    for j in range(length):
        if i==j or i+j==length-1:
           print(name[i],end=" ")
        else:
               print(" ",end=" ")
    print()'''




'''name=str(input("enter name:"))
length=len(name)
for i in range(length):
    for j in range(length):
        if i==0 or i==length or i == length-1 or i+j==length-1:
            print(name[j],end=" ")
        else:
            print(" ",end=" ")
    print()
if (((i==0 or i==length) and j>=0 and j<=length)or i+j==length-1 ):
    print(name)'''




'''n=str(input('enter name'))
length=len(n)
for i in range(length):
    for j in range(length*2):
        if i==j or j==length*2-1-i:
            print(n[i],end=' ')
        else:
            print(' ',end=' ')
    print()'''        