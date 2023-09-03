# Prompt the user for the lengths of the sides
a = float(input("Enter Side 1: "))
b = float(input("Enter Side 2: "))
c = float(input("Enter Side 3: "))

# Calculate the semi-perimeter
s = (a + b + c) / 2

# Calculate the area using Heron's formula without math module
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

# Print the result
print(f"Area: {area}")
