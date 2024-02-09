def triangle(n: int) -> str:
    '''
    Returns a string representing the triangle of numbers.
    '''
    pattern = ""
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            pattern += str(j) + ' '
        pattern += '\n'
    return pattern

user_input = int(input("Enter number: "))
triangle_pattern = triangle(user_input)
print(triangle_pattern)
print(triangle.__doc__)

'''
input:5

output:
5 4 3 2 1 
4 3 2 1
3 2 1
2 1
1


    Returns a string representing the triangle of numbers.
'''