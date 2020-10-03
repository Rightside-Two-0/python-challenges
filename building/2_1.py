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
#%%md
#Does 2 = 1 ??
#%%
from IPython.display import *
YouTubeVideo('c9ZrAA9vrmA', start=60)
#%%
#NOT TRUE
'''
Returns True if 2 is exactly equal to 1
'''
def two_is_one():
    a = 2
    b = 1
    left_side = a**2
    right_side = b**2
    #comparing~~~~~~~~~~>
    left_side == right_side
    right_side = a*b#<~~~~THIS~IS~ERROR~HERE~~~MAKES~#39~TRUE~~***
    #we can not substitute that which we are (@1:40)
    #trying to prove in the proof itself.
    make_more_difficult_l = left_side-b**2
    make_more_difficult_r = right_side-b**2
    #comparing~~~~~~~~~~>
    make_more_difficult_l == make_more_difficult_r
    expand_left = (a+b)*(a-b)
    expand_right = b*(a-b)
    reduce_left = a+b
    #comparing~~~~~~~~~~>
    reduce_left == b
    #comparing~~~~~~~~~~>
    logic_error_again = a == b#<~~THIS~IS~ERROR~HERE~~~~~***
    #we can not substitute that which we are (@3:30)
    #trying to prove in the proof itself.
    return logic_error_again
#%%
#run it
two_is_one()
