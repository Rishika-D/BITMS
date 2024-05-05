'''#Task
#Given an integer,n, perform the following conditional actions:

#If n is odd, print Weird
#If n is even and in the inclusive range of 2 to 5, print Not Weird
#If n is even and in the inclusive range of 6 to 20 , print Weird
#If n is even and greater than 20 , print Not Weird

n = int(input().strip())
if n % 2 != 0:
    print("weird")
elif n % 2 == 0 and range(2,5):
    print("Not weird")
elif n % 2  == 0 and range(6,20):
    print("weird")
elif n % 2 ==0 and n>20:
    print("Not weird")'''

'''#Task
#The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

#1.The first line contains the sum of the two numbers.
#2.The second line contains the difference of the two numbers (first - second).
#3.The third line contains the product of the two numbers.
a = int(input("Enter input"))
b = int(input("Enter input"))
print(a+b)
print(a-b)
print(a*b)'''

'''#Task
#The provided code stub reads two integers, a and b , from STDIN.

#Add logic to print two lines. The first line should contain the result of integer division,  a// b.
#The second line should contain the result of float division,  a/b .

#No rounding or formatting is necessary.

a = int(input("enter values"))
b = int(input("enter values"))
print(a//b)
print(a/b)'''

'''# Task
# The provided code stub reads and integer, n , from STDIN. For all non-negative integers i<2 , print i*i.

n = int(input("enter value"))
for i in range(n):
    if i<n:
        print(i*i)'''





