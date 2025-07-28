from stats import word_count, char_count_in_book



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
main()

