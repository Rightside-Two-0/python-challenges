#Rightside Two.0: None_profit
#There is a rightside to money, business & property!
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#Write a function named only_ints that takes two parameters. Your function should return True if both parameters are integers, and False otherwise.
#For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.

def only_ints(num1,num2):
    if type(num1) == type(int(1)):
        if type(num2) == type(int(2)):
            return True
        return False
    return False
