def get_book_text():
    with open("books/frankenstein.txt") as f:

        book_text = f.read()
        return book_text

def word_count(transcript):
    word_count = len(transcript.split())
    return word_count
    

def main():
    book_text = get_book_text() #this gets the entire transcript of the book, works
    
    num_words = word_count(book_text) 
    print (f"{num_words} words found in the document")

main()

