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

#  4. Start with an array of numbers and create a new array with each number plus 7.
#     For example, [1, 2, 3] becomes [8, 9, 10].

#  5. Start with an array of strings and create a new array with each string's length.
#     For example, ["hello", "goodbye"] becomes [5, 7].

#  6. Start with an array of hashes and create a new array of number values from each hash's :age key.
#     For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes [27, 16].

#  7. Start with an array of numbers and create a new array with each number divided by 2.
#     For example, [1, 2, 3] becomes [0.5, 1.0, 1.5].

#  8. Start with an array of strings and create a new array with each string's first letter only.
#     For example, ["hello", "goodbye"] becomes ["h", "g"].

# 9.  Start with an array of hashes and create a new array of number values from each hash's :age key times 2.
#     For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes [54, 32].

# 10. Start with an array of numbers and create a new array with each number converted into a string.
#     For example, [1, 2, 3] becomes ["1", "2", "3"].

