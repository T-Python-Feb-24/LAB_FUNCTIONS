def triangal_print(num: int) -> None:
    '''This function print number from num until it reaches 1
then calls triangal_print function again with num decrees by 1 until it reaches 0 
then the function retarn
    '''
    if num == 0:
        return
    for i in range(num, 0, -1):
        print(i, end=" ")
    print()
    triangal_print(num-1)


triangal_print(5)
print(f"\n{triangal_print.__doc__}")

