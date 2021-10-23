import re

def main():
    # Get an odometer value in U.S. miles from the user.
    first_prompt = "Enter the first odometer reading (in miles): "
    first = 'a'
    # Get another odometer value in U.S. miles from the user.
    second_prompt = "Enter the second odometer reading (in miles): "
    second = 'a'
    # Get a fuel amount in U.S. gallons from the user.
    fuel_prompt = "Enter the amount of fuel used (in gallons): "
    fuel = 'a'
    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    mpg = miles_per_gallon(first, second, fuel)
    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)
    # Round the miles per gallon to one digit after the decimal.
    mpg = round(mpg, 1)
    # Round the liters per 100 km to two digits after the decimal.
    lp100k = round(lp100k, 2)
    # Display the results for the user to see.
    print(f"{mpg} miles per gallon")
    print(f"{lp100k} liters per 100 kilometers")
    pass


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.
    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    mpg = (end_miles - start_miles) / amount_gallons
    return mpg


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.
    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    metric = 235.215 / mpg
    return metric

# Make sure each float input can be converted to a float
def validate_float(number, prompt):
    is_valid = False
    while is_valid == False:
        number = input(prompt)
        is_valid = re.search("^[0-9]*\.?[0-9]*$", number)
        if is_valid:
                number = float(number)
                is_valid = True
        else:
                print("That wasn't a valid float. Check for letters or extra symbols.")
                is_valid = False
    return number

def validate_int(number, prompt):
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
# Call the main function so that
# this program will start executing.
main()