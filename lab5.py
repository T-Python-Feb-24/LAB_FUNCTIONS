
print("---print formatted---")
 
def lab(num: int) -> int:
    '''
Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):
Document the newly created function. describe what it does, then print the documentation. 
    '''
    if num <= 0:
        return
    
    for i in range(num, 0, - 1):
        line = ""
        for j in range(i, 0, -1):
            line += str(j) + " "
        print(line.strip())

lab(5)
print(lab.__doc__)

