def pattrenSrting(number:int):
    numList = []
    for i in range(number,0,-1):
        for j in range(i,0,-1):
            numList.append(f"{str(j)} ")
        numList.append("\n")
    numList.pop()
    stringOutput =''.join(numList)
    return stringOutput

# Rewrite the function so that it returns the pattern as a string, then assign the result to a variables and print it.
result = pattrenSrting(7)
print(result)

