# This function is imported in view.py and edit.py
def is_integer(text):
    return text.isdigit() or (text.startswith("-") and text[1:].isdigit())
