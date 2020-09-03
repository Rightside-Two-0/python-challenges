# @Author: two_0
# @Date:   31-08-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
# @Last modified by:   two_0
# @Last modified time: 31-08-2020
# @License: https://github.com/Rightside-Two-0/Rightside_Two.0/blob/master/LICENSE
# @Copyright: Copyright 2020 © - All Rights Reserved
'''
returns the difference between the min
value and max value in given list
'''
def difference(input):
    min = 2**32
    max = 0
    for item in input:
        if item < min:
            min = item
        if item > max:
            max = item
    return max-min
