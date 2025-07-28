def word_count(transcript):
    word_count = len(transcript.split())
    return word_count

characters_in_book = {'t': 0, 'h': 0, 'e': 0, ' ': 0, 'p': 0, 'r': 0, 'o': 0, 'j': 0, 'c': 0, 'g': 0, 'u': 0, 'n': 0, 'b': 0, 'k': 0, 'f': 0, 'a': 0, 's': 0, 'i': 0, ';': 0, ',': 0, 'm': 0, 'd': 0, '\n': 0, 'y': 0, 'w': 0, 'l': 0, 'v': 0, '.': 0, '-': 0, ':': 0, '2': 0, '3': 0, '0': 0, '1': 0, '[': 0, '#': 0, '4': 0, '5': 0, ']': 0, '&': 0, '8': 0, '/': 0, '*': 0, '’': 0, 'x': 0, '_': 0, 'q': 0, '?': 0, '—': 0, '6': 0, 'z': 0, '(': 0, ')': 0, '7': 0, 'æ': 0, '!': 0, '“': 0, '”': 0, '9': 0, 'ë': 0, '‘': 0, 'â': 0, 'ê': 0, 'ô': 0, '™': 0, '•': 0, '%': 0, '$': 0}

def char_count_in_book(book_text):
    for i in book_text:
        characters_in_book[i] = characters_in_book[i] + 1
    return characters_in_book
    
