

## Create a function that takes 1 parameter of type int , 
# then it prints out the result formatted like 
# the following patter (if we give it 5 for example):

# 5 4 3 2 1   
# 4 3 2 1   
# 3 2 1   
# 2 1   
# 1   



def number(num:int):
   '''(number) is a function that holds one parameter to print a formatted patern'''
   for i in range(num, 0, -1):
      print(" ".join(str(j) for j in range(i, 0, -1)))
number(5)


### Document the newly created function. describe what it does, 
# then print the documentation. 

print(number.__doc__)