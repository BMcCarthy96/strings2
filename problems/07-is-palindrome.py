# Create a function that returns whether or not the string is a Palindrome.

# Write your function here.
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("kayak")) # True
print(is_palindrome("app"))  # False
print(is_palindrome("racecar")) # True
print(is_palindrome("valid")) # False
