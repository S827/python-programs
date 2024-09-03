from collections import Counter, defaultdict, OrderedDict


# Counter
li = [1, 2, 3, 3, 4, 5, 5, 6, 6, 6, 7, 7, 7, 7, 7]

print(Counter(li))
# Counter creates a counter object, inside that a dictionary with keys as the unique iterable items and values as their frequency
# of items in that list

sentence = 'blah blah some thing in my mind'
print(Counter(sentence))


# defaultdict
dict1 = {'a': 1, 'b': 2}
print(dict1['a'])
# print(dict1['c']) # it throws an error as c as a key not present in dict1

# to avoid the above problem, we can make use of defaultdict
dict2 = defaultdict(lambda: 'does not exist', dict1)
print(dict2['a'])
# no error, it gives default value for the keys which are not available in the dictionary
print(dict2['c'])
print(dict2['z'])


# OrderedDict

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1
print(d)
print(d2)
print(d2 == d)  # False as it is ordered

# let's check above with regular dictionary

d = {'c': 3}
d['a'] = 1
d['b'] = 2

d2 = {'c': 3}
d2['b'] = 2
d2['a'] = 1
print(d)
print(d2)
print(d2 == d)  # True, d and d2 are same dictionary
