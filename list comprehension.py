'''numbers=[10,20,30,40,50]
#list comprehension to create new list
doubled_numbers=[num*2 for num in numbers]
print(doubled_numbers)'''


'''numbers=[10,20,30,40,50]
square_numbers=[]
#for loop to square each elements
for num in numbers:
    square_numbers.append(num*num)
print(square_numbers)'''


'''numbers=[10,20,30,40,50]
#create a new list using list comprehension
square_numbers=[num*num for num in numbers]
print(square_numbers)'''


'''#conditionals in list comprehension
#[expression for item in list if condition == True]
#filtering even numbers from a list
even_numbers=[num for num in range(1,10)if num % 2==0]
print(even_numbers)
#output:[2,4,6,8]'''


'''#finding the vowels in a given string
word="rishika"
vowels="aeiou"
#find vowels in the string"rishika"
result=[char for char in word if char in vowels]
print(result)
#output:['i','i','a']'''





