# @Author: two_0
# @Date:   01-09-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
# @Last modified by:   two_0
# @Last modified time: 02-09-2020
# @License: https://github.com/Rightside-Two-0/Rightside_Two.0/blob/master/LICENSE
# @Copyright: Copyright 2020 © - All Rights Reserved
def personal_independence(income, ave_expenses):
    if type(income) == type('PASSIVE'):
        return income >= ave_expenses
    return False
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
'''
Define a function named up_down that takes a single number as its parameter.
Your function return a tuple containing two numbers; the first should be one
lower than the parameter, and the second should be one higher.
'''
def up_down(number):
    return number-1, number+1
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
'''
Define a function named consecutive_zeros that takes a single parameter,
which is the string of zeros and ones.
Your function should return the number described above.
'''
def consecutive_zeros(input):
    for item in input:
        if item 
