def count_chars(text):
    # returns the number of characters
    return len(text)

def count_words(text):
    # returns the amount of words by splitting by each space and counting the number of list items
    return len(text.split())

def count_sentences(text):
    # splits the text into a list by periods and returns how many list items there are
    return text.count(".") + text.count("!") + text.count("?")
