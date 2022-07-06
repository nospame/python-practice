from functools import reduce

#  1. Start with an array of numbers and compute the sum of all the numbers.
#     For example, [5, 10, 8, 3] becomes 26.
numbers = [5, 10, 8, 3]

# for loop
sum = 0
for num in numbers:
    sum += num

print(sum)

# reduce function
def do_sum(a, b):
    return a + b

sum = reduce(do_sum, numbers)
print(sum)

#  2. Start with an array of strings and combine them all into a single string.
#     For example, ["volleyball", "basketball", "badminton"] becomes "volleyballbasketballbadminton".
strings = ["volleyball", "basketball", "badminton"]

# for loop
concat_string = ""
for str in strings:
    concat_string += str

print(concat_string)

# join method
concat_string = "".join(strings)

print(concat_string)

# reduce function
def do_concat(a, b):
    return a + b

concat_string = reduce(do_concat, strings)
print(concat_string)

#  3. Start with an array of hashes and compute the sum of the prices (from the :price key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes 105.
products = [
    {"name": "chair", "price": 100}, 
    {"name": "pencil", "price": 1}, 
    {"name": "book", "price": 4}
]

# for loop
sum = 0
for product in products:
    sum += product["price"]

print(sum)

# reduce function
def sum_prices(a, b):
    return a + b["price"]

sum = reduce(sum_prices, products, 0)
print(sum)

#  4. Start with an array of numbers and compute the the minumum number.
#     For example, [5, 10, 8, 3, 9] becomes 3.
numbers = [5, 10, 8, 3, 9]

# for loop
min_num = numbers[0]
for num in numbers:
    if num < min_num:
        min_num = num

print(min_num)

# min method
min_num = min(numbers)

print(min_num)

# reduce function
def get_min(a, b):
    if a < b:
        return a
    return b

min_num = reduce(get_min, numbers)
print(min_num)

#  5. Start with an array of strings and compute the total length of all the strings.
#     For example, ["volleyball", "basketball", "badminton"] becomes 29.
strings = ["volleyball", "basketball", "badminton"]

# for loop
total_length = 0
for str in strings:
    total_length += len(str)

print(total_length)

# reduce function
def sum_length(a, b):
    return a + len(b)

total_length = reduce(sum_length, strings, 0)
print(total_length)

#  6. Start with an array of hashes and find the hash with the lowest price (from the :price key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes {name: "pencil", price: 1}.
products = [
    {"name": "chair", "price": 100}, 
    {"name": "pencil", "price": 1}, 
    {"name": "book", "price": 4}
]

# for loop
min_price = products[0]["price"]
for product in products:
    if product["price"] < min_price:
        min_price = product["price"]

print(min_price)

# reduce function
def get_min_price(a, b):
    if a < b["price"]:
        return a
    return b["price"]

min_price = reduce(get_min_price, products, products[0]["price"])
print(min_price)

#  7. Start with an array of numbers and compute product of all the numbers.
#     For example, [5, 10, 8, 3] becomes 1200.
numbers = [5, 10, 8, 3] 

# for loop
product = 1
for num in numbers:
    product *= num

print(product)

# reduce function
def do_multiply(a, b):
    return a * b

product = reduce(do_multiply, numbers)
print(product)

#  8. Start with an array of strings and combine them all into a single string, separated by dashes.
#     For example, ["volleyball", "basketball", "badminton"] becomes "-volleyball-basketball-badminton-".

#  9. Start with an array of hashes and find the hash with the shortest name (from the :name key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes {name: "book", price: 4}.

# 10. Start with an array of numbers and compute the maximum number.
#     For example, [5, 10, 8, 3] becomes 10.

