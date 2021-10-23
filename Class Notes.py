# CS 110: PROGRAMMING BUILDING BLOCKS!!!

"""
print("\nHello World!")
print("This is a test \nof making my own code.")
name = input("What is my name? ")
print("DIFFERENCE IN DISPLAYS\n")
print("Separate lines (or, separate print statements)-")
print("My name is :", name)
print("Your name is:", name, "\n")
#This next part, I was curious about if you could use strings
#and variables in the same print statement.
print("You can add string in print by saying print('Words' + 'Words' + variable). " +
 "Everything in print() is a string. You can also use commas.")
print("Input is the same thing; everything in () is a string, but the difference")
print("is that after the string, it expects an input for a variable.")
print("End of test. If you made it this far, congratulations.")
#I was curious about how Python makes comments, so I watched the next video.
print("To comment, use a # symbol. '#This is an example of a comment'")
print("You can use 'ctrl + /' to toggle that line as a comment.")
print('For block comment, use 3 " in a row. Everything between will be a block comment.\n\n')
"""
#This is an example of a comment.
# This is the correct length for any line; They cannot be more than 80 columns.
"""
This is a block comment.
"""
# type() will return what type of thing a thing is. EG.
# age = 23
#  type(age) will return <class 'int'>
# when you use '*' in strings, it repeats it that many times. For example;
# print('UWU ' * 50) will print 'UWU ' 50 times.
# len() will count how long a string is.

# full_name = 'bOB SmiTH'
# print(full_name)
# print(len(full_name)) = 9
# print(full_name.upper()) = BOB SMITH
# print(full_name.lower()) = bob smith
# print(full_name.capitalize()) = Bob smith 
# print(full_name.title()) = Bob Smith
# print(full_name.count(b)) = 1
# print(full_name.lower().count()) = 2

# '//' is basically '/'  in C++; it drops any decimals that come after it.
# '%' is the same as in C++; it just gives you the remainder. ie. 13 % 7 = 6.
# '**' is exponents.
# round(x, y) x is the float you're rounding, y is the decimal point you want to round it to.
# round(1.857142, 3) = 1.857  (can also say {1.857142:.3f}) {variable:.f} (f is fixed point notation.)
# round(1.857142, 2) = 1.85   (can also say {1.857142:.2f})               (Scientific notation uses e instead of f.)
# round(1.857142, 0) = 2.0    (can also say {1.857142:.3f})  {1234567:,} = 1,234,567 (if you use a , you get the commas in there.)
#
# math module
# 
# import math
# print(math.pi)
# print(math.sin(1))
# 
# number1 = int(input('Enter number: '))
# number2 = int(input('Enter number: '))
# number3 = int(input('Enter number: '))
#  
# total = number1 + nubmer2 + nubmer3
# remember; floats like 1/3 have to cut off somewhere, so .1 + .1 + .1 - .3 will NOT be 0.
#  
# convert F to C
# f = float(input('Enter temp:'))
# c = 5 / 9 * (f - 32)        MATH FOLLOWS PEMDAS
# print(f'{f}F = {c}C')
# 
# total_seconds = 12345
# 
# hours-
# hours = (total_seconds / 60) // 60 (don't double inside. You need the decimals for the outer double.)
# hours = total_seconds // 3600
# print(hours)
# 
# minutes-
# total_seconds = total_seconds - (hours * 3600)
# mins = total_seconds // 60
# print(mins)
# 
# seconds-
# total_seconds = total_seconds - (mins * 60)
# secs = total_seconds
# print (secs)
# 
# WHILE LOOPS!!!
# r = 1
# while(r <= 7): #loop
#     print(f'Hi there! {r}')
#     r = r + 1                   #Python uses indentation for loop encapsulation. WHILE loop ends here.
# print(f'The program has run, and you have printed out "Hi there!" {r - 1} times.')
# print(f'the value of r is {r}.')

# x = 0
# for x in range(0,10): # same format as while (x >= 0 && x < 10)
#     print(f'x = {x}')
#     x = x + 1 
#
# 
value = 123456789
print(f'{value:14}*') 
print(f'{value:20}*') 
first_name = "bobby" 
last_name = "SMITH"
full_name = f'{last_name.upper()}, {first_name.capitalize()}'
print('*123456789.123456789.123456789.123456789.*')
print(f"*{full_name:39} *")

#DO-WHILE LOOPS!!!
# while True:
#     boolian = input('Enter "Yes" or "No". ').lower()
#     if(boolian in('yes', 'no')):
#         break           <---------THIS EMULATES A DO-WHILE LOOP!!!!!
#                                     (See below.)
# if boolian == 'yes':
#     print('User typed YES.')
# elif boolian == 'no':
#     print('User typed NO.')
#
# 
#  
# !-----Note; another way of doing it is just setting a value before the while-----!
# loop and setting that as the while loop instead of True.
# eg.;
# magic_number = 4
# guess = -1
# 
# while guess != magic_number:
#   (code. Break is uneccessary now.) 
# 

temp_C = float(input('Enter temp in C; '))
temp_F = (temp_C * (9 / 5)) + 32
print(f'Temp in F is: {temp_F}F')

