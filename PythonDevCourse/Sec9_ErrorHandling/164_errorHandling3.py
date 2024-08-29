while True:
    try:
        age = int(input('What is your age? '))
        10 / age
        # raise ValueError('Stop it now')
        raise Exception('Stop it now')
    # except ValueError:
    #     print('Please enter a number')
    #     continue
    except ZeroDivisionError:
        print('Please enter age other than 0')
        break
    else:
        print('TY')
        break
    finally:
        print('Ok, I am finally done.')
    print('Can you hear me?')
