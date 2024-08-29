def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f"please enter numbers {err}")


print(sum(1, '2'))


def div(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(f'oops {err}')


print(div(1, 0))
print(div(1, 2))
print(div(1, '0'))
