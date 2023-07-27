def todo_task(text):
    ToDo = "TODO"
    if ToDo in text:
        return "Just Do It!"
    elif text == "":
        return "No task."
    else:
        return "You're not doing it?"