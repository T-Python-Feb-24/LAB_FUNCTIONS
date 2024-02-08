def triangal(num: int) -> str:
    '''This function will add the number from i to a string until num reaches one. If num = 1
return 1
    '''
    result = ""
    if num == 1:
        return "1"
    else:
        for i in range(num, 0, -1):
            result += str(i)+" "
            
    result += f"\n{str(triangal(num-1))}"

    return result


result = triangal(5)
print(result)
