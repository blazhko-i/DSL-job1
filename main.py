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

    new_text = []  # This list contains our text without separator characters. Each element of the list
    # is equal to the word
    buffer = ''  # Temporary variable to store the word
    for symbol in text:
        """If the 'buffer' is equal to 0 therefore the program skips this symbol and changes 'buffer' to 1.
        Otherwise, the program adds the symbol to 'new_text'"""
        if symbol not in whitespaces:
            buffer += symbol
        else:
            if len(buffer) != 0:  # If the text contains 2 spaces for example
                new_text.append(buffer)
                buffer = ''  # Remove the current word

    new_text.append(buffer)  # Add the last word
    print(new_text)


main()
