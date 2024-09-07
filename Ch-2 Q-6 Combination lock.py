import random

# Generate a 3-digit code where each number is between 0 and 9
code_3_digit = [random.randint(0, 9) for _ in range(3)]

# Generate a 4-digit code where each number is between 1 and 6
code_4_digit = [random.randint(1, 6) for _ in range(4)]

# Print the results
print("3-digit code:", ''.join(map(str, code_3_digit)))
print("4-digit code:", ''.join(map(str, code_4_digit)))
