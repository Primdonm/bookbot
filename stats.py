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

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

