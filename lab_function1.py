num = int(input('Choose a number: '))
def my_cool_mehod (number):
    '''this method takes 1 parameter of type int , then it prints out the result formatted'''
    for i in range(num, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()  

my_cool_mehod(num)
print(my_cool_mehod.__doc__)


#Bonus-------------------------------------------------------------------------------------
print('-----this is for Bonus-----')
num2:int = int(input('Choose another number: '))
def my_cool_method_string(number: int) -> str:
    '''This method takes 1 parameter of type int, then returns the pattern as a string.'''
    char_of_nums = ''
    for i in range(num2, 0, -1):
        row_of_char = " ".join(str(x) for x in range(i, 0, -1))
        char_of_nums += row_of_char + '\n'
    return char_of_nums

result_method = my_cool_method_string(num2)
print(result_method)



    


  

        



