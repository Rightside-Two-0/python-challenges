# @Author: two_0
# @Date:   01-09-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
# @Last modified by:   two_0
# @Last modified time: 01-09-2020
# @License: https://github.com/Rightside-Two-0/Rightside_Two.0/blob/master/LICENSE
# @Copyright: Copyright 2020 © - All Rights Reserved
'''
Write a function named palindrome that takes a single string as its
parameter. Your function should return True if the string is a palindrome,
and False otherwise.
'''
def palindrome(input):
    new_str = ''
    for index in range(len(input)-1, -1, -1):
        new_str += input[index]
    if new_str == input:
        return True
    return False
