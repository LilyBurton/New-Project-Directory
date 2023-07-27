"""
Given a task("string") with the word TODO,
return "Just Do it!"

"""
from lib.todo import *

def test_with_todo():
    result = todo_task("TODOcleaning")
    assert result == "Just Do It!"

"""
Given a task without the word TODO,
return "You're not doing it?"
"""

def test_without_todo():
    result = todo_task("cleaning")
    assert result == "You're not doing it?"

"""
Given an empty string,
return "No task."
"""

def test_no_task():
    result = todo_task("")
    assert result == "No task."
