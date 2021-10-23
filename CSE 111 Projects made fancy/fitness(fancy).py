# Import datetime so that user's
# age can be computed. 
from datetime import datetime
import re

# re.search("[1-2][0-9][0-9][0-9]\-[0-1][0-9]\-[0-3][0-9]", whatever-variable-i-want)

def main():
    # Get user's gender, birthdate, height, and weight.
    gender = input("Please enter your gender (M or F): ")
    birthday = input("Please enter your birthdate (YYYY-MM-DD): ")
    weight = int(input("Enter your weight in US pounds: "))
    height = int(input("Enter your height in US inches: "))
    # Call compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rage
    # functions as needed.
    age = compute_age(birthday)
    kg = kg_from_lb(weight)
    cm = cm_from_in(height)
    bmi = body_mass_index(weight, height)
    bmr = int(round(basal_metabolic_rate(gender, kg, cm, age), 0))
    # Print the results for the user to see.
    print(f"Age (years): {age}")
    print(f"Weight (kg): {kg:.1f}")
    print(f"Height (cm): {cm:.1f}")
    print(f"Body mass index: {bmi:.1f}")
    print(f"Basal metabolic rate (kcal/day): {bmr}")

def compute_age(birth):
    """
    Compute and return a person's age in years.
    Parameter birth: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    birthday = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # birthday in years.
    years = today.year - birthday.year

    # If necessary, subtract one from the difference.
    if birthday.month > today.month or \
        (birthday.month == today.month and birthday.day > \
            today.day):
            years -= 1
    
    return years

def kg_from_lb(lb):
    """
    Convert a mass in pounds to kilograms.
    Parameter lb: a mass in US pounds.
    Return: the mass in kilograms.
    (1 lb = 0.45359237 kg.)
    """
    kg = lb * 0.45359237
    return kg

def cm_from_in(inch):
    """
    Convert a length in inches to centimeters.
    Parameter inch: a length in inches.
    Return: the length in centimeters.
    (1 in = 2.54 cm)
    """
    cm = inch * 2.54
    return cm

def body_mass_index(weight, height):
    """
    Calculate and return aperson's body mass index (bmi).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
    Return: a person's body mass index.

    bmi = (10,000 * weight) / (height ** 2)
    """
    bmi = (10000 * weight) / (height ** 2)
    return bmi

def basal_metabolic_rate(gender, weight, height, age):
    """
    Calculate and return a person's basal metabolic rate (bmr)
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
        age must be in years.
    Return: a person's basal metabolic rate in kcal per day.
    Women:
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    Men:
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    """
    bmr = 0
    if gender.lower() == 'f':
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    elif gender.lower() == 'm':
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    else: 
        print(f"Check your gender entry. Something went wrong.")
    return bmr

main()
# Call the main function so that the program executes.