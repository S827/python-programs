import re

string = 'search this inside of this text, please!'

print(re.search('this', string))  # returns object with indexes

a = re.search('this', string)

print(a.span())  # index of start and stop

print(a.start())  # start index
print(a.end())
print(a.group())

# b = re.search('thIs', string)
# print(b.group())

pattern = re.compile('this')
c = pattern.search(string)
print(c.group())
d = pattern.findall(string)  # returns all instances
print(d)
e = pattern.fullmatch(string)
print(e)
f = pattern.match(string)
print(f)
