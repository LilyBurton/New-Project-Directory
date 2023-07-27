from lib.grammer import *

"""
Given sentance with Capital letter and punctuation
"""

def test_with_capital_letter_and_punctuation():
    result = grammer("Hello World!")
    assert result == "Correct"

"""
Given sentance with no Capital Letter
"""
def test_without_capital_letter():
    result = grammer("hello world!")
    assert result == "No Capital Letter"

def test_without_punctuation():
    result = grammer("Hello World")
    assert result == "No Punctuation"

def test_without_punctuation_or_capital():
    result = grammer("hello world")
    assert result == "No Capital Letter or Punctuation"