
# Task 01: Write User Input to a File
# Objective: Write a program that takes user input and writes it to a file.
# Instructions: The user inputs their name and age, and the program saves this data to a file named user_info.txt.
name=input("entre your name:")
age= input("entre your age:")


with open('task1.txt','w')as file:
 file.write("The user name is " + name +  "\n")
 file.write("The user age is " + age )

print("Done")



# Task 02: Read and Display File Content
# Objective: Write a program that reads the content of a file and prints it to the console.
# Instructions: Use the read() function to display the entire content of a file.
#Read PDF content
import PyPDF2


with open('b.pdf','rb')as file:
 content = PyPDF2.PdfReader(file)
 pdf_content = ''
 for page_num in range(len(content.pages)):
    page = content.pages[page_num]
    pdf_content = pdf_content + page.extract_text()
 print(pdf_content)


 



# Task 03: Count Lines in a File
# Objective: Write a program that counts the number of lines in a given text file.
# Instructions: Use a loop to read and count each line from a file.
print('\n#Task 03: Count Lines in a File\n')
    # فتح الملف user_info.txt في وضع القراءة
with open("task.txt", "r") as file:
        # استخدام list لتخزين كافة الأسطر في الملف
    lines = file.readlines()
        # حساب عدد الأسطر
    line_count = len(lines)


        # عرض عدد الأسطر في وحدة التحكم
print(f"Number of lines in the file: {line_count}")
   



# Task 04: Append Data to an Existing File
# Objective: Write a program that appends a new sentence to an existing file without overwriting the previous content.
with open("task.txt", "a") as file:
      file.write("\nThe user2 name is Amel")
      file.write("\n The user2 age is 19")



# Task 05: Create a Simple Log System
# Objective: Simulate a logging system that records the date and time of different events in a text file.
# Instructions: Use the datetime module to capture the current date and time, and log this information in a file.
import datetime


def log_sys(user_action):
    action_time = datetime.datetime.now()
    log_input = f"[{action_time}] ----- [{user_action}]"
    with open("log_file.txt", "a") as file:
        file.write(log_input + "\n")




log_sys("login user")
log_sys("user add a new comment")
log_sys("user is blocked")





# Task 06: Find and Replace in a File
# Objective: Write a program that reads a file, replaces all occurrences of a specific word with another word, and writes the modified content back to the file.
def replace_content (path_file, old_name, new_name):
    with open(path_file, 'r')as file :
        content = file.read()
        print("The old content: ", content)
        new_content = content.replace(old_name, new_name)


    with open(path_file, 'w') as file:
        file.write(new_content)
        print("The new content is: ", new_content)




old_name = input("Enter the old name : ")
new_name = input("Enter the new name : ")
file_path = input("Enter the file name : ")
replace_content(file_path, old_name, new_name)





