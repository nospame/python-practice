# Given a string, write a function that returns true if the “$” character is contained within the string or false if it is not.

# Input: “i hate $ but i love money i know i know im crazy”
# Output: true

# Input: “abcdefghijklmnopqrstuvwxyz”
# Output: false

def incl_dollar(str):
    for char in str:
        if char == '$':
            return True
    return False

print(incl_dollar("i hate $ but i love money i know i know im crazy"))
print(incl_dollar("abcdefghijklmnopqrstuvwxyz"))


# Given a string, write a function that returns a copy of the original string that has every other character capitalized. (Capitalization should begin with the second character.)

# Input: “hello, how are your porcupines today?”
# Output: “hElLo, HoW ArE YoUr pOrCuPiNeS ToDaY?”

def alternate_case(str):
    cased_str = ''
    for i in range(len(str)):
        if i % 2 == 0:
            cased_str += str[i].lower()
        else:
            cased_str += str[i].upper()
    return cased_str

print(alternate_case("hello, how are your porcupines today?"))


# Given a string, write a function that returns the first occurence of two duplicate characters in a row, and return the duplicated character.

# Input: “abcdefghhijkkloooop”
# Output: “h”

def dup_char(str):
    for i in range(len(str) - 1):
        if str[i] == str[i + 1]:
            return str[i]

print(dup_char("abcdefghhijkkloooop"))
print(dup_char("abcdefghijklop"))


# Given a string, write a function that returns true if it is a palindrome, and false if it is not. (A palindrome is a word that reads the same both forward and backward.)

# Input: “racecar”
# Output: true

# Input: “baloney”
# Output: false

def is_palindrome(str):
    for i in range(int(len(str) / 2)):
        if (str[i]) != (str[-(i + 1)]):
            return False
    return True

print(is_palindrome("racecar"))
print(is_palindrome("baloney"))


# Given two strings of equal length, write a function that returns the number of characters that are different between the two strings.

# Input: "ABCDEFG", "ABCXEOG"
# Output: 2

# Explanation: While the A, B, C, E, and G are in the same place for both strings, they have different characters in the other spaces. Since there are 2 such spaces that are different (the D and F in the first string), we return 2.

# Input: "ABCDEFG", "ABCDEFG",
# Output: 0

def diff_chars(str_a, str_b):
    count = 0
    for i in range(len(str_a)):
        if str_a[i] != str_b[i]:
            count += 1
    return count

print(diff_chars("ABCDEFG", "ABCXEOG"))
print(diff_chars("ABCDEFG", "ABCDEFG"))


# Given a string of words, write a function that returns a new string that contains the words in reverse order.

# Input: “popcorn is so cool isn’t it yeah i thought so”
# Output: “so thought i yeah it isn’t cool so is popcorn”

# using reverse method with list
def reverse_words(str):
    split_str = str.split(' ')
    split_str.reverse()
    return ' '.join(split_str)

print(reverse_words("popcorn is so cool isn’t it yeah i thought so"))

# using for loop/only strings
def reverse_words(str):
    slice_to = len(str)
    reversed_str = ''
    for i in reversed(range(len(str))):
        if str[i] == ' ':
            reversed_str += str[i + 1:slice_to]
            reversed_str += ' '
            slice_to = i
        elif i == 0:
            reversed_str += str[:slice_to]
    return reversed_str

print(reverse_words("popcorn is so cool isn’t it yeah i thought so"))    
