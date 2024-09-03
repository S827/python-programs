# with open('test.txt') as my_file: # with this we dont need to close the file after opening it
#     print(my_file.readlines())

# to just read the file, by default it is read, but can specify as 'r'
# with open('test.txt', mode='r') as my_file:
#     print(my_file.readlines())

# to write, mode = 'r+'

with open('test.txt', mode='r+') as my_file:
    text = my_file.write('Hey it\'s me')
    print(text)

# now again try to write some different text
# with open('test.txt', mode='r+') as my_file:
#     text = my_file.write('Hola') # it replaces Hey with Hola
#     print(text)
# but we what we want is to write next to the text which was already written not to overwrite it
with open('test.txt', mode='a') as my_file:

    text = my_file.write('Hola')  # Hola is now appended at the end of the text
    print(text)
# mode = 'w' will completely remove the texts and update it with new
# with 'w' we can create new files also if it was not created earlier
with open('sad.txt', mode='w') as n_file:
    text = n_file.write(':(')
    print(text)
