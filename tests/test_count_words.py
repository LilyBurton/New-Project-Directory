from lib.count_words import count_words

def test_to_count_words_when_there_are_no_words():
    result = count_words("")
    assert result == 0

def test_to_count_words_with_only_one_word():
    result = count_words("Word")
    assert result == 1

def test_to_count_words_in_string():
    result = count_words("Hello world")
    assert result == 2