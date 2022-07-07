#  1. Convert an array of arrays into a hash.
#     For example, [[1, 3], [8, 9], [2, 16]] becomes {1 => 3, 8 => 9, 2 => 16}.
arrays = [[1, 3], [8, 9], [2, 16]]
dictionary = {}

# for loop
for array in arrays:
    dictionary[array[0]] = array[1]

print(dictionary)

# dict shorthand (a la Ruby's to_h method)
dictionary = dict(arrays)

print(dictionary)

#  2. Convert an array of hashes into a hash using the :id key from the array's hashes as the keys in the new hash.
#     For example, [{id: 1, color: "blue", price: 32}, {id: 2, color: "red", price: 12}] becomes {1 => {id: 1, color: "blue", price: 32}, 2 => {id: 2, color: "red", price: 12}}.
items_array = [
  {"id": 1, "color": "blue", "price": 32}, 
  {"id": 2, "color": "red", "price": 12}
]
items_dict = {}

# for loop
for item in items_array:
    items_dict[item["id"]] = item

print(items_dict)

#  3. Convert a string into a hash with keys for each letter in the string and values for the number of times the letter appears in the string.
#     For example, "bookkeeper" becomes {"b" => 1, "o" => 2, "k" => 2, "e" => 3, "p" => 1, "r" => 1}.
string = "bookkeeper"
char_count = {}

for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)

#  4. Convert a hash into an array of arrays.
#     For example, {"chair" => 100, "book" => 14} becomes [["chair", 100], ["book", 14]].
items_dict = {"chair": 100, "book" : 14}
items_array = []

for key, value in items_dict.items():
    items_array.append([key, value])

print(items_array)

#  5. Convert a hash into an array of hashes using the keys from each hash as the :id key in each of the array's hashes.
#     For example, {321 => {name: "Alice", age: 31}, 322 => {name: "Maria", age: 27}} becomes [{id: 321, name: "Alice", age: 31}, {id: 322, name: "Maria", age: 27}].
people_dict = {
    321: {"name": "Alice", "age": 31}, 
    322: {"name": "Maria", "age": 27}
}
people_list = []

for key, value in people_dict.items():
    value["id"] = key
    people_list.append(value)

print(people_list)

#  6. Convert an array of strings into a hash with keys for each string in the array and values for the number of times the string appears in the array.
#     For example, ["do", "or", "do", "not"] becomes {"do" => 2, "or" => 1, "not" => 1}.
words = ["do", "or", "do", "not"]
words_count = {}

for word in words:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1

print(words_count)

#  7. Convert a hash into a flat array containing all the hash’s keys and values.
#     For example, {"a" => 1, "b" => 2, "c" => 3, "d" => 4} becomes ["a", 1, "b", 2, "c", 3, "d", 4].
letter_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
letter_list = []

for key, value in letter_dict.items():
    letter_list.append(key)
    letter_list.append(value)

print(letter_list)

#  8. Combine data from a hash with names and prices and an array of hashes with names, colors, and weights to make a new hash.
#     For example, {"chair" => 75, "book" => 15} and [{name: "chair", color: "red", weight: 10}, {name: "book", color: "black", weight: 1}] becomes {"chair" => {price: 75, color: "red", weight: 10}, "book" => {price: 15, color: "black", weight: 1}}.
product_dict = {"chair": 75, "book": 15}
product_list = [
  {"name": "chair", "color": "red", "weight": 10},
  {"name": "book", "color": "black", "weight": 1}
] 
full_product_info = {}

for key, value in product_dict.items():
    selected_product = list(filter(lambda product: product["name"] == key, product_list))[0]
    full_product_info[key] = {
        "price": value, 
        "color": selected_product["color"],
        "weight": selected_product["weight"]
    }

print(full_product_info)

#  9. Convert an array of hashes into a hash of arrays, using the author as keys and the titles as values.
#     For example, [{author: "Jeff Smith", title: "Bone"}, {author: "George Orwell", title: "1984"}, {author: "Jeff Smith", title: "RASL"}] becomes {"Jeff Smith" => ["Bone", "RASL"], "George Orwell" => ["1984"]}.
books_list = [
    {"author": "Jeff Smith", "title": "Bone"},
    {"author": "George Orwell", "title": "1984"},
    {"author": "Jeff Smith", "title": "RASL"}
]
authors_dict = {}

for book in books_list:
    author = book["author"]
    if author in authors_dict:
        authors_dict[author].append(book["title"])
    else:
        authors_dict[author] = [book["title"]]

print(authors_dict)

# 10. Given a hash, create a new hash that has the keys and values switched.
#     For example, {"a" => 1, "b" => 2, "c" => 3} becomes {1 => "a", 2 => "b", 3 => "c"}.
letters_dict = {"a": 1, "b": 2, "c": 3}
switched_k_v = {}

for key, value in letters_dict.items():
    switched_k_v[value] = key

print(switched_k_v)
