import math

# Make sure the input is a number so that you can convert it.
def validate_int(number, prompt):
    is_valid = False
    while is_valid == False:
        number = input(prompt)
        if number.isnumeric():
            number = int(number)
            is_valid = True
        else:
            print("Sorry, this program only works with positive integers.\n")
    print()
    return number

# Convert a number from decimal to binary.
def convert_to_binary(decimal):
    
    binary_values = []

    finished = False
    while finished == False:
        # VVV Debug line.
        # print(f'Current Value: {decimal}')
        # VVV Debug line.
        # print(f'{decimal} / 2 = {math.floor(decimal / 2)}')
        # VVV This is the binary value.
        binary = decimal % 2
        # VVV Debug line
        # print(f'Remainder: {binary}')
        if decimal != 1 and decimal != 0:
            decimal = math.floor(decimal / 2)
            binary_values.append(binary)
        else:
            binary_values.append(decimal)
            finished = True

    # VVV Debug line
    # print(f"Binary_values currently has:\n{binary_values}")

    # Make the binary even; add 0's to make complete nibbles.
    nibble = 4 - (len(binary_values) % 4)
    if nibble != 4:
        for i in range(0, nibble):
            binary_values.append(0)

    # At this point, we have the numbers, but in reverse. Let's fix this.
    binary_values.reverse()
    return binary_values

# Display as Binary number
def display_binary(binary_values):
    print(f"Binary;")
    for i in range(0, len(binary_values)):
        print(binary_values[i], end = "")
        if i + 1 != 0:
            if (i + 1) % 4 == 0:
                print(" ", end = "")
    print()

# Display as hexadecimal number.
def display_hexadecimal(binary_values):
    hex_string = ""
    string_storage = ""
    for i in range(0, len(binary_values)):
        # Take in 4 spots from binary_values,
        # convert to hex. Append to hex_string.
        # 10(dec) = A
        string_storage += f"{binary_values[i]}"
        if (i + 1) % 4 == 0:
            if string_storage == "0000":
                hex_string += "0"
            elif string_storage == "0001":
                hex_string += "1"
            elif string_storage == "0010":
                hex_string += "2"
            elif string_storage == "0011":
                hex_string += "3"
            elif string_storage == "0100":
                hex_string += "4"
            elif string_storage == "0101":
                hex_string += "5"
            elif string_storage == "0110":
                hex_string += "6"
            elif string_storage == "0111":
                hex_string += "7"
            elif string_storage == "1000":
                hex_string += "8"
            elif string_storage == "1001":
                hex_string += "9"
            elif string_storage == "1010":
                hex_string += "A"
            elif string_storage == "1011":
                hex_string += "B"
            elif string_storage == "1100":
                hex_string += "C"
            elif string_storage == "1101":
                hex_string += "D"
            elif string_storage == "1110":
                hex_string += "E"
            elif string_storage == "1111":
                hex_string += "F"
            else:
                print(f"Something went wrong in display_hex. string_storage = {string_storage}.")
            string_storage = ''
    print(f"\nHexadecimal: \n{hex_string}")

# Main driver
def main():
    decimal_prompt = 'What is your decimal number? '
    decimal = 'a'
    decimal = validate_int(decimal, decimal_prompt)

    binary_values = convert_to_binary(decimal)
    display_binary(binary_values)
    display_hexadecimal(binary_values)


# Execute program.
if __name__ == "__main__":
    main()