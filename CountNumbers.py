# Step 1: Get the number of inputs
count = int(input("Enter how many numbers you want to input: "))

# Step 2: Initialize list and counters
numbers = []
positive_count = 0
negative_count = 0
zero_count = 0

# Step 3: Get list of numbers from user
for i in range(count):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Step 4: Count positive, negative, and zero values
for num in numbers:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

# Step 5: Display the results
print("\nResults:")
print(f"Positive numbers count: {positive_count}")
print(f"Negative numbers count: {negative_count}")
print(f"Zero count: {zero_count}")
