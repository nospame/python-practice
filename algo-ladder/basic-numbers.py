# Write a function that returns whether a given number is a prime number.

def is_prime(num):
    for i in range(2, int(num / 2)):
        if num % i == 0:
            return False
    return True

print(is_prime(2))    # => True
print(is_prime(48))   # => False
print(is_prime(4259)) # => True
print(is_prime(4263)) # => False


# Write a function that prints out every number from 1 to N, with the following exceptions:

# If the number is divisible by 3, print out "FIZZ".
# If the number is divisible by 5, print out "BUZZ".
# If the number is divisible by both 3 and 5, print out "FIZZBUZZ".

def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FIZZBUZZ")
        elif i % 5 == 0:
            print("BUZZ")
        elif i % 3 == 0:
            print("FIZZ")
        else:
            print(i)

fizz_buzz(30)


# Write a function that gives the Nth number of the Fibonacci Sequence. The Fibonacci sequence begins with 0 and 1, and every number thereafter is the sum of the previous two numbers. So the sequence goes like this:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, and so on until infinity...

# Input: 9
# Output: 21 (as this is the 9th number of the Fibonacci Sequence)
#     Note: this output is incorrect by most standards, which count n(1) as 1
#     n(9) would therefore be 34; the function could easily be modified to return the previous number

def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
    return x

print(fibonacci(9))   


# Given a year, report if it is a leap year.

# The tricky thing here is that a leap year in the Gregorian calendar occurs:

# on every year that is evenly divisible by 4
# except every year that is evenly divisible by 100
# unless the year is also evenly divisible by 400
# For example, 1997 is not a leap year, but 1996 is. 1900 is not a leap year, but 2000 is.

# If your language provides a method in the standard library that does this look-up, pretend it doesn't exist and implement it yourself.

def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

print(leap_year(1997))  # => False
print(leap_year(1996))  # => True
print(leap_year(1900))  # => False
print(leap_year(2000))  # => True


# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_3_5_multiples(n):
    sum = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(sum_3_5_multiples(1000))


# The Collatz Conjecture or 3x+1 problem can be summarized as follows:

# Take any positive integer n. If n is even, divide n by 2 to get n / 2. If n is odd, multiply n by 3 and add 1 to get 3n + 1. Repeat the process indefinitely. The conjecture states that no matter which number you start with, you will always reach 1 eventually.

# Given a number n, return the number of steps required to reach 1.

# Examples
# Starting with n = 12, the steps would be as follows:

# 12
# 6
# 3
# 10
# 5
# 16
# 8
# 4
# 2
# 1

# Resulting in 9 steps. So for input n = 12, the return value would be 9.

def collatz(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
        count += 1
    return count

print(collatz(12))


# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
def is_palindrome(num):
    num_str = str(num)
    for i in range(int(len(num_str) / 2)):
        if num_str[i] != num_str[-(i + 1)]:
            return False
    return True

def largest_palindrome(n):
    max = int('1' + '0' * n)
    large_palindrome = 0
    for i in reversed(range(1, max)):
        for j in reversed(range(1, max)):
            if is_palindrome(i * j):
                if i * j > large_palindrome:
                    large_palindrome = i * j 
                break
    return large_palindrome

print(is_palindrome(334))
print(largest_palindrome(3))
