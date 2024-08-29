# # example 1
# print('example 1'.upper())

# # try:
# #     age = int(input('enter age: '))
# #     print(age)
# # except:
# #     print('Enter number')

# print('Above code just exits if user entered not an number')

# print('example2'.upper())

while True:
    try:
        # Prompt the user to enter their age
        age = int(input('Enter your age: '))
        print(age)  # Print the valid integer
    except ValueError:  # Catch only ValueError, which occurs when input is not a valid integer
        print('Enter a valid number')
    else:
        print('TY')  # If no error occurred, thank the user
        break  # Exit the loop
