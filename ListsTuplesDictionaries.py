# Task 01: List of Squares
# Objective: Create a list of squares of numbers from 1 to 10.
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list =[nb**2 for nb in range(1,11)]
print(list)




# Task 02: Add and Remove from a List
# Objective: Start with an empty list and ask the user to input names. Add each name to the list. Stop when the user types "stop". Then, remove a name of your choice from the list and print the updated list.

names = []    #empty list


while True:
    print("--------------- MENU ----------------")
    print("1 -- Add")
    print("2 -- Remove")
    print("3 -- Stop")
    print("-------------------------------------")


    choice = int(input("enter the code :"))
    if (choice == 1):
        name = input("Enter the name : ")
        names.append(name)
    elif (choice == 2):
        if names:
            name_remove = input("Enter the name to remove : ")
            if name_remove in names:
                names.remove(name_remove)
            else:
                print("this name doesn't exist in the list")
        else:
            print ("The list is empty")
    elif (choice == 3):
        break
    else:
        print ("this code doesn't exist in the menu")


print("The final list", names)







# Task 03: Grocery List
# Objective: Create a dictionary that stores grocery items as keys and their prices as values. Allow the user to add items, remove items, and view the total price of the items.
# {'Apples': 3, 'Bananas': 2, 'Milk': 5}




dict = {
   "Apples": 124,
   "Bananas": 200.23,
    "Milk": 50.55,
}
x = dict.items()
print (x)
while True:
    print("------------menu--------")
    print("1-add item")
    print("2-remove item")
    print("3-total price")
    print("4-Exit")
    print("------------------------")
    choice = int(input("pick your choice : "))
    if choice==1:
        name = input(" Enter the name : ")   #key
        price = float(input("Enter the price : "))  #value
        dict[name] = price
        print(dict)


    elif choice==2:
        #  dict.popitem()
        #  print(x)
        to_remove = input("Enter the item to remove : ")
        if to_remove in dict:
             del dict[to_remove]
        else:
             print("this item does not exist ")
    elif choice ==3:
         total = sum(dict.values())
         print(" The total price is", total)
             
           
    elif choice== 4:
            print("Exit ....")
            break
    else:
        print("Select outside the Menu")


print (" the dic is", dict)






# Task 04: Tuple Operations
# Objective: Create a tuple containing the names of five countries. Write a program that:
# Prints the first and last countries in the tuple.
# Finds the index of a specific country.
Country = ("Algeria", "Moroco", "Palestine", "Tinisia", "Canada")


print("The first country is ", Country[0])
print("The last country is ", Country[4])
print("The last country is ", Country[-1])


country_find = input ("Enter the country to find : ")
if country_find in Country:
    indx = Country.index(country_find)
    print(indx)
else:
    print("This Country does not exist")



# Task 05: Dictionary of Students
# Objective: Create a dictionary where the keys are student names and the values are their grades. Then, write a program that:
# Adds new students and their grades.
# Finds the average grade of the class.
# Allows the user to update a student’s grade.
students = {}


# [] => List
# () => Tuple
# {} => Dictionary


while True:
    print("\n------------MENU------------")
    print(" 1 -- Add grade for a Student")
    print(" 2 -- Update grade for a Student")
    print(" 3 -- Find the average grade of the class")
    print(" 4 -- Exit")
    print("-----------------------------")


    choice = int(input("Pick your choice: "))


    if choice == 1:
        name = input("Enter the name of the student: ").strip()
        grade = float(input("Enter his/her grade: "))
        students[name] = grade
   
    elif choice == 2:
        if students:
            name_update = input("Enter the name of the student to update his/her grade: ").strip()
            if name_update in students:
                new_grade = float(input("Enter the new grade: "))
                students[name_update] = new_grade
                print(f"Grade updated for {name_update}.")
            else:
                print(f"Student '{name_update}' does not exist.")
        else:
            print("No students in the list to update.")


    elif choice == 3:
        if students:
            average = sum(students.values()) / len(students)
            print(f"The average grade of the class is: {average:.2f}")
        else:
            print("No students available to calculate the average.")
   
    elif choice == 4:
        print("Exiting...")
        break
   
    else:
        print("Invalid choice! Please select a valid option from the menu.")


print("\nThe final dictionary of students is:", students)





