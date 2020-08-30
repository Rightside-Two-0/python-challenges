# @Author: Rightside Two.0: None_profit <two_0>
# @Date:   28-08-2020
# @Email:  philip@two-0.org
# @Project: Python Challenge
# @Last modified by:   two_0
# @Last modified time: 29-08-2020
# @License: https://github.com/Rightside-Two-0/Rightside_Two.0/blob/master/LICENSE
# @Copyright: Copyright 2020 © - All Rights Reserved

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
from capital_indexes import capital_indexes
def test_capital_indexes():
    assert capital_indexes('HeLLo World!') == [0,2,3,6]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
from middle_letter import middle_letter
def test_middle_lettter():
    assert middle_letter('abc') == 'b'

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
from online_status import online_status
def test_online_status():
    assert online_status({"Alice": "online","Bob": "offline","Eve": "online",}) == 2

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
from randomness import random_number
import pytest
# @pytest.mark.repeat(3000)
def test_random():
    number = random_number()
    assert number >= 1 and number <= 101

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
from typecheck import only_ints
def test_typecheck():
    bool = only_ints(1,2)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
from double_letters import double_letters
def test_double_letters():
    bool = double_letters('Hello World!')
    assert bool == True

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
from add_remove_dots import add_dots, add_dots_2, remove_dots
def test_add_dots():
    str = add_dots('test')
    assert str == 't.e.s.t'
def test_add_dots_2():
    str = add_dots_2('test')
    assert str == 't.e.s.t'
def test_remove_dots():
    str = remove_dots('t.e.s.t')
    assert str == 'test'

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
from counting_syllables import count
def test_count():
    num = count('at-tah-ma-ahha')
    assert num == 4

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
from anagrams import is_anagram
def test_is_anagram():
    bool = is_anagram('python','thynop')
    assert bool == True
