# Create a function that reverses the string using recursion.

# Write your function here.
def recursive_string(s):
    # Base case: If the string is empty or has one character, return the string itself
    if len(s) == 0:
        return s
    # Recursive case: reverse the substring and append the first character at the end
    return recursive_string(s[1:]) + s[0]

print(recursive_string("civic")) # civic
print(recursive_string("refer")) # refer
print(recursive_string("string")) # gnirts
print(recursive_string("avocado")) # odacova
print(recursive_string("application")) # noitacilppa
