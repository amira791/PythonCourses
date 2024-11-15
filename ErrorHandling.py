
# Task 01: Robust Calculator with Error Handling
# Objective: Write a program that acts as a calculator. It should ask the user to input two numbers and the operation (addition, subtraction, multiplication, or division). The program should handle the following exceptions:
# ValueError: When the user inputs something other than a number.
# ZeroDivisionError: When attempting to divide by zero.
# KeyError: When the user inputs an invalid operation.
# Instructions:
# Create a function calculate(a, b, operation) that takes two numbers and the operation and returns the result.
# Use a loop to allow continuous calculation until the user types "exit".
# Sample Output:
# Enter the first number: 10
# Enter the second number: 0
# Enter operation (add/subtract/multiply/divide): divide
# You cannot divide by zero.


def calculate (a,b,operation):
    if operation == "+":
        return a+b
    elif operation =="-":
        return a-b
    elif operation =="*":
        return a*b
    elif operation =="/":
        if b == 0:
            raise ZeroDivisionError("You can't devide by zero")
        return a/b
    else:
        raise KeyError("Invalid operation")






while True:
    try:
        a = float(input("Enter the value of a: "))
        b = float(input("Enter the value of b: "))
        operation = input("Enter the operation [+ - * /] : ")
        calculate(a,b,operation)
    except ZeroDivisionError as e:
        print(e)
    except KeyError as e:
        print(e)
    except ValueError:
        print("Enter valid values for a/b")
    if input("Do you want to stop: Yes/No: ").lower() == "yes":
        break



# Task 02: Safe File Operations
# Objective: Create a file manager program that allows the user to:
# Open a file and read its contents.
# Write to a file.
# Append new content to an existing file.
# Handle possible file-related errors such as:
# FileNotFoundError: If the file doesn’t exist when trying to read.
# PermissionError: If there is no permission to read/write the file.
# IsADirectoryError: If a directory is given instead of a file.
# Instructions:
# Create functions read_file(filename), write_file(filename, content), and append_file(filename, content).
# Handle the mentioned exceptions appropriately.
# Task 02: Safe File Operations
# دالة لقراءة محتويات الملف'


def Read_File(FileName):
    try:
        with open(FileName, 'r') as File:
            Content = File.read()
            print("File Content:\n", Content)
    except FileNotFoundError:
        print(f"Error ! : The file '{FileName}' does not exist.")
    except PermissionError:
        print(f"Error ! : You don't have permission to read the file '{FileName}'.")
    except IsADirectoryError:
        print(f"Error ! : '{FileName}' is a directory, not a file.")




# دالة للكتابة إلى الملف (ستقوم بالكتابة فوق المحتوى الموجود)
def Write_File(FileName, Content):
    try:
        with open(FileName, 'w') as File:
            File.write(Content)
            print(f"Successfully wrote to the file '{FileName}'.")
    except PermissionError:
        print(f"Error ! : You don't have permission to write to the file '{FileName}'.")
    except IsADirectoryError:
        print(f"Error ! : '{FileName}' is a directory, not a file.")


# دالة لإلحاق محتوى جديد بملف موجود
def Append_File(FileName, Content):
    try:
        with open(FileName, 'a') as File:
            File.write(Content)
            print(f"Successfully appended to the file '{FileName}'.")
    except FileNotFoundError:
        print(f"Error ! : The file '{FileName}' does not exist.")
    except PermissionError:
        print(f"Error ! : You don't have permission to append to the file '{FileName}'.")
    except IsADirectoryError:
        print(f"Error ! : '{FileName}' is a directory, not a file.")


# قائمة خيارات لاختبار العمليات
def File_Manager():
    while True:
        print('# Task 02: Safe File Operations '.center(150))
        print("**** File Manager Options : *****")
        print("* 1. Read a file                *")
        print("* 2. Write to a file            *")
        print("* 3. Append to a file           *")
        print("* 4. Exit                       *")
        print("*********************************")
       
        choice = input("Enter your choice (1-4): ")
       
        if choice == '1':
            FileName = input("Enter the filename to read: ")
            Read_File(FileName)
        elif choice == '2':
            FileName = input("Enter the filename to write: ")
            Content = input("Enter the content to write: ")
            Write_File(FileName, Content)
        elif choice == '3':
            FileName = input("Enter the filename to append: ")
            Content = input("Enter the content to append: ")
            Append_File(FileName, Content)
        elif choice == '4':
            print("Exiting the file manager.")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 4.")


File_Manager()


# Task 03: Student Grade Management with Exception Handling
# Objective: Modify the existing student grade dictionary program to:
# Prevent duplicate student names from being added.
# Handle the case where a student to update doesn’t exist.
# Ensure grades are valid (within the range of 0-20).
# Prevent non-numeric grades from being entered.
# Instructions:
# Ensure all input is validated.
# If an invalid grade is input, raise a custom InvalidGradeError.




class DuplicatedStudentException(Exception):
    pass


class InvalidGradeException(Exception):
    pass




students= {}


def add_student(name, grade):
    if name in students:
        raise DuplicatedStudentException("This student already exist")
    if grade<0 or grade>20:
        raise InvalidGradeException("Invalid Grade")
    students[name]= grade


