import re

def extract_uppercase(text):

    words = re.split(r"\W+", text)
    uppercase_words = [word for word in words if word.isupper()]
    return uppercase_words  