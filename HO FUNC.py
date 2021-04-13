def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def howdy(func):
    text = func("howdy y'all")
    print(text)

howdy(quiet)
howdy(loud)
