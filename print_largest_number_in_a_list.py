# Create a list of random numbers
numbers = [3, 6, 2, 8, 4, 10]
# Define a variable called max to hold the largest number
max = numbers[0]

# Loop through the list to find the largest number
for number in numbers:
    if number > max:
        max = number
# Print the value of max
print(max)
