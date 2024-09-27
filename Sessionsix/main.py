#Beginner Level

#f=open('myfile.txt','x') you can check the what's inside the file and all my assesments from this github link https://github.com/AhmedAdel7472/Abdelghafor-s-Virtual-Internships-Python-Program

#Reading a File and Printing Content
#Write a Python function that opens a .txt file and prints each line to the console. The file should
#contain at least 5 lines. Use a try-except block to handle any potential errors (like file not found).

def print_file_contents(file_name):
    try:
        with open(file_name,'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_name='myfile.txt'
print_file_contents(file_name)

#Writing to a File
#Write a Python function that takes a list of strings as input and writes each string as a new line to a
#.txt file. If the file already exists, it should overwrite the existing content

def write_lines_to_file(mylist):
    f=open('myfiles.txt','w')
    for line in mylist:
        f.write(line + '\n')
    f.close()


lines = [
    "This is the first line.",
    "Here is the second line.",
    "The third line comes next.",
    "Now we have the fourth line.",
    "Finally, this is the fifth line."
]


write_lines_to_file(lines)


#Appending Data to a File
#Write a Python function that appends 5 new lines to an existing .txt file. Ensure the function adds
#the new lines without deleting the existing content.

def write_lines_to_file(mylist):
    f=open('myfiles.txt','a')
    for line in mylist:
        f.write(line + '\n')
    f.close()


lines = [
    "This is the first line.",
    "Here is the second line.",
    "The third line comes next.",
    "Now we have the fourth line.",
    "Finally, this is the fifth line."
]


write_lines_to_file(lines)

# Counting Words in a File
# Create a Python function that reads a .txt file and counts the total number of words in the file.
# Handle any potential exceptions using try-except

def count_words_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# Example usage
file_name = input("Enter the file name: ")
total_words = count_words_in_file(file_name)
print(f"The total number of words is: {total_words}")

# Reading and Reversing File Content
# Write a Python program that reads a .txt file, stores its content in a list, reverses the order of the
# lines, and writes the reversed content back to the same file

def reverse_file_content(file_name):
    try:
        # Step 1: Read the file and store lines in a list
        with open(file_name, 'r') as file:
            lines = file.readlines()
        
        # Step 2: Reverse the order of the lines
        reversed_lines = lines[::-1]
        
        # Step 3: Write the reversed lines back to the same file
        with open(file_name, 'w') as file:
            for line in reversed_lines:
                file.write(line)
                
        print(f"The content of '{file_name}' has been reversed successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_name = input("Enter the file name: ")
reverse_file_content(file_name)



# Searching for a Specific Word
# Write a Python function that searches for a specific word in a .txt file and prints the line number(s)
# where the word appears. If the word doesn't exist, handle it using try-except.

def search_word_in_file(file_name, word):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            word_found = False
            
            
            for line_number, line in enumerate(lines, start=1):
                if word in line:
                    print(f"Word '{word}' found in line {line_number}: {line.strip()}")
                    word_found = True
            
            
            if not word_found:
                print(f"Word '{word}' not found in the file.")

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_name = input("Enter the file name: ")
word = input("Enter the word to search for: ")
search_word_in_file(file_name, word)



