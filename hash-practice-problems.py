# 1. Make a hash to store a person's first name, last name, and email address. Then print each attribute on separate lines.
person = {
  "first_name": "Jeff",
  "last_name": "Robertson",
  "email": "jroberts@robertson.com" 
}
print(person["first_name"])
print(person["last_name"])
print(person["email"])

# 2. Make an array of hashes to store the first name and last name for 3 different people. Then print out the first person's info.
people = [
  {"first_name": "Sally", "last_name": "Ride"},
  {"first_name": "Buzz", "last_name": "Aldren"},
  {"first_name": "Neil", "last_name": "Armstrong"},
]
print(people[0])

# 3. Make a hash to store prices for 3 different menu items. Then add a new menu item and price and print the hash to see the result.
menu = {
  "fries": 1.79,
  "milkshake": 2.39,
  "hamburger": 3.69
}
menu["soda"] = 1.29
print(menu)

# 4. Make a hash to store a book's title, author, number of pages, and language. Then print each attribute on separate lines.
book = {
  "title": "I Am a Cat",
  "author": "Natsume Soseki",
  "num_pages": 218,
  "language": "English"
}
for i in book:
    print("%s: %s" % (i, book[i]))

# 5. Make an array of hashes to store the title and author for 3 different books. Then print out the third book's author.
books = [
  book,
  {"title": "Data Structures and Algorithms", "author": "Jay Wengrow"},
  {"title": "One Hundred Years of Solitude", "author": "Gabriel Garcia Marquez"}
]
print(books[2]["author"])

# 6. Make a hash to store 3 different states and their captitals. Then add a new state and capital and print the hash to see the result.
state_capitals = {
  "Washington": "Olympia",
  "California": "Sacramento",
  "Oregon": "Salem"
}
state_capitals["Nevada"] = "Carson City"
print(state_capitals)

# 7. Make a hash to store a laptop's brand, model, and year. Then print each attribute on separate lines.
laptop = {"brand": "Dell", "model": "business computer", "year": 2019}
for i in laptop:
    print(laptop[i])

# 8. Make an array of hashes to store the brand and model for 3 different laptops. Then print out the second laptop's model.
laptops = [
  laptop,
  {"brand": "Apple", "model": "MacBook Pro"},
  {"brand": "eMachines", "model": "Tower"}
]
print(laptops[1]["model"])

# 9. Make a hash to store definitions for 2 different words. Then add a new word and definition and print the hash to see the result.
word_defs = {"banana": "yellow pointy fruit", "coffee": "hot bean (seed) juice to get ya goin"}
word_defs["water"] = "a wet necessity"
print(word_defs)

# 10. Make a hash to store a shirt's brand, color, and size. Then print each attribute on separate lines.
shirt = {
  "brand": "Calvin Klein",
  "color": "blue",
  "size": "small"
}
for i in shirt:
    print(shirt[i])
