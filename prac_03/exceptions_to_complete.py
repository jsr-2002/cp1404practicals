"""Exceptions to complete"""

finished = False
result = 0
while not finished:
    try:
        number = int(input("Please enter a number: "))
        finished = True
        result = number
    except ValueError:
        print("Please enter a valid integer.")
print(f"Valid result is: {result}")
