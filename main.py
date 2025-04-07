from stats import get_book_text
from stats import get_char_count
from stats import sort_char_count
def main():
    word_count = 0
    char_count = get_char_count("./books/frankenstein.txt")
    frank = get_book_text("./books/frankenstein.txt")
    words=frank.split()
    for word in words:
        word_count += 1
    print(f"{word_count} words found in the document")
    print(char_list)
main()