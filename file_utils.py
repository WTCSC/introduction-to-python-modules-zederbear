def line_count():
    # opens file
    file = open('file.txt', 'r')

    # reads the lines of the file
    lines = file.readlines()

    # closes the file
    file.close()

    # returns the length of the list we got from reading the lines
    return len(lines)
