matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Access to the second item of the first inner list
matrix[0][1]
print(matrix[0][1])

# Modify the second item of the first inner list to 20. Then print the updated inner list
matrix[0][1] = 20
print(matrix[0])

# Loop through the 2 dimensional list called matrix, where row is each inner list
for row in matrix:
    for item in row:
        print(item)
