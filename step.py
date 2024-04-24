'''banana=[10,'rishika',250000.75,'z']
print(banana)

for i in banana:
    print(i,end=' ')
print()
pineapple=[10,'rishika',250000.75,'z']
print(pineapple)
print(pineapple==banana)'''



'''apple=[10,5,30]
print(apple)
print(apple[1])
print(apple[-1])
print(apple[-3])
for i in apple:
    print(i,end=' ')
apple[-1]=100
print(apple)
print(apple[-1])
apple[1:4]=(-10,-20,-30)
print(apple)'''



'''college=[10,20,30,40,50]
print(college[1])
print(college[-1])
print(college[1:3])
print(college[1:7])
print(college[:])
print(college[-5:-1])
print(college[3:-1])
print(college[1:])
print(college[:-1])
print(college[0:])
print(college[0:4:2])'''



'''rishika=[]
n=int(input("Enter the list size"))
for i in range(0,n):
    ele=int(input("Enter the elements"))
    rishika.append(ele)
print(rishika)'''



'''rishika=[10,20,30,40,50]
a=[50,60,70,80,90,100]
b=rishika+a
print(b)
print(type(a))
print(type(b))
print(b*2)
print(len(b))
print(max(b))
print(min(b))'''



'''a=[10,20,30,40,50]
sum=0
for i in a:
    sum+=i
print(sum)'''


'''a=[10,25,37,40,57,65]
sum=0
for i in a:
    if i%10==7:
        print(i)'''
#37%10=7


'''a=[10,20,30,40,50,30,50]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)'''



'''apple=[10,20,30,40,50]  #print the common elements in both the lists
mango=[60,70,80,90,100,20]
for i in apple:
    for j in mango:
        if i==j:
            print(i)'''