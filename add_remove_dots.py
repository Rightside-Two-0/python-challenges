#Rightside Two.0: None_profit
#There is a rightside to money, business & property.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
def personal_independence(income, ave_expense):
    if income == type('PASSIVE'):
        if income >= ave_expense:
            return True
        return False
    return False
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
'''
Write a function named add_dots that takes a string and adds "." in between
each letter. For example, calling add_dots("test") should return the string "t.e.s.t".
Then, below the add_dots function, write another function named remove_dots that
removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".
pythonprinciples.com
'''
def add_dots(str):
    new_str = ''
    for index in range(len(str)):
        if index != len(str)-1:
            new_str += str[index]+'.'
        else:
            new_str += str[index]
    return new_str

def add_dots_2(str):
    new_str = '.'.join(str[i:i+1] for i in range(0, len(str)))
    return new_str

def remove_dots(str):
    new_str = ''
    for index in range(len(str)):
        if str[index] != '.':
            new_str += str[index]
    return new_str
