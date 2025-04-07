def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return(char_count)

def sort_on(dict):
    return dict["count"]

def sort_char_count(char_count):
    chars_list = []
    for char, count in char_count.items():
        chars_list.append({"char":char, "count":count})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list