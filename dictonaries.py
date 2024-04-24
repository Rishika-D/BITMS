'''#the data is stored as key-value pairs using a python dictionary
emp={"name":"rishika","age":30,"salary":250000,"dob":"2004-05-07"}
print("Employee data...")
print(emp)

#creating a dictonary
#with each item as a pair
Dict=dict({1: 'Mango', 2: 'Apple', 3:'Banana'})
print("\ncreate dictonary by using dict():")
print(Dict)

#creating a dictonary
#with each item as a pair
Dict=dict([(4, 'rishika'),(2,'moksha')])#tuple in dictionary
print(Dict)'''

def withdraw(account, amount):
    if amount > account['balance']:
        print("Insufficient funds!")
    else:
        account['balance'] -= amount
        account['transactions'].append(f"Withdrawal: ${amount}")
        print(f"Withdrawal successful. Remaining balance: ${account['balance']}")

def deposit(account, amount):
    account['balance'] += amount
    account['transactions'].append(f"Deposit: ${amount}")
    print(f"Deposit successful. Remaining balance: ${account['balance']}")

def get_balance(account):
    return account['balance']

def get_transaction_history(account):
    return account['transactions']

# Create an account dictionary
account = {
    'balance': 1000,
    'transactions': []
}

# Dictionary to map user choices to functions
choices = {
    '1': deposit,
    '2': withdraw,

'''#working of functions as dictionaries without params
def rishika():
    return"This is my bank account"
#initialize dictionary
#check for function name as key
test_dict={"fname":rishika,"age":50,"address":"salem"}

#printing original directory
print("The original directory is:"+str(test_dict))
      
#calling function using braces
res=test_dict["fname"]()
      
#printing result
print("The required call result:"+str(res))'''


#working of functions as dictionaries without params
def rishika(a,b):
    print("my result bank balance=",a+b)
#initialize dictionary
#check for function name as key
test_dict={"fname":rishika,"age":50,"address":"salem"}

#printing original directory
print("The original directory is:"+str(test_dict))
      
#calling function using braces
test_dict["fname"](10,20)


