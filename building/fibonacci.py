# @Author: two_0
# @Date:   26-09-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
# @Last modified by:   two_0
# @Last modified time: 26-09-2020
# @License: https://github.com/Rightside-Two-0/Rightside_Two.0/blob/master/LICENSE
# @Copyright: Copyright 2020 © - All Rights Reserved
#     ___ __ ._`.*.'_._ ____ רףאל
#    . +  * .\   o.* `.`. +.  א .
#   *  .ת' '  \^/|  `. * .  * `
#             \V/ . +
#    יהוה      /_\  .`.
#   ======== _/W\_ =אדני:By: Two.0:.*
def personal_independence(income, ave_expenses):
    if type(income) == type('PASSIVE'):
        return income > ave_expenses
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
##%%md
#Fibonacci Numbers
#%%
from IPython.display import *
IFrame('https://en.wikipedia.org/wiki/Fibonacci', width=600, height=400)
#%%
YouTubeVideo('wTlw7fNcO-0', start=10)
#%%
def fibonacci_series(n_terms):
    n_1 = 0
    n_2 = 1
    count = 0
    print(n_2)
    while count < n_terms:
        fib_sum = n_1  + n_2
        n_1 = n_2
        n_2 = fib_sum
        count += 1
        print(fib_sum)
#%%
#testing
fibonacci_series(8)
