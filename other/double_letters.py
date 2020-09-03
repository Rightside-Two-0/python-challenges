#Rightside Two.0: None_profit
#There is a rightside to money, business & property.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#Define a function named double_letters that takes a single parameter.
#The parameter is a string. Your function must return True if there are two
#identical letters in a row in the string, and False otherwise.
def double_letters(str):
    for letter in range(len(str)):
        if str[letter-1] == str[letter]:
            return True
    return False
