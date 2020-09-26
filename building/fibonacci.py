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
IFrame('https://en.wikipedia.org/wiki/Fibonacci', width=500, height=400)
#%%
YouTubeVideo('wTlw7fNcO-0', start=10)
#%%
def fibonacci_series(n_terms):
    #sum of the previous two
    n1, n2 = 0,1
    count = 0
    while count < n_terms:
        print(n1)
        fib_sum = n1+n2
        #update the values
        n1 = n2
        n2 = fib_sum
        count +=1
#%%
#testing
fibonacci_series(10)
