"""File input/output practice"""

# 1. Ask user for name and save to file
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2. Read name back and print greeting
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# 3. Sum of first two numbers in numbers.txt
with open("numbers.txt", "w") as out_file:
    print("17\n42\n400", file=out_file)

in_file = open("numbers.txt", "r")
num1 = int(in_file.readline())
num2 = int(in_file.readline())
in_file.close()
print(num1 + num2)

# 4. Sum all numbers in file
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    total += int(line)
in_file.close()
print(total)
