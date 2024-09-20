#Beginner Level

# Basic Calculator with Multiple Exceptions: Create a program that asks the user to input two numbers
# and an operation (addition, subtraction, etc.). Handle cases where the user enters invalid numbers,
# chooses an invalid operation, or tries to divide by zero.


# try:
#     x = int(input('Enter the First Number '))
# except ValueError:
#     print('Invalid input. Please enter an integer.')

# try:
#     y = int(input('Enter the Second Number '))
# except ValueError:
#     print('Invalid input. Please enter an integer.')

# o = input('Enter the Operation (+, -, *, /): ')


# def switch(o):
#     if o == '+':
#         print(x + y)
#     elif o == '-':
#         print(x - y)
#     elif o == '*':
#         print(x * y)
#     elif o == '/':
#         try:
#             print(x / y)
#         except ZeroDivisionError:
#             print('Not Divisible by zero')
#     else:
#         print('Invalid Operation')

# switch(o)


# List Element Retrieval: Write a function that takes a list and asks the user for an index to retrieve an
# element. Handle cases where the index is out of range or the input is not an integer. Print an
# appropriate error message in each case

# def Retrieve(lis=[]):
#     try:
#         index = int(input('Enter the index: '))
#     except ValueError:
#         print('Invalid input. Please enter an integer.')
#         return

#     if index < 0 or index >= len(lis):
#         raise IndexError('Index out of bounds')  # Raising a more specific exception
#     else:
#         print(f'The element at index {index} is: {lis[index]}')


# lis = [1, 2, 3, 4, 5]

# try:
#     Retrieve(lis)
# except IndexError as e:
#     print(e)  




#Dictionary Key Lookup with Basic Error Handling: Ask the user to input a key to look up in a pre-
#defined dictionary. Use try-except to handle cases where the key does not exist. Additionally, handle
#cases where the user input is not valid, such as providing an empty string or a non-string data type (like
#a number).

def lookup_in_dict(my_dict):
    try:
        key=input('Enter a key to look for ')
        if not key:
           raise ValueError('input cant be empty, Please Enter a valid key.')
        if not isinstance(key,str):
           raise TypeError('Key Must be a string')
    
        value=my_dict[key]
        print(f'The value for "{key}" is: {value}')
    
    except KeyError:
        print(f'Error: The key "{key}" does not exist in the dictionary.')
    
    except ValueError as ve:
        print(ve)

    except TypeError as te:
        print(te)

mydict= {
    'name':'Ahmed',
    'Age': 21,
    'country':'Egypt',
    'Profession':'Software Engineer'
}


lookup_in_dict(mydict)


#Intermidiate Level

# Complex Dictionary and List Handling: Create a program that takes a dictionary where the values are
# lists. Ask the user for a key and an index to retrieve a specific list element. Handle errors for invalid
# keys, invalid indexes, and improper data types for the input.


def retrieve_from_dict_list(my_dict):
    try:
        
        key = input("Enter the key: ")

        
        if key not in my_dict:
            raise KeyError(f"The key '{key}' does not exist in the dictionary.")

        
        list_value = my_dict[key]
        
        
        if not isinstance(list_value, list):
            raise TypeError(f"The value for '{key}' is not a list.")

        
        index = int(input("Enter the index: "))
        
        
        if index < 0 or index >= len(list_value):
            raise IndexError(f"Index {index} is out of bounds for the list associated with '{key}'.")

        
        print(f"The element at index {index} in the list of '{key}' is: {list_value[index]}")

    except KeyError as ke:
        print(ke)
    except ValueError:
        print("Invalid index. Please enter an integer.")
    except IndexError as ie:
        print(ie)
    except TypeError as te:
        print(te)


my_dict = {
    "fruits": ["apple", "banana", "cherry"],
    "numbers": [10, 20, 30, 40]
}

retrieve_from_dict_list(my_dict)



# Multiple File Operations: Design a function that asks the user for a filename, tries to open and read the
# file, and then processes its content. Use try-except blocks to handle the cases where the file does not
# exist, the file is empty, or the content cannot be processed due to type or formatting issues.



def process_file():
    try:
        
        filename = input("Enter the filename: ")
        
        
        with open(filename, 'r') as file:
            content = file.read()

        
        if not content:
            raise ValueError("The file is empty.")

        
        words = content.split()
        print(f"The file contains {len(words)} words.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")


process_file()





# Class Method with Error Handling: Write a class with a method that processes a list of numbers and
# performs operations like finding the maximum, average, and sum. Use try-except blocks to handle cases
# where the list is empty, contains non-numeric elements, or other unexpected issues arise.



class ListProcessor:
    def __init__(self, numbers):
        self.numbers = numbers

    def process_list(self):
        try:
            
            if not self.numbers:
                raise ValueError("The list is empty.")

            
            if not all(isinstance(num, (int, float)) for num in self.numbers):
                raise TypeError("The list contains non-numeric elements.")
            
            
            total = sum(self.numbers)
            avg = total / len(self.numbers)
            max_value = max(self.numbers)

            
            print(f"Sum: {total}")
            print(f"Average: {avg}")
            print(f"Maximum: {max_value}")

        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

numbers = [10, 20, 30, 40]
processor = ListProcessor(numbers)
processor.process_list()
