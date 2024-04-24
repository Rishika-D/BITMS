'''email=["abc@gmail.com","def@gmail.com","ijk@gmail.com"]
password=[12345678,12345,98765]
uemail=str(input("Enter email"))
upaw=int(input("Enter password"))
for i in range(0,len(email)):
    if email[i]==uemail:
        if password[i]==upaw:
            print("Already registered")
            break
else:
    print("Register first")
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
    '3': get_balance,
    '4': get_transaction_history
}

while  email[i]==uemail and password[i]==upaw:

    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '5':
        print("Exiting program.")
        break

    if choice in choices:
        if choice == '1' or choice == '2':
            amount = float(input("Enter amount: "))
            choices[choice](account, amount)
        else:
            print(choices[choice](account))
    else:
        print("Invalid choice. Please try again.")'''


'''class mango:
    def __init__(self):
        print("this is what?")
    def rishika(self):
        print("this is whithout para")
    def abc(self,a,b):
        print(a+b,"this is with para")
    def magicalprimes(self,a):
         print("check if it is magicalprime or not")
         n=(input("Enter a mumber"))
         if n%2==0:
             print("not prime")
         else:
             print("prime")
    def neon(self,a):
        print("check neon or not")
man=mango()
man.rishika()
man.abc(10,20.5)
man.magicalprimes(101)
man.neon(7)'''
        


sum = 0
print("Enter the number to check:")
num = int(input())
square = num * num

while (square != 0):
    digit = square % 10
    sum = sum + digit
    square = square // 10

if (num == sum):
    print(str(num)" is a neon number.")
else:
    print(str(num) " is not a neon.")