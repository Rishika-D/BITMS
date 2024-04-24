'''if(5>10):
    print("yes")
else:
    print("no")'''



'''age1=int(input("enter age1:"))
age2=int(input("enter age2:"))
if(age1>age2):
    age3=age1+age2
    print("my age added",age3)
else:
    age3=age1-age2
    print("my age subtracted",age3)'''



'''email='rishikadudekonda1@gmail.com'
password='12345'
uemail=str(input("enter email id:"))
upassword=str(input("enter password:"))
if(email==uemail and password==upassword):
           print("login success")
else:
           print("login failed")'''
           

'''email:"rishikadudekonda1@gmail.com"
password:"12345"
uemail=str(input("enter the email:"))
upassword=int(input("enter the password:"))
if(email == uemail):
    if(password == upassword):
        print("login successful")
    else:
        print("login failed due to incorrect password")
else:
    printf("login failed due to incorrect email")'''



'''email='rishikadudekonda@gmail.com'
password='12345'
otp='54321'
uemail=str(input("Enter the email"))
upassword=str(input("Enter the password"))
uotp=str(input("enter the otp"))
if(email==uemail and password==upassword):
    print("login successful")
    if(uotp==otp):
        print("transaction successful")
    else:
        print("transaction failed")
else:
    print("login failed")'''



'''num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
if(num1>num2):
    print("num1 is greater")
elif(num1==num2):
    print("num1 and num2 are equal")
else:
    print("num2 is greater")'''
    


'''num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
print("num1 is greater"if(num1>num2)else"num2 is greater")'''



a=50
b=10
c=-15
print('a' if a>b and a>c else 'b' if b>c else 'c')
