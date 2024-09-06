import re

# Find all lower case characters alphabetically between "a" and "m":

txt = "The rain in Spain"

x = re.findall('[a-m]', txt)

print(x)

txt1 = "That will be 59 dollars"

# Find all digit characters:

x1 = re.findall('\d', txt1)
print(x1)

txt2 = "hello planet"

# Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x2 = re.findall('he..o', txt2)
print(x2)

txt3 = "hello planet"

# Check if the string starts with 'hello':
x3 = re.findall('^hello', txt3)
print(x3)
if x3:
    print('Yes, string starts with "hello"')
else:
    print('No match')

txt3 = "hello planet"

# Check if the string ends with 'planet':
x4 = re.findall('planet$', txt3)
if x4:
    print('Yes')
else:
    print('No match')

txt4 = "hello planet"

# Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
x5 = re.findall('he.*o', txt4)
print(x5)

# Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
x6 = re.findall('he.+o', txt4)
print(x6)

# Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
x7 = re.findall('he.?o', txt4)
print(x7)
txt5 = 'jio bekar hai'
x8 = re.findall('ji.?o', txt5)
print(x8)


# Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
x9 = re.findall('he.{2}o', txt4)
print(x9)

txt6 = "The rain in Spain falls mainly in the plain!"

# Check if the string contains either "falls" or "stays":
x10 = re.findall('falls|stays', txt6)
print(x10)
