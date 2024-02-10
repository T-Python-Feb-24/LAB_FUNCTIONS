def countDown(number: int) -> str:
    """This function returns the pattern as a string saved in a variable."""
    pattern = ""
    for i in range(number, 0, -1):
        for j in range(i, 0, -1):
            pattern += str(j) + " "
        pattern += "\n"
    return pattern

triangle_pattern = countDown(5)
print(triangle_pattern)
print(countDown.__doc__)
