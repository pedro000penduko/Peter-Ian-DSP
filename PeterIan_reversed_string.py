# Get user input
input_string = input("Enter a string: ")

# Reverse the input string
reversed_string = input_string[::-1]

# Convert the reversed string to all caps
uppercase_reversed_string = reversed_string.upper()

# Calculate the string count
string_count = len(input_string)

# Display the results
print("OUTPUT:", uppercase_reversed_string)
print("CHARACTERS:", string_count)
