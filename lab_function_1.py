def number_pattern(number:int)->int:
    ''' This function will prints a descending pattern of numbers starting from specific number to 1.'''
    
    for i in range(number,0 ,-1):
        for j in range(0 , i):
            print(i - j, end =" ")
        print() #new line

# Calling the number_pattern with the argument (5)
number_pattern(5)

# Print the documentation
print(number_pattern.__doc__)

