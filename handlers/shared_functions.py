from random import randint

# These functions are imported in view.py and edit.py
def is_integer(text):
    return text.isdigit() or (text.startswith("-") and text[1:].isdigit())

def append_emoji(text, category):
    """
    This function makes some text more pretty with emojies
    Text - any string
    Category - number 0 through 3, list index
    """
    # Categories in order: offline edu, online edu, day off, work
    categories = [
        ["🚌", "🎓", "👩🏼‍🏫"],
        ["✍️", "📚", "💻"],
        ["🤟", "💤", "🥰"],
        ["🔥", "📈", "💸"],
    ]
    return text + " " + categories[category][randint(0, 2)]
