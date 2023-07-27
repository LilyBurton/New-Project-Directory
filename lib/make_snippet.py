def make_snippet(str):
    words = str.split(" ")
    first_five = words[:5]
    if len(words) > 5:
        return " ".join(first_five) + "..."
    else:
        return str
    
    