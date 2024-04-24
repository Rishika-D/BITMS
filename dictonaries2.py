'''test_string=input("Enter string:")
l=[]
l=test_string.split()
wordfreq=[l.count(p) for p in l]
print(dict(zip(l,wordfreq)))'''

#1.python program to print sum of negative numbers,even numbers and positive odd numbers in list
#python program to print largest even and largest odd numbers in a list
n=int(input("Enter the number of elements to be in the list:"))
b=[]
for i in range(0,n):
    a=int(input("Element: "))
    b.append(a)
sum1=0
sum2=0
sum3=0
for j in b:
    if(j>0):
        if(j%2==0):
            sum1=sum1+j
        else:
            sum2=sum2+j
    else:
        sum3=sum3+j
print("Sum of all positive even numbers:",sum1)
print("Sum of all positive odd numbers:",sum2)
print("Sum of all negative numbers:",sum3)
    