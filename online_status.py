#Rightside Two.0: non.profit
#There is a rightside to money, business & property.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#statuses = {
#    "Alice": "online",
#    "Bob": "offline",
#    "Eve": "online",
#}
#In this case, the number of people online is 2.
#Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
#Your function should return the number of people who are online.
def online_status(status):
    count = 0
    for key, item in status.items():
        if item == 'online':
            count += 1
    return count
