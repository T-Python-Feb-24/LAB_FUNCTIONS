def num_pattern(n:int):
    '''Returns a pattern of decreasing integers starting from n to 1 as a string. Parameters:n (int): The  integer value.'''
    for i in range(n,0,-1):
        for j in range(i,0,-1): 
            print(j,end=' ')
        print('\r')       
num_pattern(5)