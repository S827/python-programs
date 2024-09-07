def do_stuff(num=0):
    try:
        if num:
            return int(num) + 50
        elif num == 0:
            return 50
        else:
            return 'please enter number'
    except ValueError as err:
        return err


def power(num):
    try:
        return int(num)**int(num)
    except ValueError as err:
        return err


print(power(10))
