import random
from os.path import exists

# Get the name and gender from the user. Returns a tuple with the order
# of [name, gender] 
def get_info():
    name = input("What is your character's name? ")
    gender = "Unassigned"
    valid_gender = False
    while valid_gender == False:
        temp_gender = input("What gender is your character? (M/F) ")
        if temp_gender.lower() in ('m', 'f'):
            if temp_gender.lower() == 'm':
                gender = "Male"
                valid_gender = True
            else:
                gender = "Female"
                valid_gender = True
        else:
            print(f"Sorry, {temp_gender} wasn't an option. Type 'M' for male",
            f"or 'F' for female.")
        print()
    return name, gender

# Roll a 20-sided die.
def roll_dice():
    roll = random.randint(1, 20)
    return roll

# Ensures a set of rolls meet the minimum required total value for
# stats (70). Returns True if it does, False if it doesn't.
def validate_stat_rolls(dice_rolls):
    total = 0
    for roll in dice_rolls:
        total += roll
    if total >= 70:
        # return total for pytest purposes
        return True, total
    else:
        # return total for pytest purposes
        return False, total

# Generate stats for the 6 traits (In order: Strength (Str), Dexterity (Dex),
# Constitution (Con), Intelligence (Int), Wisdom (Wis), and Charisma (Cha)).
# For extra randomness, it shuffles the list before returning.
def get_stat_array():
    rolls = []
    are_valid_stats = False
    while are_valid_stats == False:
        # Clear rolls
        rolls = []
        for _ in range(6):
            dice_roll = roll_dice()
            rolls.append(dice_roll)
        stat_info = validate_stat_rolls(rolls)
        are_valid_stats = stat_info[0]
    random.shuffle(rolls)
    return rolls

# Generates your character's race
def get_race():
    races = ["Aarakocra", "Aasimar", "Bugbear", "Centaur",
        "Changeling", "Dragonborn", "Dwarf", "Elf", "Firbolg",
        "Genasi", "Gnome", "Goblin", "Goliath", "Half-Elf", 
        "Half-Orc", "Halfling", "Hobgoblin", "Human", "Kenku", 
        "Kobold", "Lizardfolk", "Loxodon", "Minotaur", "Orc", 
        "Tabaxi", "Tiefling", "Tortle", "Triton", "Warforged", 
        "Yuan-Ti Pureblood"]
    my_race = random.choice(races)
    return my_race

# Generates a class for your character.
def get_class():
    classes = ["Artificier", "Blood Hunter", "Barbarian", 
        "Bard", "Cleric", "Druid", "Fighter", "Monk", 
        "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock",
        "Wizard"]
    my_class = random.choice(classes)
    return my_class

# Generates background.
def get_background():
    backgrounds = ["Acolyte", "Anthropologist", "Athlete",
        "Charlatan", "Cloistered Scholar", "Courtier",
        "Criminal/Spy", "Entertainer", "Far Traveler",
        "Folk Hero", "Gladiator", "Hermit", "Inheritor",
        "Knight", "Noble", "Outlander", "Pirate", "Sage",
        "Sailor", "Soldier", "Urchin"]
    background = random.choice(backgrounds)
    return background

# Export a character to a new file. If one does not exist, creates a file.
def export_character(character):
    file_exists = exists("randomized_characters.csv")
    header = "Name,Gender,Race,Class,Background,Str,Dex,Con,Int,Wis,Cha"

    with open("randomized_characters.csv", mode="at") as file:
        # Write the header if file does not exist.
        if file_exists == False:
            file.write(f"{header}\n")
       
        # Add character line to file.
        file.write(f"{character}\n")

# Prompts the user for a boolean answer. Can pass in a function.
def bool_prompt(question):
    answer = "NOT GIVEN"
    is_valid_answer = False
    while is_valid_answer == False:
        temp_answer = input(question)
        if temp_answer.lower() in('y', 'n'):
            is_valid_answer = True
            if temp_answer == 'y':
                answer = True
            else:
                answer = False
        else:
            print(f"I'm sorry; {temp_answer} wasn't an option.",
                'Type "y" for yes, or "n" for no.')
    return answer


def main():
    keep_going = True
    while keep_going:
        # Get name and gender from user.
        info = get_info()
        name = info[0]
        gender = info[1]
        print(f'Name: {name}\t\tGender: {gender}\t\t', end="")

        # Get character race
        race = get_race()
        print(f'Race: {race}')


        # Get character class
        my_class = get_class()
        print(f'Class: {my_class}\t\t', end="")

        # Get character background 
        background = get_background()
        print(f'Background: {background}')

        # Get stats for character.
        stat_array = get_stat_array()
        strength = stat_array[0]
        dexterity = stat_array[1]
        constitution = stat_array[2]
        intelligence = stat_array[3]
        wisdom = stat_array[4]
        charisma = stat_array[5]
        print('---BASE STATS---')
        print(f'Str: {strength}\t\tDex: {dexterity}\t\tCon: {constitution}')
        print(f'Int: {intelligence}\t\tWis: {wisdom}\t\tCha: {charisma}')
        print()

        # Prompt user if they would like to save their character.
        save_prompt = "Would you like to save your character? (y/n) "
        save = bool_prompt(save_prompt)

        if save:
            # Save character data into a CSV
            character = f"{name},{gender},{race},{my_class},{background},{strength},{dexterity},{constitution},{intelligence},{wisdom},{charisma}"
            export_character(character)
            print(f'Character saved. See file "randomized_characters.csv" for',
                'character stats.')

        # Prompt the user if they would like to generate another character
        keep_going_prompt = "Would you like to create another character? (y/n) "
        keep_going = bool_prompt(keep_going_prompt)
        if keep_going:
            print()
    

if __name__ == "__main__":
    main()