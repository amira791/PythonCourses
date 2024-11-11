# Create a Class for Books:
# Create a Book class with attributes title, author, and year.
# Add a method to display book details.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")

# Simple Bank Account:
# Create a class BankAccount with methods to deposit, withdraw, and check_balance.
# Ensure withdrawal doesn't allow overdraft.
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance for withdrawal.")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

# Person Inheritance:
# Create a class Person with attributes name and age.
# Create a subclass Student with an additional attribute student_id. Add a method to display all details.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")

# Animal Sounds Polymorphism:
# Create a base class Animal and subclasses Dog and Cat that override the make_sound method.
# Write a function that takes an animal and calls its make_sound method.

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

def animal_sound(animal):
    animal.make_sound()

