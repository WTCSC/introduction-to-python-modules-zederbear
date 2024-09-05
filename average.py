"""
Import the text_utils module you created and calculate the average number of
words per line in a given text file. The text file that will be used to test
this is the text file called "sample.txt" (located in the same directory as
this exercise). The average number of words per line should be rounded down to
the nearest integer.

Print the average number of words per line in the text file in the following
format:

"Average words per line: [average]"
"""

import text_utils

def average_words():
    text = file.open("sample.txt", "r")
    lines = text.readlines()
    avg = 0
    num_lns = len(lines)
    for i in lines:
        avg += text_utils.words(i)
    return f'Average words per line: {avg/num_lns}'
