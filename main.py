print("hello world")
def main():
    book_path = "/home/felixmaster/workspace/github.com/primdonm/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)


    print(f"{num_words} words found in the document")

    chars_dict = get_num_letters(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    word = text.lower()
    d={}
    for i in word:
        keys = d.keys()
        if i in keys:
            d[i] +=1
        else:
            d[i] = 1
        #d[i]= d.get(i,0)+1
    #letter_list = list(words)    
    print(d)
    return (d)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list



main()