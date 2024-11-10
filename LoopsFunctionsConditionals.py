#Practice Tasks (For Loops and While Loops)
# Task 01: Print Numbers
# Objective: Print numbers from 1 to 10 using both for and while loops.
for i in range(1, 11):
    print(i)
i = 1
while i < 11:  #<=10
    print(i)
    i += 1    #i = i +1

# Task 02: Calculate the Sum of Numbers
# Objective: Write a program that calculates the sum of numbers from 1 to 100 using a loop.

total_sum = 0
for num in range(1, 101):
    total_sum += num
print("The sum of numbers from 1 to 100 is:", total_sum)

# Task 03: Multiplication Table
# Objective: Write a program that prints the multiplication table for a given number.
nb = int(input("enter the number: "))
for i in range (11):
    result = nb * i
    print(result)

# Task 04: Count Down Timer
# Objective: Write a program that prints a countdown from 10 to 1 using a while loop.
print('# Task 04 : Count Down Timer')
CountDown = 10
while CountDown >= 1:
    print(CountDown)
    CountDown -= 1

# Task 05: Guess the Number
# Objective: Create a number guessing game where the user has to guess a number between 1 and 10 using a while loop.
import random
cpt = 1
num = int(input("Guess the number: "))  # i gave him the number
rand = random.randint(1,10)    # generate the random value
while num != rand and cpt < 3 :
    if num < rand :
        print ("Too Low")
        cpt += 1
    else :
        print("Too high")
        cpt += 1
    num = int(input("Guess the number: "))


if (num == rand):
    print("You Wiiin  !")
else:
    print ("You Lost !")




# Practice Tasks (Functions and Conditionals)
# Task 01: Find the Maximum of Three Numbers
# Objective: Write a function that takes three numbers as input and returns the largest.
a=int(input("enter value: "))
b=int(input("enter value: "))
c=int(input("enter value: "))




def maxi (a, b, c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b  
    else:
        return c

print(maxi(a,b,c))




# Task 02: Calculate the Area of a Circle
# Objective: Write a function that calculates the area of a circle given its radius.
import math
def AreaCircle(r):
 result = math.pi*r**2
 return result
radius = float(input("Enter the value of the Radius: "))
A=AreaCircle(radius)
print(f"the Area is : {A:.2f}")

# Task 03: Create a Simple Calculator
# Objective: Write functions for addition, subtraction, multiplication, and division. Ask the user to choose an operation.

print('\n  # Task 03: Create a Simple Calculator')
# دالة الجمع
def Addition(a, b):
    Add = a + b
    return Add
# دالة الطرح
def Subtraction(a, b):
    Sub = a - b
    return Sub
# دالة الضرب
def Multiplication(a, b):
    Multp = a * b
    return Multp
# دالة القسمة
def Division(a, b):
    if b == 0:
        Div =  "You cant devide by 0"
    else:
        Div = a / b
    return Div
# برمجة الحاسبة


while True:   #  لتكرار العمل عدة مرات
    # طلب إدخال الأرقام من المستخدم
    Num1 = float(input('Enter the first Number : '))
    Num2 = float(input('Enter the second Number : '))
    # قائمة اختيارات العمليات الحسابية
    print("---------------------MENU-------------------------")
    print('1 - Addition.')
    print('2 - Subtraction.')
    print('3 - Multiplication.')
    print('4 - Division.')
    print('5 - Exit')
    print("--------------------------------------------------")
    Choice = int(input('* Enter the transaction type number from the menu above : '))
    if Choice == 1:
        print(Addition(Num1, Num2))
    elif Choice == 2:
        print(Subtraction(Num1, Num2))
    elif Choice == 3:
        print(Multiplication(Num1, Num2))
    elif Choice == 4:    
        print(Division(Num1, Num2))
    elif Choice == 5:
        print("Exit ....")
        break
    else:
        print('Select outside the list, try again ..')    

# Task 04: Count Vowels in a String
# Objective: Write a function that counts the number of vowels in a string.

def vowels_detecter (word):
    v= "aeiuyoAEIUYO"
    cpt = 0
    for i in word:
        if i in v:
            cpt +=1
    return cpt
word = input("Enter the word : ")
print (f" the number of vowels in this word is {vowels_detecter(word)}")




#----------------------
# Rayhane
# i = R => if R in v(aeiuyoAEIUYO) | yes => cpt = cpt + 1 | no cpt
# i = a => if a in v(aeiuyoAEIUYO) | yes => cpt = cpt + 1 | no cpt

# Task 05: Prime Number Checker
# Objective: Write a function that checks whether a given number is prime.
def prime(number):
    if number <= 1:
        return " Not Prime"
    else:
        for i in range(2, int(number**0.5)+1):
            if number % i == 0:
                return "Not Prime"
        return " Yes Prime"




number = int(input("Enter the number : "))
print(prime(number))

# Project Idea: Simple Banking System Simulation
# Write functions to simulate a simple banking system:
# deposit(balance, amount): Adds the deposit amount to the balance.
# withdraw(balance, amount): Subtracts the withdrawal amount from the balance.
# check_balance(balance): Displays the current balance.
# Ask the user to input transactions, and call the corresponding functions.


balance = 100

def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if balance > amount:
        return balance - amount
    else:
        return "You can't do this operation. Check your balance."

def check_balance(balance):
    print("The current balance:", balance)

while True:
    print("---------------------MENU-------------------------")
    print('1 - Deposit')
    print('2 - Withdraw')
    print('3 - Check Balance')
    print('4 - Exit')
    print("--------------------------------------------------")

    choice = int(input('* Enter the transaction type number from the menu above: '))
    
    if choice == 1:
        amount = float(input('Enter the amount to deposit: '))
        balance = deposit(balance, amount)
        check_balance(balance)

    elif choice == 2:
        amount = float(input('Enter the amount to withdraw: '))
        result = withdraw(balance, amount)
        if isinstance(result, str):
            print(result)
        else:
            balance = result
            check_balance(balance)

    elif choice == 3:
        check_balance(balance)

    elif choice == 4:
        print("Exit ....")
        break

    else:
        print('Invalid selection, try again.')
