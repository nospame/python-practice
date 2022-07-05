# 1. Write a program that uses variables to store a first and last name, then prints the full name in one line using string concatenation (the + operator).
first_name = "Jerome"
last_name = "Monsignor"
print(first_name + " " + last_name)

# 2. Write a program that uses variables to store a first and last name, then prints the full name in one line using string interpolation (the #{} operator).
first_name = "Barbara"
last_name = "Waterson"
print("%s %s" % (first_name, last_name))

# 3. Write a program that asks the user to input a word. If the word is "marco", print "polo".
input_word = input("Enter a word: ")
if input_word == "marco":
    print("polo")

# 4. Write a program that uses variables to store three different colors, then prints out a sentence using the colors with string concatenation (the + operator).
color1 = "purple"
color2 = "brown"
color3 = "magenta"
print(color1 + " " + color2 + " " + color3)

# 5. Write a program that uses variables to store three different colors, then prints out a sentence using the colors with string interpolation (the #{} operator).
print("%s %s %s" % (color1, color2, color3))

# 6. Write a program that asks the user to enter a name. If the name is not "Santa", print "You're not Santa."
input_name = input("Enter a name: ")
if input_name  != "Santa":
    print("You're not Santa.")

# 7. Write a program that uses variables to store a book's title and author, then prints out a sentence using that information with string concatenation (the + operator).
book_title = "I Am a Cat"
book_author = "Natsume Soseki"
print(book_title + " by " + book_author)

# 8. Write a program that uses variables to store a book's title and author, then prints out a sentence using that information with string interpolation (the #{} operator).
print("%s by %s" % (book_title, book_author))

# 9. Write a program that asks the user to enter a password. If the password is "Joshua", the program responds "Shall we play a game?". For any other password, the program responds "Access denied"
input_password = input("Enter a password: ")
if input_password == "Joshua":
    print("Shall we play a game?")
else:
    print("Access denied")

# 10. Write a program that uses variables to store the names of three cities, then prints out a sentence using that information with string concatenation (the + operator).
city1 = "London"
city2 = "New York"
city3 = "Seattle"
print(city1 + ", " + city2 + ", and " + city3)
