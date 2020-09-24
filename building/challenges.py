#%%
# @Author: two_0
# @Date:   01-09-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
# @Last modified by:   two_0
# @Last modified time: 24-09-2020
# @License: https://github.com/Rightside-Two-0/Rightside_Two.0/blob/master/LICENSE
# @Copyright: Rightside Two.0 ~ Copyright 2020 © - All Rights Reserved
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
#%% md
'''
Create a function that returns 2 strings printed out.
1st: represents the problem (addition) --> **** + **
2nd: represents the answer the characters & the # --> ****** 6
'''
#%%
def add_it(number1, number2):
    print('*'*number1,'+','*'*number2)
    print('*'*(number1+number2), number1+number2)
    return number1+number2
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%% md
'''
Define a function named consecutive_zeros that takes a single parameter,
which is the string of zeros and ones.
'''
#%%
def consecutive_zeros(input):
    count = 1
    longest = 0
    if len(input) > 1:
        for index in range(len(input)):
            if input[index] == input[index-1]:
                if input[index] == '0':
                    count += 1
                    if count > longest:
                        longest = count
            else:
                if count > longest:
                    longest = count
                count = 1
    return longest
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%% md
'''
Define a function named all_equal that takes a list and checks whether
all elements in the list are the same.
'''
#%%
def all_equal(input):
    is_true = True
    for index in range(len(input)):
        if input[index] != input[index-1]:
            is_true = False
    return is_true

#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%% md
'''
Define a function named triple_and that takes three parameters and
returns True only if they are all True and False otherwise.
'''
#%%
def triple_and(input1, input2, input3):
    return input1 and input2 and input3
triple_and(True, False, True)

#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#%% md
'''
Define a function named convert that takes a list of numbers as its only
parameter and returns a list of each number converted to a string.
'''
#%%
def convert(input):
    return [str(x) for x in input]

convert([1,2,3])
#%% md
#Prime Numbers within a range
#%%
#~~Rightside~Two.0~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
'''
Given two positive integers start and end. The task is to write a
Python program to print all Prime numbers in an Interval.
https://www.geeksforgeeks.org
'''
def prime_interval(start, end):
    #cycle through every integer within range
    for item in range(start, end+1):
        #cycle through all below down to 2
        for item_y in range(2, item):
            #test each one if factors
            if item % item_y == 0:
                break
        else:
            print(item)
