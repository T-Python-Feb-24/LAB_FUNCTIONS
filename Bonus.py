# Rewrite the function so that it returns the pattern as a string, then assign the result to a variables and print it.


def pattern(count:int) -> str:
    pattern = ""
    for row in range(count, 0, -1):
        line = ""
        for cal in range(row, 0, -1):
            line += str(cal) + " "
        pattern += line + "\n"
    return pattern

number = 7
result = pattern(number)
print(result)