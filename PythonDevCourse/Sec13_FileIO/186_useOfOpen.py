my_file = open('test.txt')
# print(my_file.read())
# my_file.seek(0)
# # blank line because it moves the cursor to next line where there is no text as it has single line of text
# print(my_file.read())
# my_file.seek(0)  # with seek, we move cursor back to line 1 (index 0)
# print(my_file.read())  # blank line
# print(my_file.read())  # blank line
# print(my_file.read())  # blank line

# print(my_file.readline())  # readline
# print(my_file.readline())  # read next line
# print(my_file.readline())  # read next line
# print(my_file.readline())  # read next line
# print(my_file.readline())  # read next line
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())

print(my_file.readlines())  # returns list of all the lines in the file

my_file.close()
