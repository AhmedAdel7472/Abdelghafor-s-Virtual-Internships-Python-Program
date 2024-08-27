# Question 1
# Create a list of 10 random numbers
numbers = [12, 5, 8, 3, 17, 9, 21, 14, 6, 10]

# Add 2 more numbers to the list
numbers.append(18)
numbers.append(7)

# Remove one number from the list (e.g., remove the number 3)
numbers.remove(3)

# Sort the list in ascending order
numbers.sort()

# Print
print("Sorted list:", numbers)


# Question 2
numbers = (10, 20, 30)
a, b, c = numbers
# Print 
print("a:", a)
print("b:", b)
print("c:", c)


# Question 3

# Create a dictionary with 4 items
students = {
    "Ahmed": 21,
    "Hamsa": 23,
    "Zakaria": 19,
    "Hussain": 20
}

# Update the age of one student (e.g., update Bob's age to 23)
students["Hamsa"] = 23

# Remove another student from the dictionary (e.g., remove Charlie)
del students["Zakaria"]

# Print
print("Updated dictionary:", students)
