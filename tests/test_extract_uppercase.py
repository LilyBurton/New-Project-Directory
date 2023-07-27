# EXAMPLE

from lib.extract_uppercase import *
"""
Given an empty string, 
return an empty list
"""
def test_extract_empty_with_no_string():
    result = extract_uppercase("")
    assert result == []
"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

"""
Given lowercase words,
return an empty list
"""
def test_with_lowercase_words():
    result = extract_uppercase("hello world")
    assert result == []

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_one_uppercase():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

"""
Given a mixture of uppercase and lowercase words,
return only the uppercase words.
"""
def test_extract_uppercase_words_only():
    result = extract_uppercase("hello WORLD i AM a TEXT")
    assert result == ["WORLD", "AM", "TEXT"]

"""
If there is a text with a mix cased word,
that word is not included in the returned list
"""
def test_extract_uppercase_words_that_doesnt_have_lowercase():
    result = extract_uppercase("hello WoRlD YES")
    assert result == ["YES"]

"""
Given two uppercase words
It returns a list with both words
"""
def test_extract_uppercase_multiple_uppercase_words():
    result = extract_uppercase("HELLO WORLD") 
    assert result == ["HELLO", "WORLD"]

"""
Given a lowercase word and an uppercase word with an exclamation mark
It returns a list with the uppercase word, no exclamation mark
"""
def test_extract_uppercase_with_no_punctuation():
    result = extract_uppercase("hello WORLD!")
    assert result == ["WORLD"]

