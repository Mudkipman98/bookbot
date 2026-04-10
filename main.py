import sys
from stats import word_count, char_occurrence, sorted_characters

#?"books/frankenstein.txt" #this is just the path, not an actual useable variable, it's just there for the get_book_text function to use

def get_book_text(path):
    with open(path) as b:
        return b.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book = sys.argv[1]

    book_text = get_book_text(book) #assigns the text of the target book to the string book_text
    num_words = word_count(book_text)
    char_dict = char_occurrence(book_text)
    sorted_chars = sorted_characters(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_chars:
        if item['char'].isalpha() == False:
            continue
        print(f"{item['char']}" + ": " + f"{item['num']}")

main()
