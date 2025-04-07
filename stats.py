def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_char_count(path_to_file):
    char_count = {}
    with open(path_to_file) as f:
        file_contents = f.read()
        for char in file_contents.lower():
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