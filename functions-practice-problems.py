# 1. Write a function that takes in a number and returns the number times two. Then run the function and print the result.
def times_two(num):
    return num * 2

print(times_two(7))

# 2. Write a function that takes in a string and returns the string with all capital letters. Then run the function and print the result.
def capitalize(string):
    return string.upper()

print(capitalize("banana"))

# 3. Write a function that takes in two numbers and returns the first number subtracted by the second. Then run the function and print the result.
def subtract(num1, num2):
    return num1 - num2

print(subtract(7, 3))

# 4. Write a function that takes in a number and returns the number times itself. Then run the function and print the result.
def square(num):
    return num * num

print(square(12))

# 5. Write a function that takes in a string and returns the first letter of the string. Then run the function and print the result.
def first_letter(string):
    return string[0]

print(first_letter("sahara"))

# 6. Write a function that takes in three strings and returns a string that combines all three strings with spaces in between. Then run the function and print the result.
def combine_strings(str1, str2, str3):
    return str1 + " " + str2 + " " + str3

print(combine_strings("apple", "apricot", "antelope"))

# 7. Write a function that takes in a number and returns the number as a string. Then run the function and print the result.
def num_as_string(num):
    return str(num)

print(num_as_string(741))

# 8. Write a function that takes in a string and returns the string repeated 5 times. Then run the function and print the result.
def string_five_times(str):
    return str * 5

print(string_five_times("potato"))

# 9. Write a function that takes in 3 numbers and returns the average (the sum divided by 3.0). Then run the function and print the result.
def average(num1, num2, num3):
    sum = num1 + num2 + num3
    return sum / 3

print(average(6, 8, 91))

# 10. Write a function that takes in a number and returns the number times 10 plus 30. Then run the function and print the result.
def times_10_plus_30(num):
    return num * 10 + 30

print(times_10_plus_30(89))