"""
variable
# print(type(variable)) will return variable type.
# variable.isalpha() will say "are these letters?". You can use this to ensure user input with bool logic.

while True:
    variable = input('Enter a number: ')
    if variable.isnumeric():
        break
    print('Your input has letters. Please try again. ')
    print(f'(Your input was "{variable}")\n')
print(f'Your number is {variable}.')

#do whatever you need with the number from this point on.
"""

#displaying 
number = int(input('Enter number: '))
ones = number % 10
if  number in(11, 12, 13):
    print(f'{number}th')
elif ones == 1:
    print(f'{number}st')
elif ones == 2:
    print(f'{number}nd')
elif ones == 3:
    print(f'{number}rd')
else:
    print(f'{number}th')

#leap year rules!!!
# multiple of:
# 400-> yes
# 100-> no
# 4-> yes 

# Number of days in a month;
# month = int(input('Enter month (1-12): '))
# year = int(input('Enter year: ')) 
# 
# days = 0
# if month in (1, 3, 5, 7, 8, 10, 12):
#   days = 31
# elif month in (4, 6, 9, 11):
#   days = 30
# else:
#   #calculate leap year
#   if year % 400 == 0:
#       days = 29
#   elif year % 100 == 0:
#       days = 28
#   elif year % 4 == 0:
#       days = 29
#   else:
#       days = 28 
# print(f'{month} has {days} days.') 


# TAXES!!! AH-HAH!!!
#
# income = float(input('Enter income for the year: '))
# 
# tax_rate = 0
# 
# if income < 9875:
#   tax_rate = 10
# elif income < 40125:
#   tax_rate = 12
# elif income < 85525:
#   tax_rate = 22
# elif income < 163300:
#   tax_rate = 24
# elif income < 207350:
#   tax_rate = 32
# elif income < 518400:
#   tax_rate = 35
# else:
#   tax_rate = 37

# print(f'Income of {income} is taxed at {tax_rate}%') 

#----------------------------------------
# DEALING WITH IMAGES.
# (Import image) 
# from PIL import Image

# open the image and load into a variable 
# image_original = Image.open("beach.jpg")
# This will try to open a new window to open the image.
# 
#  
# width, height = image_original.size

# print(width, height)


# pixels_original = image_original.load()
# 
#  
#[X, Y] coordinate of pixel you want to grab VVV
# r, g, b = pixels_original[100, 200]

# print(r, g, b) # range 0 to 255

# VVV sets the color of the pixel.  
# pixels_original[100, 200] = (0, 0, 0) #black

#(draws red line across.)
#for i in range(100, 200, 1):
#    (this format is for making pixels.)
#    pixels_original[i, 200] = (255, 0, 0) #red
# 
# for j in range(10): #for 10 lines
#     #draw a red line
#     for i in range(width):
#(this puts them consecutively VVVVV on top of each other.)
#         pixels_original[i, 200 + j] = (255, 0, 0) #Red
# 
#-------FOR LOOPS---------#
# values are assumed to be (0  ,  - ,   1 ) if not included.
# for a_variable in range(start, end, step):
#     do
#     do
#     do
# 
# i = []
# for i in range(0, 10):
#     print(i)
# 
# print()
# for i in range(0, 10, 1):
#     print(i)
# 
# print()
# for i in range(10, 700, 7):
#     print(i)
# 
# for i in range(100):
#     print('Hello World') 

#-----------------LIST STUFF-----------------#
#
# TUPLES #
#  
# Tuples are lists that cannot be changed (read-only). They are defined when declared, and they're
# faster to execute. Insted of square brackets, you use parentheses.
#
# list_numbers = [1, 2, 75, 10] 
# tupple_numbers = (1, 2, 75, 10)
# 
# NEGATIVE NUMBER INDEXING #
# 
# Using a negative number when indexing will loop backwards through the thing.
#
#            0  1  2  3
# numbers = [1, 2, 3, 4]
#           -4 -3 -2 -1
# 
# You can use certain functions with a list. For example, if you have a list called "values", simply putting;
# 
# values.reverse()
# 
# to reverse the order the numbers are in. No need to put "values = values.reverse()". 
#  
#------------------RegEx------------------#
"""
#Code from www.w3schools.com on re.search, adapted to searching for 0-9 and the '.' character.
import re

txt = "a5.0321"
# ^[0-9]*\ says; search for the numbers 0 through 9. \ says "escape", * says "I don't care for how long". 
# .? says "search for this .", and the ? says "this part is optional."
# $ says "this is the end of the search parameters."
x = re.search("^[0-9]*\.?[0-9]*$", txt)

if x:
  print("YES! This works as a postive float!", float(txt))
else:
  print("Invalid as a float or is negative.", txt)
"""
# You can skip an opening line that gives you the format of a .txt document by using
# the count (inherent in every for loop).

