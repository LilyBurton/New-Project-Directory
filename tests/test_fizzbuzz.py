from lib.fizzbuzz import fizzbuzz
# number which is not divisable by 3 or 5, return number.

def test_given_non_3_5_divisible_returns_number():
    result = fizzbuzz(1)
    assert result == 1

# number which is divisable by 3, return "Fizz". 

def test_given_divisable_by_three_return_fizz():
    result = fizzbuzz(9)
    assert result == "Fizz"

# number is divisable by 5, return "Buzz"

def test_given_if_number_divisable_by_5():
    result = fizzbuzz(25)
    assert result == "Buzz"

# Given a number divisible 3 and 5, return "Fizzbuzz"

def test_given_if_number_is_divisible_by_3_and_5():
    result = fizzbuzz(30)
    assert result == "Fizzbuzz"