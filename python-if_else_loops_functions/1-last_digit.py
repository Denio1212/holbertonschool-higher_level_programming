#!/usr/bin/python3
import random
number = random.randint(-10001, 10000)

if number > 0:
    lastdigit = number % 10
else:
    lastdigit = number % -10
print("Last digit of {} is {}".format(number, lastdigit), end=' ')
if number > 5:
    print("and is greater than 5")
elif number == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
