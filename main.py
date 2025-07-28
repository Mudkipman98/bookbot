def get_book_text():
    with open("books/frankenstein.txt") as f:

    
        book_text = f.read()
        return book_text

def main():
    print(get_book_text())    

main()

