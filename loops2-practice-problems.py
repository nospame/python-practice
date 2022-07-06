# 1. Write a while loop to print the numbers 1 through 10.
i = 1
while i <= 10:
    print(i)
    i += 1

# 2. Write a while loop that prints the word "hello" 5 times.
i = 0
while i < 5:
    print("hello")
    i += 1

# 3. Write a while loop that asks the user to enter a word and will run forever until the user enters the word "stop".
while True:
    user_input = input("Please enter a word: ")
    if user_input == "stop":
        break

# 4. Write a while loop that prints the numbers 0 through 100, increasing by 5 each time.
i = 0
while i <= 100:
    print(i)
    i += 5

# 5. Write a while loop that prints the number 9000 ten times.
i = 0
while i < 10:
    print(9000)
    i += 1

# 6. Write a while loop that asks the user to enter a number and will run forever until the user enters a number greater than 10.
while True:
    user_input = input("Enter a number: ")
    if int(user_input) > 10:
        break

# 7. Write a while loop that prints the numbers 50 to 70.
i = 50
while i <= 70:
    print(i)
    i += 1

# 8. Write a while loop that prints the phrase "Around the world" 144 times.
phrase = "Around the world"
i = 0
while i < 144:
    print(phrase)
    i += 1

# 9. Write a while loop that asks the user to enter a word and will run forever until the user enters a word with more than 5 letters.
while True:
    user_input = input("Enter a word: ")
    if len(user_input) > 5:
        break

# 10. Write a while loop that prints the even numbers from 2 to 40.
i = 2
while i <= 40:
    print(i)
    i += 2
