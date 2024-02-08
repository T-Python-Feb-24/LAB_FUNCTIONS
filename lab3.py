def number_la(num1:int)->int:
    ''' this function for print the number '''
    for d in range(num1,0,-1):
        for k in range(d,0,-1):
            print(k, end='')
        print()
number_la(num1=5)
print(number_la.__doc__)

#bonus
def number_la(name1)->str:
    pattern_name:str="lama"
    return pattern_name
print(number_la("lama"))












