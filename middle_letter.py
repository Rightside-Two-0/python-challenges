#Rightside Two.0: non.profit
#There is a rightside to money, business & property
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#For example, mid("abc") should return "b"
# and mid("aaaa") should return "".
def middle_letter(word):
    middle = int((len(word)-1)/2)
    return word[middle:middle+1]
