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
