from stats import word_count, char_count_in_book, all_chars_in_book, sorted_dict



def get_book_text():
    with open("books/frankenstein.txt") as f:

        book_text = f.read()
        return book_text

def main():
    book_text = get_book_text() #assign the text of our document to the variable 'book_text'
    book_text = book_text.lower() #update book_text to be in all lowercase

    num_words = word_count(book_text) #count the words in book_text
    print (f"{num_words} words found in the document") #print the wordcount

    char_count = char_count_in_book(book_text)

    #print(char_count) #prints the updated characters_in_book found in stats.py.  It's an unsorted dictionary at this point, with key:value pairs of {'character': 'occurrence', 'character': 'occurrence', etc.}

    list_of_dicts_of_chars = all_chars_in_book(char_count)

    for i in list_of_dicts_of_chars:
        key = i.keys()
        key_list = list(key)

        if key_list[0].isalpha() != True:
            list_of_dicts_of_chars = list_of_dicts_of_chars.pop(list_of_dicts_of_chars[i])


    print(list_of_dicts_of_chars) #This gives us the dictionary we need to sort, then make pretty later.

    sorted_characters_by_occurance = sorted_dict(list_of_dicts_of_chars)

    print(sorted_characters_by_occurance)
    

main()

