#  1. Start with an array of numbers and create a new array with only the numbers less than 20.
#     For example, [2, 32, 80, 18, 12, 3] becomes [2, 18, 12, 3].
numbers = [2, 32, 80, 18, 12, 3]

# for loop
numbers_under_20 = []
for num in numbers:
    if num < 20:
        numbers_under_20.append(num)

print(numbers_under_20)

# filter function
def under_20(num):
    return num < 20

numbers_under_20 = list(filter(under_20, numbers))
print(numbers_under_20)

#  2. Start with an array of strings and create a new array with only the strings that start with the letter "w".
#     For example, ["winner", "winner", "chicken", "dinner"] becomes ["winner", "winner"].
strings = ["winner", "winner", "chicken", "dinner"]

# for loop
w_strings = []
for str in strings:
    if str[0] == 'w':
        w_strings.append(str)

print(w_strings)

# filter function
def starts_with_w(str):
    return str[0] == 'w'

w_strings = list(filter(starts_with_w, strings))
print(w_strings)

#  3. Start with an array of hashes and create a new array with only the hashes with prices greater than 5 (from the :price key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes [{name: "chair", price: 100}].
products = [
    {"name": "chair", "price": 100}, 
    {"name": "pencil", "price": 1}, 
    {"name": "book", "price": 4}
]

# for loop
products_more_than_5 = []
for product in products:
    if product["price"] > 5:
        products_more_than_5.append(product)

print(products_more_than_5)

# filter function
def price_more_than_5(product):
    return product["price"] > 5

products_more_than_5 = list(filter(price_more_than_5, products))
print(products_more_than_5)

#  4. Start with an array of numbers and create a new array with only the even numbers.
#     For example, [2, 4, 5, 1, 8, 9, 7] becomes [2, 4, 8].
numbers = [2, 4, 5, 1, 8, 9, 7]

# for loop
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

# filter function
def is_even(num):
    return num % 2 == 0

even_numbers = list(filter(is_even, numbers))
print(even_numbers)

#  5. Start with an array of strings and create a new array with only the strings shorter than 4 letters.
#     For example, ["a", "man", "a", "plan", "a", "canal", "panama"] becomes ["a", "man", "a", "a"].
strings = ["a", "man", "a", "plan", "a", "canal", "panama"]

# for loop
short_strings = []
for str in strings:
    if len(str) < 4:
        short_strings.append(str)

print(short_strings)

# filter function
def shorter_than_4(str):
    return len(str) < 4
    
short_strings = list(filter(shorter_than_4, strings))
print(short_strings)

#  6. Start with an array of hashes and create a new array with only the hashes with names shorter than 6 letters (from the :name key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes [{name: "chair", price: 100}, {name: "book", price: 4}].

#  7. Start with an array of numbers and create a new array with only the numbers less than 10.
#     For example, [8, 23, 0, 44, 1980, 3] becomes [8, 0, 3].

#  8. Start with an array of strings and create a new array with only the strings that don't start with the letter "b".
#     For example, ["big", "little", "good", "bad"] becomes ["little", "good"].

#  9. Start with an array of hashes and create a new array with only the hashes with prices less than 10 (from the :price key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes [{name: "pencil", price: 1}, {name: "book", price: 4}].

# 10. Start with an array of numbers and create a new array with only the odd numbers.
#     For example, [2, 4, 5, 1, 8, 9, 7] becomes [5, 1, 9, 7].
