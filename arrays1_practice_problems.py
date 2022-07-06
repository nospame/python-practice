# 1. Create an array to store 3 words. Then add two more words to the array and print the array on one line.
words = ["bob", "duck", "weave"]
words.append("punch")
print(words)

# 2. Create an array to store 4 letters. Then change the second letter to a number and print the array on one line.
letters = ["g", "h", "i", "j"]
letters[1] = 17
print(letters)

# 3. Create an array to store 5 numbers. Then print out each number on separate lines with a while loop.
numbers = [7, 14, 21, 24, 38]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

# 4. Create an array to store 1 number. Then add three more numbers to the array and print the array on one line.
numbers = [3]
numbers.extend([8, 12, 16])
print(numbers)

# 5. Create an array to store 3 strings with lower case letters. Then change the third string to have all capital letters and print the array on one line.
strings = ["banana", "tangelo", "grapricot"]
strings[2] = strings[2].upper()
print(strings)

# 6. Create an array to store 3 names. Then print out each name on separate lines with a while loop.
names = ["Jeoffrey", "Bobert", "George"]
i = 0
while i < len(names):
    print(names[i])
    i += 1

# 7. Create an array to store 2 strings. Then add one string to the array and print the array on one line.
strings = ["halt", "who goes there?"]
strings.append("it is I!")
print(strings)

# 8. Create an array to store 5 numbers. Then change the first number to 10 times its original value and print the array on one line.
numbers = [8, 6, 7, 5, 3]
numbers[0] = numbers[0] * 10
print(numbers)

# 9. Create an array to store 2 numbers. Then print out each number on separate lines with a while loop.
numbers = [41, 98]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

# 10. Create an array to store names of 3 different countries. Then add one more country and print the array one line.
countries = ["Brazil", "Chechnya", "Sudan"]
countries.append("Canada")
print(countries)
