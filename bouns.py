#Bonus
#Rewrite the function so that it returns the pattern as a string, then assign the result to a variables and print it.

def generate_descending_pattern(num: int) -> str:
    if num <= 0:
        return "Please enter a positive number."
    
    pattern = ""
    for i in range(num, 0, -1):
        line = ' '.join(str(j) for j in range(i, 0, -1))
        pattern += line + "\n"
    
    return pattern.rstrip()

pattern_output = generate_descending_pattern(5)

print(pattern_output)
print(type(pattern_output))