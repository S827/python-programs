string = "ABCDCDCDCDCDC"
sub_string = "CDC"

count = string.count(sub_string)
print(count)

# pos = string.find(sub_string, 0)
# print(pos)

# pos = string.find(sub_string, 1)
# print(pos)
# pos = string.find(sub_string, 2)
# print(pos)
# pos = string.find(sub_string, 3)
# print(pos)
# pos = string.find(sub_string, 4)
# print(pos)
# for overlapping occurrences
count = 0 # start the counter
start = 0   # position

while start <= len(string) - len(sub_string): # loop should run according to the length of substring and string, 
    # if substring is only 3charcahracer, then we dont need to run the loop at the whole lenfth of the string to 
    # find the occuurence of sdubstring, as after 4th position, there will be only2 characters
    pos = string.find(sub_string, start) # find the position of 1st occurrence of substring starting from start
    if pos != -1:    # is substring is not found, it will return -1, so when it is not -1 execute this line
        count += 1   # , increment the count, that substring is found
        start = pos + 1 # increment the start, as 1st occurrence is found and we need to check for the 2nd occurrence, so start need to recalcualte, which will be pos + 1, to check for the 2nd occurrence if it satisfies the while condition
    else:
        break     # otherwise break the program
print(count)    # got the number of occurrences
