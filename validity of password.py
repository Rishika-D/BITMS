'''#write a python program to accept the string and caluculate the number of digits and letters
str="python 3.2"
digit=letter=0
for ch in str:
    if ch.isdigit():
       digit=digit+1
    elif ch.isalpha():
        letter=letter+1
    else:
        pass
print("Letters:",letter)
print("Digits:",digit)'''



'''#write a python program to check the validity of password validation:
import re
p = input("Input your password")
x=True
if (len(p) < 6 or len(p) > 12):
    pass
elif not re.search("[a-z]", p):
    pass
elif not re.search("[0-9]", p):
    pass
elif not re.search("[A-Z]", p):
    pass
elif not re.search("[$#@]", p):
    pass
elif re.search("\s", p):
    pass
else:
    print("Valid Password")
    x = False
    pass
if x:
    print("Not a Valid Password")'''