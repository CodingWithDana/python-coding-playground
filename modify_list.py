numbers = [5, 2, 1, 7, 4]

# # Add a number at the end of the list
# numbers.append(20)
# print(numbers)

# # Add a number at a random location in the list, for example, add number 40 in the third spot where 1 is currently located
# numbers.insert(2, 40)
# print(numbers)

# # Remove number 5
# numbers.remove(5)
# print(numbers)

# # Remove everything in the list
# numbers.clear()
# print(numbers)

# # Remove the last item in the list
# numbers.pop()
# print(numbers)

# # Return the index of an item in the list, here we want to return the index of the number 5 in the list
# numbers.index(5)
# print(numbers.index(5))

# # We can use in operator to check the existence of an item in the list. For example, we want to check if 50 in the list above
# print(50 in numbers)
# # This way, if the number doesn't exist, you get False as the output. Instead, if you use numbers.index(50), you will get ValueError message.
# # The in operator is the best way here

# # Count the occurence of an item in the list
# print(numbers.count(5))

# # Sort
# # If you write like this to sort the list, you will get the output None, because this sort method doesnt really return any values
# print(numbers.sort())
# # it simply just sorts this list
# # To use sort() method and print the sorted list, write the code like below: (this way is sorting in ascending order, smallest to largest)
# numbers.sort()
# print(numbers)

# # Sort in decending order (largest to smallest)
# numbers.sort()
# numbers.reverse()
# print(numbers)

# # Get a copy of the list. This method is useful when you modify a list, you can modify the copied list so the original list is always the same
# # Define a variable to store the copy of the list
# copied_list = numbers.copy()

# # Remove the duplicate
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
# # Define a variable to store the unique list
uniques = []
# Loop through the list numbers
for number in numbers:
    if number not in uniques:  # not is an operator
        uniques.append(number)
print(uniques)
