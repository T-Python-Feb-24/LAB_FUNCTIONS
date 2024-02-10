## Create a function that takes 1 parameter of type int , 
# then it prints out the result formatted like the following patter (if we give it 5 for example):
# 5 4 3 2 1   
# 4 3 2 1   
# 3 2 1   
# 2 1   
# 1   

# Document the newly created function. describe what it does, then print the documentation. 
def decreasingPattren(number:int):
    ''' This function Print a decreasing pattern of numbers. 
    Parameters: number (int): The number representing the size of the pattern. '''
    for i in range(number,0,-1):
        for j in range(i,0,-1):
            print(j, end = " ")
        print("")
 
# Function output :            
decreasingPattren(7)

# Function documentation output : 
print(decreasingPattren.__doc__)
