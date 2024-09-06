import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

string = "abc12@yahoo.com"

a = pattern.search(string)
print(a)
string1 = "div@.com"
print(pattern.search(string1))
