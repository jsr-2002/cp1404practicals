# Example starting point (you can add TODOs in your file)
numbers = [1, 2, 3, 4, 5]

# Example comprehension
squares = [n ** 2 for n in numbers]
print(squares)

# TODO: Create list of even numbers
evens = [n for n in numbers if n % 2 == 0]
print(evens)

# TODO: Create list of numbers doubled
doubles = [n * 2 for n in numbers]
print(doubles)

# TODO: Create list of strings converted to lowercase
names = ["Alice", "Bob", "CHARLIE"]
lower_names = [name.lower() for name in names]
print(lower_names)
