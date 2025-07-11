from stats import get_book_words, count_character, sort_it
import sys
def get_book_text(book):

    with open(book) as f:
        file_content = f.read()
    return file_content



def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_book_words(text)
    
    counter = count_character(text)
    sorted_list = sort_it(counter)
    print_report(book_path,num_words,sorted_list)
    #print(sort_on(counter))

def print_report(book_path, num_words, sorted_list):   
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for i in sorted_list:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
    
    #print(counter)





main()