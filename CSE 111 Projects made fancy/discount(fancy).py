from datetime import datetime
import re

count = 0
subtotal = 0
# Deal with price of individual items.
while subtotal != 'done':
    price = 'commence program'
    if price == 'done':
        subtotal = 'done'
    else:
        is_valid_price = False
        while is_valid_price == False:
            if count != 0:
                price = input("Enter the price of the object (or 'done' when finished): $")
            if price == 'done':
                subtotal = 'done'
                break
            is_valid_price = re.search("^[0-9]*\.?[0-9]*$", price)
            if is_valid_price:
                price = float(price)
                is_valid_price = True
            else:
                if count != 0:
                    print("That wasn't a valid price. Check for letters or extra symbols.\n")
                is_valid_price = False
            count += 1

    #Deal with number of items wanted.
    is_valid_quantity = False
    # Skip if subtotal is "done"
    if subtotal != 'done':
        while is_valid_quantity == False:
            quantity = input("Enter the quantity of items: ")
            if quantity.isnumeric():
                quantity = int(quantity)
                is_valid_quantity = True
            else:
                print("That didn't work. Check your entry for letters or symbols.")
        
    # Calculate subtotal.

    if subtotal != 'done':
        subtotal = price * quantity
        # Pull date and time from computer
        this_time = datetime.now()
        # Extract day of week (0 = Monday, 6 = Sunday)
        day_of_week = this_time.weekday()
        deduct = subtotal / 10
        running_total = subtotal

        # VVV Code for testing when Discount works. Comment out.
        # day_of_week = 1
        # VVV Code for testing when Discount doesn't work. Comment out.

        if day_of_week in(1, 2):
            if subtotal >= 50:
                running_total = subtotal - deduct
                print(f"Discount ammount: ${deduct:.2f}")
            else:
                difference = 50 - subtotal
                print(f"You can qualify for a discount if you",
                f"add ${difference:.2f} to your subtotal.")

        tax = running_total * .06
        grand_total = running_total + tax

        print(f"Sales tax: ${tax:.2f}\nTotal: ${grand_total:.2f}\n")
        is_valid_price = False

    
"""
Stretch Challenges
If your team finishes the core requirements in less than an
hour, complete one or more of these stretch challenges.
Note that the stretch challenges are optional.

1. Add code to your program that the computer will execute
if today is Tuesday or Wednesday and the customer is not
purchasing enough to receive the discount. This added code
should compute and print the difference between $50 and the
subtotal which is the additional amount the customer would
need to purchase in order to receive the discount.

2. Near the beginning of your program replace the code that
asks the user for the subtotal with a loop that repeatedly
asks the user for a price and a quantity and computes the
subtotal. This loop should repeat until the user enters
the word "done" for the price.
"""