from lib.e_extractor import e_extractor

# Given an empty string, it returns an empty string

def test_given_an_empty_string_return_empty_string():
    result = e_extractor(" ")
    assert result == " "

# Given a string without any e's in it, returns the same string.

def test_given_no_es_return_same_string():
    result = e_extractor("golf")
    assert result == "golf"

    # Given an string with one e in it, 
    # returns the string with the e relocating to the start. 

def test_given_one_e_return_string_with_e_at_start():
    result = e_extractor("hello")
    assert result == "ehllo"

    # Given string with multiple e's in it,
    # return string with all the es at the start. 

def test_given_multple_es_return_string_with_es_at_start():
    result = e_extractor("bees")
    assert result == "eebs"

    # Given string that already has es at the start,
    # return the same string.

def test_given_e_at_start_on_the_string():
    result = e_extractor("eggs")
    assert result == "eggs"