# @Author: two_0
# @Date:   29-08-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
# @Last modified by:   two_0
# @Last modified time: 29-08-2020
# @License: https://github.com/Rightside-Two-0/Rightside_Two.0/blob/master/LICENSE
# @Copyright: Copyright 2020 © - All Rights Reserved
#~~~~~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
'''
Write a function named is_anagram that takes two strings as its parameters.
Your function should return True if the strings are anagrams, and False
otherwise.
'''
def is_anagram(str1, str2):
    list_1 = list(str1)
    list_1.sort()
    list_2 = list(str2)
    list_2.sort()
    return list_1 == list_2
