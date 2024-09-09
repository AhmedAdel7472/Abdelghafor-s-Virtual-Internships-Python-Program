# Beginner Level :
# Function with Multiple Arguments: Write a function calculate_total_price() that takes the price of an item and the quantity purchased, and returns the total price. Ensure the function handles cases where either argument is missing by setting default values

def Total_Price(item_price=0.0,quantity=0):
    total=item_price * quantity
    return total
item_price=float(input("what is the Item price "))
quantity=int(input("what is the Quantity "))
print(f"Total Price = {Total_Price(item_price,quantity)}")    

# Function with Conditional Logic: Create a function is_even() that takes an integer as an argument and returns True if the number is even and False if it's odd.Include simple error handling for non-integer inputs using conditional statements.

def isEven(ur_input=0):
    if ur_input.is_integer()==True:
        if ur_input%2==0:
            return True
        else:
            return False
    else:
        print("Your Number is not an integer")
        return None

ur_input=float(input("What is the number you want to check ? "))
Cond=isEven(ur_input)
if Cond is True:
    print("Your Number is Even")
elif Cond is False:
    print("Your Number is Odd")
else:
    print("Please enter a valid integer number.")

# String Manipulation in Functions: Write a function 
# format_name() that takes a first name and last name as
# arguments and returns a neatly formatted full name,
# e.g., "Ahmed Hazem". Ensure that the function handles
# cases where names are provided in lowercase.

def Foramt_Name(first_name,last_name):
    full_name=first_name+last_name
    return full_name

first_name=input("Your First Name ").capitalize()
last_name=input("Your Last_Name ").capitalize()
print(Foramt_Name(first_name,last_name))

# Intermediate Level :
# List Manipulation in Functions: Write a function
# remove_duplicates() that takes a list of numbers and
# returns a new list with all duplicate numbers removed,
# maintaining the original order.Intermediate Level :
# List Manipulation in Functions: Write a function
# remove_duplicates() that takes a list of numbers and
# returns a new list with all duplicate numbers removed,
# maintaining the original order.


def remove_duplicates(listaya=[]):
    myset=set()
    for i in listaya:
        myset.add(i)
    return myset
listaya=[1,2,3,4,5,6,7,8,2,3,9,10,5,3,4]
sets={}
sets=remove_duplicates(listaya)
print(sets)

# Recursive Function for Factorial Calculation: Write a
# function factorial() that takes an integer and returns
# its factorial using recursion. Ensure the function is
# optimized for larger inputs.


def factorial(number):
    if number==0 or number==1:
        return 1
    return number * factorial(number-1)

print(factorial(5))


# Function with Multiple Return Values: Create a
# function calculate_statistics() that takes a list of
# scores and returns the highest score, the lowest score,
# and the average score. Ensure the function works
# correctly with positive numbers.


def calculate_statistics(listaya=[]):
    Total=0
    print(f"Maximum Number = {max(listaya)}")
    print(f"Minimum Number = {min(listaya)}")
    for i in listaya:
        Total+=i
    Average=Total/(len(listaya))
    return Average
listaya=[1,2,3,4,5]
avg=calculate_statistics(listaya)
print(f"Average number = {avg}")