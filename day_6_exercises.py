# Exercise 1: Indentation
# def potatoes():
#     print("Potatoes!")
#     print("Boil 'em, mash 'em, put 'em in a stew")


# Exercise 2: Line Length
# long_string = "This is an exaple of a very long string that goes " \
# "well beyond the character limit."
# print(long_string)

# Exercise 3: Blank Lines
# class Examoles:
#     def first_method(self):
#         pass


#     def second__method(self):
#         pass

# def function_a():
#     print("It's to crampted!")

# def function_b():
#     print("I need some space!")


# Exercise 4: Organizing Imports

#Standard Library Imports
# import os
# import sys

# # Third-party Imports
# import numpy
# import tensorflow

# # Local Imports
# import ga_core
# import 


# Naming Conventions and Whitespaces

# Exercise 1: Naming Conventions
# def calculate_sum(a, b):
#     total_sum = a + b
#     return total_sum


# Exercise 2: Whitespaces
# result = (a + b) * (c - d)
# my_list = [1, 2, 3]
# print(result)


# Documentation and Comments



# Exercise 1: Inline Comments
# def seperate_fruits_and_veggies(items): # Creates a function
#     fruits = [] # Creates an empty list called fruits
#     veggies = [] # creates an empty list called veggies
#     for item in items:
#         name, category =  item # gets name and category of item
#         if category == "fruit": (# adds items with category fruit 
# to fruits list)
#             fruits.append(name)
#         else:
#             veggies.append(name) # adds everything else to veggie list
#     return fruits, veggies # returns both fruits and veggies



# Exercise 2: Docstrings

# def seperate_fruits_and_veggies(items):
#     """Sorts fruits and veggies into separate list.

#     fruits = []: the fruits list.
#     veggie = []: the veggie list.
     
#     for item in item: collects the name and category to sort item into proper 
#     list.

#     Returns: 
#         items in two list sorted by category
#     """ 
#     fruits = [] 
#     veggies = [] 
#     for item in items:
#         name, category =  item 
#         if category == "fruit": 
#             fruits.append(name)
#         else:
#             veggies.append(name) 
#     return fruits, veggies


# Day 6: Error handling

# Exercise 1: LBYL and EAFP
grocery_list = {"bread": 4.50, "cheese": 12.47, "yogurt": 3.99}

# LBYL approach
# if "butter" in grocery_list:
#     print(f"butter: {grocery_list['butter']}units")
# else:
#     print("Error: 'butter' not found in grocery list.")


# EAFP approach
# try:
#     print(f"butter: {grocery_list['butter']} units")
# except KeyError:
#     print("Error: 'butter' not found in grocery list.")


# Day 6: Multi-Line Text, Comments, anf F-Strings

# Exercise 1: Multi-Line Strings

# Using Parenthesis

# about_me = (
#     "I work with Linux and Open Source Software,\n" 
#     "I love riding motorcycles,\n" 
#     "I have a pet wolfe\n"
# )
# print(about_me)

# Using triple quotes
# about_me ="""I work with Linux and Open Source Software
# I love riding  motorcycles
# I have a pet wolfe
# """
# print(about_me)


# Exercise 2: Multi-Line Function Call

# add_bee_hive(
#     beekeeper_name = "Alice",
#     location = "North Field",
#     hive_capacity = 50,
#     bee_species = "Apis mellifera",
#     honey_production_rate = 20.5,
#     hive_health = "Good",
#     queen_present = True,
#     last_inspection = "2024-11-20",
#     notes = "Hive thiving with high activity"
# )


# Exercise 3: Multi-line Data Structures

# stores = {
#     "Store A": 120,
#     "Store B": 340,
#     "Store C": 275,
#     "Store D": 420,
#     "Store E": 310,
#     "Store F": 95,
#     "Store G": 240,
#     "Store H": 180,
#     "Store I": 60,
#     "Store J": 410
# }

# Exercise 4: Module Docstrings
# class bee_keeper_Manager:
# """
#     Name: bee_keeper_manager.py

#     Purpose: To help beekeepers manage thier hives, track honey production,
#     and monitor hive health
#         Features:
#                Add new hives.
#                Update hive health status.
#                Track honey production rates.
#                Generate hive activity reports.
               
#         Author: Buzz McComb
        
#         Version: 2.1
#         """


# Day 6: Type Hints and Annotations

# Exercise 1: Add Type Hints to a Function

# def apples(apple_type: str) -> str:
#     return f"I love, {apple_type} apples!"


# Exersice 2: Use Type Hints for Variables

# title: str = "Python Developer"
# years_experience: int = 10
# is_remote: bool = True    

# Exercise 3: Annotate a Math Function

# def calculate_area(length: float, width: float) -> float:
#     return length * width
