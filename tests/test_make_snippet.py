from lib.make_snippet import make_snippet

def test_to_make_an_empty_snippet():
    result = make_snippet("")
    assert result == ""

def test_to_make_a_snippet_with_four_words():
    result = make_snippet("I love fluffy cats")
    assert result == "I love fluffy cats"

def test_to_make_a_snippet():
    result = make_snippet("I love cats and dogs")
    assert result == "I love cats and dogs"

def test_if_string_is_more_than_5_words():
    result = make_snippet("I love cats and dogs and rats")
    assert result == "I love cats and dogs..."