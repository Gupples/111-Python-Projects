import math
import re

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

# Validate_float. For making sure input strings can be converted to floats.
# (remember to import re when used.)
def validate_float(number, prompt, error):
    is_valid = False
    temp_number = number
    while is_valid == False:
        temp_number = input(prompt)
        # This specific search is set up for prices
        is_valid = re.search("^[0-9]*\.?[0-9]*$", temp_number)
        if is_valid:
                temp_number = float(temp_number)
                is_valid = True
        else:
                print(error)
                is_valid = False
    return temp_number

# Alternative way of executing main(). Usefull when 
#  testing functions or importing. remember to uncomment
#  when you use it.
#  
# if __name__ == "__main__":
#     main()
# 
# When writing test code, you can use this instead of making
# and calling a main().
# 
# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
# pytest.main(["-v", "--tb=line", "-rN", __file__])
# ^^^^^^^^^^^ Uncomment this line.  