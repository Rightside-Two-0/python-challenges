# @Author: Rightside Two.0: None_profit <two_0>
# @Date:   29-08-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
# @Last modified by:   two_0
# @Last modified time: 29-08-2020
# @License: https://github.com/Rightside-Two-0/Rightside_Two.0/blob/master/LICENSE
# @Copyright: Copyright 2020 © - All Rights Reserved
'''
Define a function named count that takes a single parameter.
The parameter is a string. The string will contain a single word
divided into syllables by hyphens
'''
def count(str):
    counter = 0
    for index in range(len(str)):
        if str[index] == '-':
            counter += 1
    return counter+1
