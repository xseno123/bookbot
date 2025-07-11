def get_book_words(text):
    words = text.split()
    return len(words)

def count_character(text):
    char_dict = {}
    text_lower = text.lower()
    for c in text_lower:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict

def sort_on(d):
    return d["num"]

def sort_it (dict):
    sorter =[]
    for ch in dict:
        sorter.append({"char":ch, "num": dict[ch]})
    sorter.sort(reverse=True, key=sort_on)
    return sorter


    #list_of_dicts = [{"char": k, "num": v} for k, v in dict.items()]
    #list_of_dicts.sort(key=lambda x: x["num"], reverse = True)

    #return list_of_dicts
    #return list_of_dicts["num"]


