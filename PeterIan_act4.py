def count_characters(s):
    # Initialize counters
    lowercase_count = 0
    uppercase_count = 0
    digit_count = 0
    special_count = 0

    # Iterate through each character in the string
    for char in s:
        if char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            special_count += 1

    return lowercase_count, uppercase_count, digit_count, special_count

# Input string
input_string = input("Enter a string: ")

# Call the function to count characters
lower, upper, digits, special = count_characters(input_string)

# Display the results
print("Lowercase letters:", lower)
print("Uppercase letters:", upper)
print("Digits:", digits)
print("Special characters:", special)