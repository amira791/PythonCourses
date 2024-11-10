# Task 01: String Concatenation
# Objective: Concatenate two strings.
# Instructions:
# Create two variables that store different parts of a sentence, and then concatenate them to form a complete sentence.
a = "aaaaa"
b = "bbbbb"
c = a + b
print(c)

# Task 02: Calculate the Sum of Two Numbers
# Objective: Perform basic arithmetic.
# Instructions:
# Write a program that adds two numbers stored in variables and prints the result.
x = int(input("enter the 1st value "))
y = int(input("enter the 2nd value "))
c = x +y
print(f"the sum of {x} and {y} is {c}")


# Task 03: Temperature Conversion
# Objective: Convert temperature from Celsius to Fahrenheit.
# Instructions:
# Write a program that takes a temperature in Celsius and converts it to Fahrenheit using the formula:
# Fahrenheit = (Celsius * 9/5) + 32.
C = float(input("enter the value of C "))
F = (C * 9/5) + 32
print ("the result is", F)

# Task 04: Even or Odd
# Objective: Check whether a number is even or odd.
# Instructions:
# Ask the user for a number, and determine if it's even or odd.
value = int(input("enter the value: "))


if value % 2 == 0 :
    print("عدد زوجي")
else :
    print("عدد فردي")

# Task 05: Swap Two Variables
# Objective: Swap the values of two variables.
# Instructions:
# Create two variables and swap their values without using a third variable.
ab = 10
cd = 20
ab , cd = cd , ab
print(ab)
print(cd)

# Task 06: Square of a Number
# Objective: Calculate the square of a number.
# Instructions:
# Write a program that calculates the square of a number provided by the user.
number = float(input("enter the value : "))
result = number ** 2
print(result)

# Task 07: Greater Number
# Objective: Find the greater of two numbers.
# Instructions:
# Ask the user to input two numbers and print the larger one.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print(f"The greater number is: {num1}")
elif num2 > num1:
    print(f"The greater number is: {num2}")
else:
    print("Both numbers are equal.")

# Task 08: Temperature Checker
# Objective: Check if the temperature is hot or cold.
# Instructions:
# Ask the user to input a temperature, and print "It's hot" if the temperature is above 35°C, otherwise print "It's cold."

temperature = float(input("Enter the temperature in Celsius: "))

if temperature > 40:
    print("It's hot.")
else:
    print("It's cold.")

# Task 09: Check for eligibility to vote
# Objective: Determine if a person is eligible to vote based on their age and citizenship.
# Instructions:
# The user inputs their age and whether they are a citizen (yes/no).
# احصل على مدخلات المستخدم للعمر والمواطنة
age = int(input("Enter your age: "))
citizen = input("Are you a citizen (yes/no)? ").lower()
  #yes / no     Yes YES yEs -> yes


if age >= 18 and citizen == "yes":  
    print("ok")
else:
    print("no")





# Task 10: Verify login credentials
# Objective: Simulate a login process where the user needs to enter the correct username and password.
# طلب إدخال إسم المستخدم و كلمة المرور
Username = input("Enter your username: ")
Password = input("Enter your password: ")

Correct_Username = "Amel"
Correct_Password = "123"
# تحقق مما إذا كان اسم المستخدم وكلمة المرور المدخلين صحيحين
if Username == Correct_Username and Password == Correct_Password:
    print("Login successful!")
else:
    print("Incorrect username or password. Please try again.")