def update_student(name, grade):
    if name is not students:
        raise KeyError("This student does not exist")
    if grade<0 or grade>20:
        raise InvalidGradeException("Invalid Grade")
    students[name]= grade






def calculate_avrg():
    if not students:
        return 0
    return sum(students.values())/len(students)




while True:
    print("******************************")
    print("1-- Add Student ")
    print("2-- Update Grade ")
    print("3-- Calculte Average ")
    print("4-- Exit ")
    print("******************************")


    try:
        choice = int(input("Pick your choice: "))
        if choice == 1:
           name = input("Enter the name of the student: ")
           grade = float(input("Enter the grade of the student: "))
           add_student(name, grade)
        elif choice ==2:
           name = input("Enter the name of the student: ")
           new_grade = float(input("Enter the grade of the student: "))
           update_student(name, new_grade)
        elif choice ==3:
           print(calculate_avrg())
        elif choice == 4:
           print("Exit ....")
           break
        else :
           print("Enter a valid code 1 -- 4")
    except DuplicatedStudentException as e:
        print(e)
    except InvalidGradeException as e:
        print(e)
    except KeyError as e:
        print(e)
   





# Task 04: Bank Account Manager with Custom Exceptions
# Objective: Create a banking application that supports deposits, withdrawals, and balance checks. The program should:
# Raise a custom exception InsufficientFundsError if a withdrawal results in a negative balance.
# Prevent deposits of negative amounts by raising an InvalidDepositError.
# Include a finally block to log all transactions (both successful and failed) to a text file for record-keeping.
# Instructions:
# Implement functions deposit(amount), withdraw(amount), and check_balance().
# Ensure error handling for invalid inputs and edge cases.


global balance
balance = 10000


class InvalidDepositError(Exception):
   pass




class InsufficientFundsError(Exception):
   pass


def deposit(balance):
    try:
          amount= float(input('Enter the amount : '))
          balance = balance + amount
          print ("The new balance is", balance)


          if amount<0:
             raise InvalidDepositError("Invalid deposit value")


    except ValueError :
      print("Enter a valid number ")
    except InvalidDepositError as e:
       print(e)
   




def withdraw(balance):
    try:
          amount= float(input('Enter the amount : '))
           
          if balance < amount:
             raise InsufficientFundsError("InsufficientsFunds")
          balance = balance - amount
          print("The new balance is", balance)
       
    except ValueError:
      print("Enter a valid number")
    except InsufficientFundsError as e:
       print(e)




def check_balance(balance):
    print("The current balance", balance)
   




while True:
    print("******************************")
    print("1-- Deposit ")
    print("2-- WithDraw ")
    print("3-- CheckBalance ")
    print("4-- Exit ")
    print("******************************")


    choice = int(input("Pick your choice: "))
    if choice == 1:
          deposit(balance)
    elif choice ==2:
          withdraw(balance)
    elif choice ==3:
           check_balance(balance)
    elif choice == 4:
           print("Exit ....")
           break
    else :
           print("Enter a valid code 1 -- 4")








# Task 05: Nested Exception Handling in a Shopping Cart System
# Objective: Create a shopping cart system where:
# Users can add items to the cart (store the item name and quantity in a dictionary).
# If the user enters an invalid item or quantity, raise a ValueError.
# Apply a discount using a discount_code. Raise a custom InvalidDiscountError if the code is invalid.
# Add an option to remove items from the cart. If the item doesn’t exist, raise a KeyError.
# Instructions:
# Include try blocks for each operation (adding items, applying a discount, removing items).
# Ensure all exceptions are handled gracefully, and the user is informed of the issue.

class InvalidDiscountError(Exception):
    pass

def add_item_to_cart(cart, item, quantity):
    if not isinstance(item, str) or not isinstance(quantity, int) or quantity <= 0:
        raise ValueError("Invalid item name or quantity.")
    cart[item] = cart.get(item, 0) + quantity

def apply_discount(total, discount_code):
    valid_codes = {"DISCOUNT10": 0.10, "DISCOUNT20": 0.20}
    if discount_code not in valid_codes:
        raise InvalidDiscountError("Invalid discount code.")
    return total * (1 - valid_codes[discount_code])

def remove_item_from_cart(cart, item):
    if item not in cart:
        raise KeyError(f"Item '{item}' not found in the cart.")
    del cart[item]

cart = {}
while True:
    print("\n1 - Add item")
    print("2 - Remove item")
    print("3 - Apply discount")
    print("4 - View cart")
    print("5 - Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        try:
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item_to_cart(cart, item, quantity)
            print(f"{quantity} {item}(s) added to the cart.")
        except ValueError as ve:
            print(ve)

    elif choice == '2':
        try:
            item = input("Enter item name to remove: ")
            remove_item_from_cart(cart, item)
            print(f"{item} removed from the cart.")
        except KeyError as ke:
            print(ke)

    elif choice == '3':
        try:
            discount_code = input("Enter discount code: ")
            total = sum(cart.values()) * 10  # Assuming each item is 10 units for simplicity
            total_with_discount = apply_discount(total, discount_code)
            print(f"Total after discount: {total_with_discount}")
        except InvalidDiscountError as ide:
            print(ide)

    elif choice == '4':
        print("Cart contents:", cart)

    elif choice == '5':
        break

    else:
        print("Invalid choice, try again.")
