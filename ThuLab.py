def print_pattern(num):
    '''The shape of this function is nice '''
    for i in range(num, 0, -1):
       
        for j in range(i, 0, -1):
         
            print(j, end=" ")

        print()

print_pattern(5)

print(print_pattern.__doc__)

