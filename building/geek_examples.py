# @Author: two_0
# @Date:   21-09-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
# @Last modified by:   two_0
# @Last modified time: 23-09-2020
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
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
from IPython.display import Latex
def add_it(input1, input2):
    return Latex('$'+str(input1)+'+'+str(input2)+'='+str(input1+input2)+'$')
add_it(3,4)
#%%md
#More General Solution
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
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
add_all([3,4,8,13,55,33,21,56,777,345])
#%%md
#Factorial of n
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#6! = 6*5*4*3*2*1
def factorial(input):
    results = input
    if input != 1:
        results *= factorial(input-1)
    return results

factorial(6)
6*5*4*3*2*1 == factorial(6)
#%%md
#Simple Interest
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
'''
Simple interest formula is given by:
Simple Interest = (P x T x R)/100
Where,
P is the principle amount
T is the time and
R is the rate
'''
principle = 25000
term = 360
rate = .06
Simple_Interest = (principle * term * rate)/100
Simple_Interest
#%%md
#Armstrong Numbers
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
'''
Wrtie a function that returns true or false
if the input is infact an Amstring number.
'''
