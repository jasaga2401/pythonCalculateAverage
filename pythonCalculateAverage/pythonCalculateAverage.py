
# Correct program: Calculates the average correctly.
def calculate_average_correctly(numbers):
    # Excludes zeros from the sum and count
    valid_numbers = [num for num in numbers if num != 0]
    return sum(valid_numbers) / len(valid_numbers) if valid_numbers else 0

# Incorrect program: Incorrectly calculates the average, including zeros in the count.
def calculate_average_incorrectly(numbers):
    # Includes zeros in the count
    return sum(numbers) / len(numbers) if numbers else 0

# Test case
data = [10, 20, 0, 30, 0, 40]  # Mixed list with some zero values

# Calculate averages using both methods
correct_result = calculate_average_correctly(data)
incorrect_result = calculate_average_incorrectly(data)

# Print results
print(f"Correct Average: {correct_result}")
print(f"Incorrect Average: {incorrect_result}")
