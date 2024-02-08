'''
Create a function that takes 1 parameter of type int , 
then it prints out the result formatted like the following 
patter (if we give it 5
'''


def number (num:int) :
 ''' (number) is a function that holds one parameter'''
 for i in range (num, 0, -1):
    for j in range (i, 0, -1):
       total = i + j 
       print(total)
    
       print(j)
    
number(5) 

'''
Document the newly created function. 
describe what it does, then print the documentation. 
'''

print(number.__doc__)

