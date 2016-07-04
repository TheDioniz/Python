# the simplest impossible math problem - the Collatz Sequence
# any number you will pass there, it will finally be decreased to 1

import sys


def collatz(number):
    is_odd = number % 2

    if is_odd:
        ret_val = (3 * number) + 1
    else:
        ret_val = (number // 2)
    return ret_val

# check if used passed correct value - must be int
try:
    number = int(input())
except ValueError:
    print("The value must be an integer.")
    sys.exit(1)

# validate the number until it's equal to 1
while number != 1:
    number = collatz(number)
    print(number)