# if count != 0:               or              if count > 2: (if there are 2 lines of header)
#     print('Do stuff')
# 
# can also do .readlines()[insertStartingIndexHere:] 
# so if you opened something as files that had 1 line of header;
# 
# files.readlines()[1:]
# 
# 
# 
#-------".JOIN()"-------#
# Takes a list or tuple and joins the values, using a specified character/string to separate.
# SYNTAX
# 1    2  3
# "".join( )
# 1. Whatever's in here will separate the values. " " will make a sentance.
# 2. join function.
# 3. parameters. You can use 'line.split()', for example.
# 
# 
#----------Writing to a file---------#
# 
# BEWARE; THIS WILL OVERRIDE ANY PREVIOUS FILES WITH THAT NAME
#
# (* is bold, it's new stuff. Don't include in actual code.) 
# items = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
# with open('new_file.csv'*, 'w'*) as file:
#   for item in items:
#       # This puts the item on a lline, and then adds \n.  
#       file.write(str(item))
#       file.write('\n')

#       #could also use a formatted string.      
#       file.write(f'{item}\n')    
# 
#----------Reading and saving to another file------------#
# 
# with open('data.txt') as in_file, open('new_datafile.txt', 'w') as out_file:
#   for line in in_file:
#       print(line)
#       out_file.write(line)
# 
#   You could open a file, split and strip the line, use .join(),
#     and then write to the out_file. 
# 
#------------FILTERING DATA----------#
# 
# (year,month,day,temp)
# with open('raw_temps.scv') as raw, open('clean_temps.csv', 'w') as clean:
#   
#   #copy header 
#   line = raw.readline()
#   clean.write(line)
# 
#   #copy data 
#   for line in raw:
#       parts = line.split(',') 
#       print(parts)
#       
#       #make sure line has four parts
#       if len(parts) != 4:
#           print('Error with line: ', line)
#       else:
#           clean.write(line)
# 
#       #test that temp is plausible
#       temp = float(parts[3])
#       if temp < -100 or temp > 140:
#           print('Error with temp: ', line)
#       else:
#           clean.write(line)
# 
# print('END')
# 
#---------READING AND PLOTTING DATA---------#
# (matploylib.py is a mod you'd need to download.)
# import matplotlib.py as plt
# 
# # Data.csv
# 
# usa = []
# usa_years = []
# can = []
# can_years[]
#      
# with open('data.csv')as data:
#   for line in data:
#       parts = line.split(',')
#       if parts[0] == 'USA':
#           usa.append(float(parts[3]))
#           usa_years.append(int(parts[2]))
#       if parts[0] == 'CAN':
#           usa.append(float(parts[3]))
#           usa_years.append(int(parts[2]))
#  
# print(usa) 
# print(usa_years)
#
#          (x, y) 
# plt.plot(usa_years, usa)
# plt.ylabel('Co2 usage')
# plt.show()
#  
#----------Functions and IF statements----------#
#
# #You can make if statements witout elifs or elses. 
# def is_leap_year(year)
#   if year % 400 == 0:
#       return True
#   
#   if year % 100 == 0:
#       return False
# 
#   return year % 4 == 0
#
#----------Simple Shopping Program: turning these to functions.----------#

# #main code 
# items = []
# 
# print("Welcome to the Shopping list program")
# choice = -1
# while choice != 3:
#   print('1) add item') 
#   print('2) display item') 
#   print('3) quit') 
# 
#   choice = int(input('Enter choice (1-3): ))
# 
#   if coice == 1:
#       item = input(Enter item to add to the list: ')
#       items.append(item)
#   elif choice == 2:
#       print("Shopping list")
#       for i in range(len(items)):
#           print(f'{i = 1}: {items[i]}')
#   elif choice == 3:
#       pass:
#   else:
#       print("Invalid choice.")
# print('All Done')

# #(FUNCTIONS THAT COME FROM THIS)
# def welcome_message():
#   print("Welcome to the Shopping List Program!")
# 
# def display_menu():
#   print('1) add item') 
#   print('2) display item')
#   print('3) quit')
# 
# def get_choice():
#   choice = -1
#   while choice != 3
#       choice = int(input('Enter choice (1-3): ))

# def add_item(items)
#   item = input(Enter item to add to the list: ')
#       items.append(item) 

# def display_list():
#   print("Shopping list")
#   for i in range(len(items)):
#       print(f'{i = 1}: {items[i]}')
# 
# ****ALTERNATE CODE FOR PROGRAM****
# items = []
# welcome_message()
# choice = -1 


# CS 111: PROGRAMMING WITH FUNCTIONS
"""
WRITING TO A FILE WITH OPEN()
import math
from datetime import datetime

moment = datetime.now()

with open("volumes.txt", mode="at") as stat_doc:

    line = f'{moment:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}'
    # VVV Debug code
    print(line)
    # VVV 'file' means "append this line to this file"
    print(line, file=stat_doc)
"""
#
# PASS!!! 
# 
#   "In Python, pass is a null statement. The interpreter does not
#   ignore a pass statement, but nothing happens and the statement
#   results into no operation. The pass statement is useful when you
#   don't write the implementation of a function but you want to
#   implement it in the future." -www.educative.io
# 
#   Basically, use "pass" as a placeholder so you don't crash when
#   there's no code there. Do what you do with print(), but with
#   "pass".
# 
# 
# 
# 
# 
# 
# 
#  