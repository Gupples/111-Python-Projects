"""
The time in seconds that a pendulum takes to swing
back and forth once is given by this formula:
             ____
            / n
    t = 2π / ----
          √  9.81

where t is the time in seconds,
π is PI the ratio of the circumference divided by
    the diameter of a circle (use math.pi), and
n is the length of the pendulum in meters.

Write a program that prompts a user to enter the length of a
pendulum in meters and then computes and prints the time in
seconds that it takes for that pendulum to swing back and forth.
"""
import math
import re

is_valid_length = False
while is_valid_length == False:
    value = input("Please enter the length of a pendulum in meters: ")
    is_valid_length = re.search("^[0-9]*\.?[0-9]*$", value)
    if is_valid_length:
        length = float(value)
        time = 2 * math.pi * math.sqrt(length / 9.81)
        print(f"The time it takes for the pendulum to swing is {time:.2f} seconds.")
    else:
        print("That didn't work. Please make sure you don't have any",
        "negative numbers or letters in your entry.\n")
        #VVV Reminder to me; need to do this part because running re.search sets it to something
        #  that's not true OR false, but reacts with "true", hence we don't need
        #  anything for if the search actually works.
        is_valid_length = False