# Task 06: Reverse a List
# Objective: Create a program that reverses a list of numbers provided by the user.
# Instructions:
# Ask the user to input numbers separated by spaces.
# Store the numbers in a list.
# Reverse the list and print it.
print('\n# Task 06: Reverse a List')


# طلب الأرقام من المستخدم وفصلها وتحويلها إلى قائمة
numbers = input("Enter numbers separated by spaces : ").split()


# mot =  "1 2 3 4"
# a = "1"
# b= "2"
# c = "3"
# d = "4"
# numbers = [1, 2, 3, 4]


# عكس القائمة
reversed_numbers = numbers[::-1]
numbers.reverse()


# طباعة القائمة المعكوسة
print("The inverted list is : ", " ".join(reversed_numbers))
print(numbers)


# Task 07: Check for Duplicate Items in a List
# Objective: Write a program that checks if a list contains any duplicate values.
# Instructions:
# Ask the user to input several numbers.
# Store them in a list.
# Check if the list contains any duplicates and print the result.
#Solution 01

print('\n# Task 07 : Check for Duplicate Items in a List')
# طلب إدخال طول القائمة
Listlength =  int(input('\n*= Enter the length of the list : '))




# ملئ القائمة
List = []


for i in range(0, Listlength):
    Fill = int(input(' Input several numbers : '))
    List.append(Fill)
    i += i    
print('\n Your list : ', List)    


# التحقق من أن القائمة تحتوي على قيم مكررة
i = 0
while i <= len(List):
    Duplicate = List.count(i)
    if Duplicate > 1:
        break
    i += 1


if Duplicate > 1:
    print('\n The list contains duplicated values')
else:
    print('\n The list contains no duplicated values')    
   

#Solution 02: 
numbers = input("Enter numbers separated by spaces : ").split()
# list = [1,2,2,5]     list_set = [1,2,5]
# list2 = [44,55,66]   list2_set = [44,55,66]
# list3 = [2,2,2,2]    list3_set = [2]


if len(numbers) > len(set(numbers)):
    print("There is duplicated items")
else:
    print("No duplicated items")


# Task 08: Sum of Even Numbers in a List
# Objective: Write a program that finds the sum of all even numbers in a list.
# Instructions:
# The user inputs a list of numbers.
# The program finds and prints the sum of the even numbers.


numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
even_sum = sum(num for num in numbers if num % 2 == 0)
print("Sum of even numbers:", even_sum)


# Task 09: Tuple Unpacking
# Objective: Create a tuple with multiple values and unpack the values into separate variables.
# Instructions:
# Create a tuple with several elements (e.g., name, age, city).
# Unpack these values into separate variables and print them.
list = [1,2,3,4,5]
t = tuple(list)
print(t)


# Task 10: Merge Two Dictionaries
# Objective: Write a program that merges two dictionaries into one.
# Instructions:
# Create two dictionaries with key-value pairs.
# Merge the two dictionaries and print the final result.

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict = {**dict1, **dict2}
print("Merged dictionary:", merged_dict)


# Task 11: Find the Intersection of Two Lists
# Objective: Write a program that finds common elements between two lists.
# Instructions:
# Ask the user to input two lists of numbers.
# Find and print the common elements between the two lists.


list1 = list(map(int, input("Enter the first list of numbers: ").split()))
list2 = list(map(int, input("Enter the second list of numbers: ").split()))
intersection = list(set(list1) & set(list2))

print("Common elements:", intersection)


# Task 12: Convert List to Tuple
# Objective: Convert a list of numbers to a tuple.
# Instructions:
# Ask the user to input numbers for a list.
# Convert the list to a tuple and print it.


numbers = list(map(int, input("Enter numbers for the list: ").split()))
numbers_tuple = tuple(numbers)
print("Tuple:", numbers_tuple)


# Task 13: Find the Largest and Smallest Number in a List
# Objective: Write a program that finds and prints the largest and smallest numbers in a list.
# Instructions:
# The user inputs a list of numbers.
# The program finds the largest and smallest values in the list.


numbers = list(map(int, input("Enter a list of numbers: ").split()))

largest = max(numbers)
smallest = min(numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)


# Task 14: Count Occurrences of a Character in a String
# Objective: Write a program that counts how many times a specific character appears in a string.
# Instructions:
# The user inputs a string and a character.
# The program counts the number of occurrences of the character in the string and prints the result.


text = input("Enter a string: ")
char = input("Enter the character to count: ")
count = text.count(char)

print(f"The character '{char}' appears {count} times in the string.")




