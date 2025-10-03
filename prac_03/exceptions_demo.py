"""Demo of exceptions"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

except ZeroDivisionError:
    print("Cannot divide by zero!")

print("Finished.")

# Reflection:
# ValueError occurs if user enters something not an integer (e.g., "abc")
# ZeroDivisionError occurs if denominator = 0
# Avoid ZeroDivisionError by checking denominator != 0 before dividing
