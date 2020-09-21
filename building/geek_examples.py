# @Author: two_0
# @Date:   21-09-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
# @Last modified by:   two_0
# @Last modified time: 21-09-2020
# @License: https://github.com/Rightside-Two-0/Rightside_Two.0/blob/master/LICENSE
# @Copyright: Copyright 2020 © - All Rights Reserved
#https://www.geeksforgeeks.org/python-programming-examples/
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
#%%md
#Adding Numbers
#%%
from IPython.display import Latex
def add_it(input1, input2):
    return Latex('$'+str(input1)+'+'+str(input2)+'='+str(input1+input2)+'$')
add_it(3,4)
#%%md
#More General Solution
#%%
def add_all(input_list):
    total = 0
    str_ = ''
    for item in input_list:
        total += item
        if item == input_list[-1]:
            str_ += str(item)
        else:
            str_ += str(item)+'+ '
    return Latex('$'+str_+'='+str(total)+'$')
add_all([3,4,5,6,7])
