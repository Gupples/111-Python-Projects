from Dice_roller import get_rolls, calculate_damage
# Input; add display labels so people can understand what they rolled.

# Validate_int. For making sure input strings can be converted to ints.
def validate_int(number, prompt, error):
    is_valid = False
    temp_number = number
    while is_valid == False:
        temp_number = input(prompt)
        if temp_number.isnumeric():
            temp_number = int(temp_number)
            is_valid = True
        else:
            print(error)
    print()
    return temp_number

def prompt_for_display(value, prompt, error):
    is_valid = False
    temp_value = value
    while is_valid == False:
        temp_value = input(prompt)
        if temp_value.lower() in("y", "n"):
            if temp_value.lower() == 'y':
                temp_value = True
            else:
                temp_value = False
            is_valid = True
        else:
            print(error)
    print()
    return temp_value

# Display all the rolls you made (and calculate total damage)
def display_rolls(rolls, total_rolls, min_roll, roll_final, stat_number):
    # Make stat number green. Note; When changing text color, the statement
    # MUST be surrounded with single quotes.
    print(f'STAT #{stat_number}')
    count = 1
    # Make text white again
    print(f'\033[1;32;40mDISPLAY KEY\nYou rolled: this many times')
    print(f'**************\033[0;37;40m')
    for i in rolls:
        if i != 0:
            print(f"{count}'s: {i}")
        count += 1
    print(f"\nSubtotal: {total_rolls}\nSmallest roll: {min_roll}")
    print(f"Stat: {roll_final}")
    print("------------")

def calculate_min_roll(rolls):
    min = 7
    for i in range(0, 6):
        if i < min and rolls[i] > 0:
            min = i + 1
    return min

def get_stats(show_rolls):
    stats = []
    for i in range(0, 6):
        rolls = get_rolls(6, 4)
        total_rolls = calculate_damage(rolls, False)
        min = calculate_min_roll(rolls)
        stat_total = total_rolls - min

        if show_rolls:
            display_rolls(rolls, total_rolls, min, stat_total, i + 1)
        stats.append(stat_total)
    return stats

def main():
    number = 'a'
    times_prompt = "How many stat sets would you like to roll? "
    error = "Sorry, you need to only have positive numbers."
    times = validate_int(number, times_prompt, error)

    show_rolls = "HAS NOT YET BEEN MADE"
    bool_prompt = "Would you like to see the stat roll breakdowns (y/n)? "
    bool_error = "I'm sorry; you must either type (y) or (n)."
    show_rolls = prompt_for_display(show_rolls, bool_prompt, bool_error)

    all_stat_lines = []
    count = 0
    is_valid_set = True
    while count < times:
        if show_rolls:
            if count != 0:
                print()
            if is_valid_set:
                print(f"------------------STAT SET #{count + 1}------------------\n")
        stats = get_stats(show_rolls)
        stat_line = f"Stats: {stats} Stat total: {sum(stats)}"
        if sum(stats) >= 70:
            if show_rolls:
                print(stat_line)
            else:
                print(f'\033[1;34;40m{stat_line}\033[1;37;40m')
            all_stat_lines.append(stat_line)
            count += 1
            is_valid_set = True
        else:
            if show_rolls:
                print(f'\033[1;31;40m{stat_line}\nStat total does not meet stat',
                    'minimum of 70. Rerolling stats...\033[1;37;40m')
                print(f"------------")
            is_valid_set = False
    if show_rolls:
        print()
        print(f'\033[1;34;40m---SUMMARY OF STAT TOTALS---\033[1;37;40m')
        for i in all_stat_lines:
            print(f'{i}')

if __name__ == "__main__":
    main()