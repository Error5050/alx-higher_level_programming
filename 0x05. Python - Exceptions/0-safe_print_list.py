#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    total = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            total += 1
        except IndexError:
            break
    print("")
    return (total)




vi 1-safe_print_integer.py

#!/usr/bin/python3


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
