#  1. Use a nested loop to convert an array of number pairs into a single flattened array.
#     For example, [[1, 3], [8, 9], [2, 16]] becomes [1, 3, 8, 9, 2, 16].
list = [[1, 3], [8, 9], [2, 16]]
flat_list = []

for sub_list in list:
    for item in sub_list:
        flat_list.append(item)

print(flat_list)

#  2. Use a nested loop with two arrays of strings to create a new array of strings with each string combined.
#     For example, ["a", "b", "c"] and ["d", "e", "f", "g"] becomes ["ad", "ae", "af", "ag", "bd", "be", "bf", "bg", "cd", "ce", "cf", "cg"].
list_a = ["a", "b", "c"]
list_b = ["d", "e", "f", "g"]
list_ab = []

for a in list_a:
    for b in list_b:
        list_ab.append(a + b)

print(list_ab)

#  3. Use a nested loop with one array of strings to create a new array that contains every combination of each string with every other string in the array.
#     For example, ["a", "b", "c", "d"] becomes ["ab", "ac", "ad", "ba", "bc", "bd", "ca", "cb", "cd", "da", "db", "dc"].
list = ["a", "b", "c", "d"] 
list_combos = []

for i in range(len(list)):
    for j in range(len(list)):
        if i != j:
            list_combos.append(list[i] + list[j])

print(list_combos)

#  4. Use a nested loop to find the largest product of any two different numbers within a given array.
#     For example, [5, -2, 1, -9, -7, 2, 6] becomes 63.
numbers = [5, -2, 1, -9, -7, 2, 6]
large_product = 0

for i in range(len(numbers)):
    for j in range(len(numbers)):
        product_ij = numbers[i] * numbers[j]
        if product_ij > large_product and i != j:
            large_product = product_ij

print(large_product)

#  5. Use a nested loop to compute the sum of all the numbers in an array of number pairs.
#     For example, [[1, 3], [8, 9], [2, 16]] becomes 39.
list = [[1, 3], [8, 9], [2, 16]]
sum = 0

for sub_list in list:
    for item in sub_list:
        sum += item

print(sum)

#  6. Use a nested loop with two arrays of numbers to create a new array of the sums of each combination of numbers.
#     For example, [1, 2] and [6, 7, 8] becomes [7, 8, 9, 8, 9, 10].

#  7. Use a nested loop with an array of numbers to compute an array with every combination of products from each number.
#     For example, [2, 8, 3] becomes [4, 16, 6, 16, 64, 24, 6, 24, 9].

#  8. Use a nested loop to find the largest sum of any two different numbers within an array.
#     For example, [1, 8, 3, 10] becomes 18.

#  9. Use nested loops with an array of numbers to compute a new array containing the first two numbers (from the original array) that add up to the number 10. If there are no two numbers that add up to 10, return false.
#     For example, [2, 5, 3, 1, 0, 7, 11] becomes [3, 7].

# 10. Use a nested loop to convert an array of string arrays into a single string.
#     For example, [["a", "man"], ["a", "plan"], ["a", "canal"], ["panama"]] becomes "amanaplanacanalpanama".
