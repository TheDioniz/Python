# the simplest impossible math problem - the Collatz Sequence
# any number you will pass there, it will finally be decreased to 1
def collatz(number):
    is_odd = number % 2

    if is_odd:
        ret_val = (3 * number) + 1
    else:
        ret_val = (number // 2)
    return ret_val

#get number from the user  - cast string to int at once
number = int(input())

#validate the number until it's equal to 1
while number != 1:
    number = collatz(number)
    print(number)