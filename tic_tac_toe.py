# @Author: two_0
# @Date:   31-08-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
# @Last modified by:   two_0
# @Last modified time: 01-09-2020
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
For example, calling get_row_col("A3") should return the tuple (2, 0) because
A3 corresponds to the row at index 2 and column at index 0in the board
'''
def get_row_col(input):
    part_1 = 0
    part_2 = 0
    if len(input) == 2:
        if input[:1] == 'A':
            part_2 = 0
        elif input[:1] == 'B':
            part_2 = 1
        elif input[:1] == 'C':
            part_2 = 2
        #~~~~~~~~~~~~~~~~~~~~~~~~>
        if input[1:] == '1':
            part_1 = 0
        elif input[1:] == '2':
            part_1 = 1
        elif input[1:] == '3':
            part_1 = 2
    return part_1, part_2
