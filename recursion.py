'''def a():
    a=input()
for a in range(1,100):
    print(a)'''


def a(n):
    if n > 0:
        a(n-1)
        print(n,end=' ')
a(100)