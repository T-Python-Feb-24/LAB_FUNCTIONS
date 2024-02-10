def countDown(number: int)-> int:
    """this function print a formatted pattern that looks like tringle"""
    for i in range(number, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

print(countDown(5))
print(countDown.__doc__)