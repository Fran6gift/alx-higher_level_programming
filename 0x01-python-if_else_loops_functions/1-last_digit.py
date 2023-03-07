#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def lastDigit(n):
    if n < 0:
        n = abs(n)
    return (n % 10)

if number < 0:
    last_digit = lastDigit(number) * -1
else:
    last_digit = lastDigit(number)

if last_digit > 5:
    print('Last digit of {:d} is '.format(number) + str(last_digit) +
          ' and is greater than 5')
if last_digit == 0:
    print('Last digit of {:d} is '.format(number) + str(last_digit) +
          ' and is 0')
if last_digit < 6 and last_digit != 0:
    print('Last digit of {:d} is '.format(number) + str(last_digit) +
          ' and is less than 6 and not 0')
