import random
# Input; add display labels so people can understand what they rolled.

# To avoid crashing, make sure input strings can be converted to ints.
def validate_int(number, prompt, error):
    is_valid = False
    while is_valid == False:
        number = input(prompt)
        if number.isnumeric():
            number = int(number)
            is_valid = True
        else:
            print(error)
    return number

# Get the number of sides for the die you're rolling.
def get_sides():
    sides = -1
    sides_prompt = 'How many sides does the die have? '
    sides_error = "That didn't work. Make sure your number is an int higher than 1."
    # Make sure the sides are a valid int. Also deal with coin
    # situations. 
    while sides <= 1:
        sides = validate_int(sides, sides_prompt, sides_error)
        # add code to make sure it's higher than 1, with a case for
        #  coins.
        if sides <= 1:
            print(sides_error)
        elif sides == 2:
            print("...That's a coin, but I can work with that.")
    return sides

# Get the number of rolls the user is making.
def get_number_of_rolls(is_coin):
    roll_nums = -1
    chance = "roll"
    if is_coin:
        chance = "flip"
    roll_prompt = f'How many {chance}s do you want to make? '
    roll_error = "That didn't work. Make sure you only have numbers."
    # Make sure the number of rolls are a valid int.
    while roll_nums <= 0:
        roll_nums = validate_int(roll_nums, roll_prompt, roll_error)
        if roll_nums == 0:
            print("Dude. You wanted to roll, so roll! ")
    # Erase inside print() when final product is done.
    return roll_nums

# Acutally make the rolls
def get_rolls(sides, number_of_rolls):
    # Make temp storage space for your roll values.
    temp_rolls = []
    for i in range(0, sides):
        temp_rolls.append(0)

    # Generate rolls.
    for i in range(0, number_of_rolls):
        roll = random.randint(1, sides)
        temp_rolls[(roll - 1)] += 1
    return temp_rolls

# Calculate total damage dealt by your rolls.
def calculate_damage(rolls, is_coin):
    damage = 0
    if is_coin:
        damage = rolls[0]
    else:
        count = 1
        for i in rolls:
            damage += i * count
            count += 1
    return damage

# Display all the rolls you made (and calculate total damage)
def display(is_coin, rolls, damage):
    # Vertical display
    # Max number of sides for this should be about 6. 
    if is_coin:
        print(f"Heads: {rolls[0]}\nTails: {rolls[1]}")
    # Vertical display (for 2 < sides <= 8) (change to elif statement)
    else:
        count = 1
        print(f'DISPLAY KEY\nYou rolled: this many times')
        print(f'**************')
        for i in rolls:
            if i != 0:
                print(f"{count}'s: {i}")
            count += 1
    print(f"\nTotal damage: {damage}")
    

# Main driver.
def main():
    rolls = []
    is_coin = False
    sides = get_sides()

    if sides == 2:
        is_coin = True
    num_of_rolls = get_number_of_rolls(is_coin)
    # Debug line
    # print(f"sides = {sides}")
    # Debug line
    # print(f"number of rolls = {num_of_rolls}")
    rolls = get_rolls(sides, num_of_rolls)
    # Debug line
    # print(rolls)
    total_damage = calculate_damage(rolls, is_coin)
    # Debug line
    # print(f"Damage = {total_damage}")
    print()
    display(is_coin, rolls, total_damage)

# Execute program.
if __name__ == "__main__":
    main()