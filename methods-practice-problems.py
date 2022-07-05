# 1. Write a program that asks the user to enter a word, then prints that word with all capital letters.
input_word = input("Enter a word: ")
print(input_word.upper())

# 2. Write a program that asks the user to enter a number, then prints "That's a big number" if the number is greater than 100.
input_number = input("Enter a number: ")
if int(input_number) > 100:
    print("That's a big number")

# 3. Write a program that asks the user to enter two numbers, then prints the numbers added together.
number1 = input("Enter a number: ")
number2 = input("Enter another number: ")
print(int(number1) + int(number2))

# 4. Write a program that asks the user to enter a word, then prints that word in reverse order.
input_word = input("Enter a word: ")
print(input_word[::-1])

# 5. Write a program that asks the user to enter a number, then prints the number times 10.
input_number = input("Enter a number: ")
print(int(input_number) * 10)

# 6. Write a program that asks the user to enter two words, then prints both words on the same line in all capital letters.
word1 = input("Enter a word: ")
word2 = input("Enter another word: ")
print(word1.upper() + " " + word2.upper())

# 7. Write a program that asks the user to enter a word, then prints the number of letters in the word.
input_word = input("Enter a word: ")
print("%s is %s characters long" % (input_word, len(input_word)))

# 8. Write a program that asks the user to enter a number, then prints "That's a negative number" if the number is less than 0.
input_number = int(input("Enter a number: "))
if input_number < 0:
    print("That's a negative number")

# 9. Write a program that asks the user to enter two numbers, then prints the two numbers multiplied together.
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
print(number1 * number2)

# 10. Write a program that asks the user to enter a word, then prints "That's a long word" if the word has more than 5 letters.
input_word = input("Enter a word: ")
if len(input_word) > 5:
    print("That's a long word")
