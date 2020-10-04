# @Author: two_0
# @Date:   03-10-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
# @Last modified by:   two_0
# @Last modified time: 03-10-2020
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
#%%md
#A Custom implementation of the 'zip' function
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
'''
The built-in function zip takes two or more list
and combines them together into one list.
We are to implementation our on logic to make this
happen.
'''
def zap(list_1, list_2):
    master_list = [x for x in list_1]
    for item in list_2:
        master_list.append(item)
    return master_list
#%%
#testing
l_1 = [1,2,3]
l_2 = [4,5,6]
zap(l_1, l_2)
