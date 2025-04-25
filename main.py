from stats import get_num_words
from stats import get_num_letters
from stats import chars_dict_to_sorted_list

#print("hello world")
def main():
    #book_path = "/home/felixmaster/workspace/github.com/primdonm/bookbot/books/frankenstein.txt"
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)


    print(f"{num_words} words found in the document")

    chars_dict = get_num_letters(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    #print(f"{num_words} words found in the document")
    #print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")




def get_book_text(path):
    with open(path) as f:
        return f.read()







main()