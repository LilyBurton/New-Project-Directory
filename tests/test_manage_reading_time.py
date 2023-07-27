from lib.manage_reading_time import *

"""
    Given a text, 200 words,
    It will return 1. 
    
"""
def test_to_manage_reading_time_with_200_words():
    text = " ".join("word" for i in range(0, 200))
    result = manage_reading_time(text)
    assert result == 1.0

"""
    Given a text, 400 words,
    It will return 2.0. 
    
"""
def test_to_manage_reading_time_with_400_words():
    text = " ".join("word" for i in range(0, 400))
    result = manage_reading_time(text)
    assert result == 2.0

"""

Given a text, 300 words,
It will return 1.5.

"""
def test_to_manage_reading_time_with_300_words():
    text = " ".join("word" for i in range(0, 300))
    result = manage_reading_time(text)
    assert result == 1.5
"""
If text is an empty string,
It will raises an error. 
"""
# def test_to_manage_reading_time_with_no_strings():
#     error = manage_reading_time()
#     assert error == "Error"
    