def function_1(n):
    """Prints a countdown pattern starting from the entered positive number."""

    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()
#for print the Documention
print(function_1.__doc__)
# input for the user 
number = int(input("Enter a positive integer -> "))
if number <= 0:
    print("Please enter a positive integer.")
else:
    function_1(number)
