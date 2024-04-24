#print(dir(locals()['_builtins_']))

'''try:
    num=10
    deno=0
    result=num/deno
    print(result)
except:
    print('error:denominator cannot be 0')'''

'''try:
    even_numbers=[2,4,6,8]
    print(even_numbers[5])
except ZeroDivisionError:
    print('denominaator cannot be 0')
except IndexError:
    print('indext out of bound')'''

'''try:
    num=int(input('enter a number:'))
    assert num%2==0
except:
    print('not an even number!')
else:
    reciprocal=1/num
    print(reciprocal)'''



file_path="abc.txt"
try:
    with open(file_path,"r")as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")
except exception as e:
    print(f"An error occured:{e}")
finally:
    print("closing the file")
    print("closing the file.")