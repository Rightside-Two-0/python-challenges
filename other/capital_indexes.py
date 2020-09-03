#!/usr/bin/env python3
#Rightside Two.0: Python challenges
# ~ Its always better to be on the rightside ~
#give a word like HeLlO --> [0,2,4]
def capital_indexes(word):
    content = []
    for index, item in enumerate(word):
        if item.isupper():
            content.append(index)
    return content
