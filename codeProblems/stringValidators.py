"""
Task

You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string .

Constraints


Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

Sample Input

qA2
Sample Output

True
True
True
True
True
"""

if __name__ == "__main__":
    s = input()

    has_alnum = any(c.isalnum() for c in s)
    print(has_alnum)

    has_alpha = any(c.isalpha() for c in s)
    print(has_alpha)

    has_digit = any(c.isdigit() for c in s)
    print(has_digit)

    has_lower = any(c.islower() for c in s)
    print(has_lower)

    has_upper = any(c.isupper() for c in s)
    print(has_upper)

# in a single for loop

if __name__ == "__main__":
    s = input()

    for c in s:
        if c.isalnum():
            has_alnum = True
        if c.isalpha():
            has_alpha = True
        if c.isdigit():
            has_digit = True
        if c.islower():
            has_lower = True
        if c.isupper():
            has_upper = True

    print(has_alnum)
    print(has_alpha)
    print(has_digit)
    print(has_lower)
    print(has_upper)

# break from loop when already found the requirement

if __name__ == "__main__":
    s = input()
    has_alnum = False
    has_alpha = False
    has_digit = False
    has_lower = False
    has_upper = False

    for c in s:
        if not has_alnum and c.isalnum():
            has_alnum = True
        if not has_alpha and c.isalpha():
            has_alpha = True
        if not has_digit and c.isdigit():
            has_digit = True
        if not has_lower and c.islower():
            has_lower = True
        if not has_upper and c.isupper():
            has_upper = True

        # if all conditions already met, break out from loop, as no need to iterate any more
        if has_alnum and has_alpha and has_digit and has_lower and has_upper:
            break
    
    print(has_alnum)
    print(has_alpha)
    print(has_digit)
    print(has_lower)
    print(has_upper)