def number_pattern(number):
    """
    This function will take a number to descending pattern of numbers starting from specific number to 1 
    then it will return a sting with this pattern.
    """
    string_pattern = ""
    for i in range(number, 0, -1):
        for j in range(0, i):
            string_pattern += f"{str(i-j)} "
        string_pattern += "\n"
    return string_pattern

# Using the function and printing the result
take_string_pattern = number_pattern(5)
print(take_string_pattern)