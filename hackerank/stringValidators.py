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

    