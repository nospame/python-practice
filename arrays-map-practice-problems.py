#  1. Start with an array of numbers and create a new array with each number times 3.
#     For example, [1, 2, 3] becomes [3, 6, 9].
# while loop
numbers = [1, 2, 3]
i = 0
while i < len(numbers):
    numbers[i] = numbers[i] * 3
    i += 1

print(numbers)

# for loop
numbers = [1, 2, 3]
for i in range(len(numbers)):
    numbers[i] *= 3

print(numbers)

# map function
numbers = [1, 2, 3]
def times_3(num):
    return num * 3

numbers = list(map(times_3, numbers))
print(numbers)

#  2. Start with an array of strings and create a new array with each string upcased.
#     For example, ["hello", "goodbye"] becomes ["HELLO", "GOODBYE"].
# for loop
strings = ["hello", "goodbye"]
for i in range(len(strings)):
    strings[i] = strings[i].upper()

print(strings)

# map function
strings = ["hello", "goodbye"]
def upper(str):
    return str.upper()

strings = list(map(upper, strings))
print(strings)

#  3. Start with an array of hashes and create a new array of string values from each hash's :name key.
#     For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes ["Alice", "Blane"].
people = [
    {"name": "Alice", "age": 27}, 
    {"name": "Blane", "age": 16}
]

# for loop
people_names = []
for person in people:
    people_names.append(person["name"])

print(people_names)

# map function
def extract_name(person):
    return person["name"]

people_names = list(map(extract_name, people))
print(people_names)

#  4. Start with an array of numbers and create a new array with each number plus 7.
#     For example, [1, 2, 3] becomes [8, 9, 10].
numbers = [1, 2, 3]

# for loop
numbers_plus_7 = []
for number in numbers:
    numbers_plus_7.append(number + 7)

print(numbers_plus_7)

# map function
def add_7(num):
    return num + 7

numbers_plus_7 = list(map(add_7, numbers))
print(numbers_plus_7)

#  5. Start with an array of strings and create a new array with each string's length.
#     For example, ["hello", "goodbye"] becomes [5, 7].
strings = ["hello", "goodbye"]

# for loop
string_lengths = []
for string in strings:
    string_lengths.append(len(string))

print(string_lengths)

# map function
string_lengths = list(map(len, strings))
print(string_lengths)

#  6. Start with an array of hashes and create a new array of number values from each hash's :age key.
#     For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes [27, 16].
people = [
    {"name": "Alice", "age": 27}, 
    {"name": "Blane", "age": 16}
]

# for loop
people_ages = []
for person in people:
    people_ages.append(person["age"])

print(people_ages)

# map function
def extract_age(person):
    return person["age"]

people_ages = list(map(extract_age, people))
print(people_ages)

#  7. Start with an array of numbers and create a new array with each number divided by 2.
#     For example, [1, 2, 3] becomes [0.5, 1.0, 1.5].
numbers = [1, 2, 3]

# for loop
halved_numbers = []
for num in numbers:
    halved_numbers.append(num / 2)

print(halved_numbers)

# map function
def half(num):
    return num /2
  
halved_numbers = list(map(half, numbers))
print(halved_numbers)

#  8. Start with an array of strings and create a new array with each string's first letter only.
#     For example, ["hello", "goodbye"] becomes ["h", "g"].
strings = ["hello", "goodbye"]

# for loop
first_letters = []
for string in strings:
    first_letters.append(string[0])

print(first_letters)

# map function
def first_letter(str):
    return str[0]

first_letters = list(map(first_letter, strings))
print(first_letters)

# 9.  Start with an array of hashes and create a new array of number values from each hash's :age key times 2.
#     For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes [54, 32].
people = [
    {"name": "Alice", "age": 27}, 
    {"name": "Blane", "age": 16}
]

# for loop
people_doubled_ages = []
for person in people:
    people_doubled_ages.append(person["age"] * 2)

print(people_doubled_ages)

# map function
def extract_doubled_age(person):
    return person["age"] * 2

people_doubled_ages = list(map(extract_doubled_age, people))
print(people_doubled_ages)

# 10. Start with an array of numbers and create a new array with each number converted into a string.
#     For example, [1, 2, 3] becomes ["1", "2", "3"].
numbers = [1, 2, 3]

# for loop
num_strings = []
for num in numbers:
    num_strings.append(str(num))

print(num_strings)

# map function
num_strings = list(map(str, numbers))
print(num_strings)

