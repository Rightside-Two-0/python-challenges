# @Author: two_0
# @Date:   29-08-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
# @Last modified by:   two_0
# @Last modified time: 30-08-2020
# @License: https://github.com/Rightside-Two-0/Rightside_Two.0/blob/master/LICENSE
# @Copyright: Copyright 2020 © - All Rights Reserved
'''
Collatz conjecture states that all numbers return to 1 after the
repeated rules; if x is odd: 3x+1 else x/2
'''
def collatz(number):
    range_numbers = []
    steps = 0
    while number > 1:
        if number % 2 == 0:
            number = number/2
            range_numbers.append(number)
            steps += 1
        else:
            number = 3*number+1
            range_numbers.append(number)
            steps += 1
    return range_numbers, steps
#~~~~Rightside~Two~~~~~~~~~~~~~~~~~>
import matplotlib.pyplot as plt
for index in range(3, 34):
    fig = plt.figure()
    x = range(collatz(index)[1])
    y = collatz(index)[0]
    plt.title('Collatz Conjecture of ('+str(index)+')')
    plt.ylabel('height of x')
    plt.xlabel('# of steps needed to return to source')
    plt.plot(x,y)
