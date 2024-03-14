print("hello world")
def main():
    book_path = "/home/felixmaster/workspace/github.com/primdonm/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    print(f"{num_words} words found in the document")


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


main()