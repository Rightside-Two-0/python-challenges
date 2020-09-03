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
    #looking at primes in each series
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
fig = plt.figure()
for index in range(3, 31):
        x = range(collatz(index)[1])
        y = collatz(index)[0]
        print(index, 'steps:', max(x), 'max:', max(y), y)
        #Europhates seeve
        if all(index%i!=0 for i in range(2,index)):
            plt.plot(x,y)
            print('#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>')
