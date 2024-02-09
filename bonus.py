# Bonus 

# Rewrite the function so that it returns the pattern 
# as a string, then assign the result to a variables and print it.


def number(num):
    pattern = ""
    for i in range (num, 0, -1):
        pattern += " ".join(str(j) for j in range(i, 0, -1)) + "\n"
    return pattern
result = number(5)
print(result)

