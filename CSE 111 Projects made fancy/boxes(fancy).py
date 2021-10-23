# This is fancy because I added a function to ensure there would be no crashing; namely, making sure
# each input is converted to an integer after validating that it can be.  
import math

def validate(number, prompt):
    is_valid = False
    while is_valid == False:
        number = input(prompt)
        if number.isnumeric():
            number = int(number)
            is_valid = True
        else:
            print("That didn't work. Check input for symbols, letters,",
                "or negative signs.")
    return number


prompt1 = "Enter the number of items: "
prompt2 = "Enter the number of items per box: "
items = 'a'
load = 'a'
items = validate(items, prompt1)
load = validate(load, prompt2)
# '.ceil' takes a number and rounds up to nearest int. '.floor' rounds down.
boxes = 0
# Ensure we don't divide by 0 here.
while load <= 0:
    print(f'Box capacity has to be greater than 0.')
    load = validate(load, prompt2)
boxes = math.ceil(items/load)

print(f'For {items} items, packing {load} in each box, you will',
    f'need {boxes} boxes.')