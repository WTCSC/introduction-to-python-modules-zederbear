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
    # opens the file
    text = open("sample.txt", "r")
    # turns the file into a list
    lines = text.readlines()
    # closes the file
    text.close()
    # defines the average starting at 0
    avg = 0
    # defines the number of lines by getting the length of the list that is the file
    num_lns = len(lines)
    # adds the amount of words in each index of the lines list to avg
    for i in lines:
        avg += text_utils.count_words(i)
    # returns the average words per line
    return f'Average words per line: {avg//num_lns}'
print(average_words())
