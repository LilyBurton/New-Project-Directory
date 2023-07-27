As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

Design a project

def manage_reading_time(text):
<!-- Parameters:
      text = string, in human readable words
      float = decimal number representing reading time. -->

Scenarios!
<!-- Given a text, 200 words,
     It will return 1. -->
    manage_reading_time("200 words") => 1.0

 <!-- Given a text, 400 words,
     It will return 1. -->
    manage_reading_time("200 words") => 2.0

<!-- Given a text, 300 words,
     It will return 1. -->
    manage_reading_time("200 words") => 1.5

<!-- If text is an empty string,
     It will raises an error. -->
     manage_reading_time("") => It raises an error. "Can't estimate reading time from an empty text."
