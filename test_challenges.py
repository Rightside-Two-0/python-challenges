#Rightside Two.0: None.profit
#There is a rightside to money, business & property
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
    assert bool == True
