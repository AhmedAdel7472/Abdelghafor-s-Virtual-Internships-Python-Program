#Beginner
#1st task
age = 15

if age < 13:
    print("The person is a child.")
elif 13 <= age < 18:
    print("The person is a teenager.")
else:
    print("The person is an adult.")

#2nd task
number = 10

while number > 0:
    print(number)
    number -= 1

#3rd task
number = 5

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

# intermidiate

#1st task

a = 10
b = 25
c = 15

if a > b and a > c:
    print("The largest number is:", a)
elif b > a and b > c:
    print("The largest number is:", b)
else:
    print("The largest number is:", c)
    
#2nd task 
attempts = 0

while attempts < 3:
    attempts += 1
    print(f"Attempt number {attempts}")


#3rd task 

number = 6
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(f"The factorial of {number} is: {factorial}")

#Hard level

#1st task

year = 2004

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#2nd task
a, b = 0, 1
count = 0

while count < 10:
    print(a)
    a, b = b, a + b
    count += 1
    
#3rd task 
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = []

for num in numbers:
    if num > 1:  # Prime numbers are greater than 1
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)

print("Prime numbers:", prime_numbers)


