def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_num_chr(book_text):
    chrs_dict = {}
    for c in book_text.lower():
        chrs_dict[c] = chrs_dict.get(c, 0) + 1
    return chrs_dict

def get_sorted_chars(char_counts_dict):
    sorted_list = []
    for char, count in char_counts_dict.items():
        sorted_list.append({"char": char, "num": count})

    def sort_by(item):
        return item["num"]

    sorted_list.sort(reverse=True, key=sort_by)
    return sorted_list
