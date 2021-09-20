def get_text():
    """The function gets text from a file and writes it to a string"""
    text_in_file = open('text', 'r')
    text = ''
    for line in text_in_file:
        text += line
    return text


def main():
    text = get_text()
    whitespaces = [' ', '\n', '\t']

    new_text = []  # This list contains our text without separator characters
    buffer = 1  # Temporary variable
    buf = ''  # Temporary variable to store the word
    for symbol in text:
        """If the 'buffer' is equal to 0 therefore the program skips this symbol and changes 'buffer' to 1.
        Otherwise, the program adds the symbol to 'new_text'"""
        for item in whitespaces:
            if symbol == item:
                buffer = 0
                break
        if buffer == 0:
            if len(buf) != 0:  # If the text contains 2 spaces for example
                new_text.append(buf)
                buf = ''  # Remove the current word
            buffer = 1
            continue
        else:
            buf += symbol
    new_text.append(buf)  # Add the last word
    print(new_text)


main()
