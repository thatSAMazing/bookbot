def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = char_count(text)
    sorted_char_counts = sort_dict_into_dict_list(char_counts)
    for d in sorted_char_counts:
        if d["char"].isalpha():
            print(f"The '{d['char']}' character wsa found {d['num']} times")



def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def char_count(text):
    lowered = text.lower()
    char_dict = {}
    for char in lowered:
        if char in char_dict:
            char_dict[char]+=1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_dict_into_dict_list(d):
    new_list = []
    for key, value in d.items():
        new_dict = {"char": key, "num": value}
        new_list.append(new_dict)

    new_list.sort(reverse=True,key=sort_on)
    return new_list

main()
