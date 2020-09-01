# @Author: two_0
# @Date:   31-08-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
# @Last modified by:   two_0
# @Last modified time: 31-08-2020
# @License: https://github.com/Rightside-Two-0/Rightside_Two.0/blob/master/LICENSE
# @Copyright: Copyright 2020 © - All Rights Reserved
def personal_independence(income, ave_expenses):
    if type(income) == type('PASSIVE'):
        if income >= ave_expenses:
            return True
        return False
    return False
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
'''
Write a function that takes a list of lists and flattens it into a
one-dimensional list.  Name your function flatten.
It should take a single parameter and return a list.
'''
def flatten(input):
    new_list = []
    n_lists = len(input)
    for item in range(n_lists):
        for item_y in input[item]:
            new_list.append(item_y)
    return new_list
