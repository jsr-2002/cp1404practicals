"""Random number practice"""
import random

# Example outputs
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# Questions as comments:
# Line 1: Smallest = 5, Largest = 20
# Line 2: Produces odd numbers between 3 and 9 (cannot produce 4)
# Line 3: Any float between 2.5 and 5.5 inclusive

# New code: random number between 1 and 100 inclusive
print(random.randint(1, 100))
