'''
Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter 
(if we give it 5 for example):
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1

Document the newly created function. describe what it does, then print the documentation.
'''

def pattern(count:int):
    '''This function will print a pattern with numbers'''
    for value in range(0, count + 1):
        for val in range(count - value, 0 , -1):
            print(val, end=" ")
        print("\r")

number = 5
pattern(number)
print(pattern.__doc__)