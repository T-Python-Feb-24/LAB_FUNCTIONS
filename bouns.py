def pattern_string(n):
    '''Returns a pattern of decreasing integers starting from n to 1 as a s Parameters: n (int): The starting integer value.'''
    pattern=""
    for i in range(n,0,-1):
        for j in range(i,0,-1):
         pattern+=str(j)
    pattern +="\n"
    return pattern 
pattern= pattern_string(10)
print(pattern)