def grammer(text):
    first_letter = text[0]
    last_letter = text[-1]
    punctuation = "!?."
    while first_letter.isupper() is True:
        if last_letter in punctuation:
            return "Correct"
        else:
            return "No Punctuation"
        
    else:
        if last_letter in punctuation:
            return "No Capital Letter"
        else:
            return "No Capital Letter or Punctuation"
    