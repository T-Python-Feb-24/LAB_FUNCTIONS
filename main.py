def intgers(x):
 ''' Function thats print from n to 1 in pattern '''
 for i in range(x, 0, -1): # 
    
    for m in range(i,0,-1 ):
        print(m,end=' ')
    print('\r')

intgers(5)
print(intgers.__doc__)
