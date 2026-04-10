def word_count(text):
    list_o_words = text.split()
    return len(list_o_words)

def char_occurrence(text):
    working_text = text.lower()
    dictionary = {}
    for character in working_text:
        dictionary[character] = dictionary.get(character, 0) + 1
        
    return dictionary

def sort_on(items):
    return items["num"]

def sorted_characters(dict):
    dict_list = []
    for i in dict:
        dict_list.append({"char": i, "num": dict[i]})
    
    dict_list.sort(reverse=True, key=sort_on)

    return dict_list



     
