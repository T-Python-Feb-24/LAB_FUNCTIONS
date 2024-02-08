def function_2(num):
    '''
    Prints a countdown pattern starting from the entered positive number.
    Rewrite the function so that it returns the pattern as a string, then assign the result to a variables and print it.
    '''

    pattern = ""  
    for i in range(num, 0, -1):
        line = ""
        for j in range(i, 0, -1):
            line += str(j) + " "  
        pattern += line.strip() + "\n"  
    return pattern 

pattern_result = function_2(1)


print(pattern_result)

# Input for the user 
number = int(input("Enter a positive integer: "))
if number <= 0:
    print("Please enter a positive integer.")
else:
    pattern_result = function_2(number)
    print(pattern_result)
