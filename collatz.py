# @Author: two_0
# @Date:   29-08-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
# @Last modified by:   two_0
# @Last modified time: 29-08-2020
# @License: https://github.com/Rightside-Two-0/Rightside_Two.0/blob/master/LICENSE
# @Copyright: Copyright 2020 © - All Rights Reserved
'''
Collatz conjecture states that all numbers return to 1 after the
repeated rules; if x is odd: 3x+1 else x/2
'''
def collatz(number):
    steps = 0
    range_numbers = []
    while number != 1:
        if number % 2 == 0:
            number = number / 2
            steps += 1
            range_numbers.append(number)
        else:
            #must be odd
            number = number*3+1
            steps +=1
            range_numbers.append(number)
    return range_numbers, steps
y = range(0, collatz(300)[1])
x = collatz(300)[0]
from matplotlib import pyplot as plt
plt.plot(y, x)
plt.show()
