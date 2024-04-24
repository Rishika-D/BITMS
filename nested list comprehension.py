'''#Nested list comprehension
matrix=[[j for j in range(5)]for i in range(3)]

print(matrix)

integer_input=list(map(int,input("Enter integers seperated by space:").split()))
float_input=list(map(float,input("Enter floats seperated by space:").split()))
string_input=list(input("Enter strings seperated by space:"))

print("Integer input:",integer_input)
print("Float input:",float_input)
print("String input:",string_input)

 
#storing multiple data types in the same variable using a list
data=list(map(int,input("Enter integers seperated by space:").split()))
data.extend(list(map(float,input("Enter floats seperated by space:").split())))
data.extend(input("Enter strings seperated by space:").split())

print("Data:",data)'''