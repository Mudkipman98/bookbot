from stats import word_count, char_count_in_book, all_chars_in_book



def get_book_text():
    with open("books/frankenstein.txt") as f:

        book_text = f.read()
        return book_text




def main():
    book_text = get_book_text()
    book_text = book_text.lower() #all of the book's text in lowercase

    num_words = word_count(book_text)
    print (f"{num_words} words found in the document")

    char_count = char_count_in_book(book_text)

    print(char_count)

    sorted_chars_in_book = all_chars_in_book(char_count)

    for i in sorted_chars_in_book:
        key = i.keys()
        key_list = list(key)

        if key_list[0].isalpha() != True:
            sorted_chars_in_book = sorted_chars_in_book.pop(sorted_chars_in_book[i])


    print(sorted_chars_in_book)
main()

