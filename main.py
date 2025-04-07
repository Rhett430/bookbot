from stats import(
    get_word_count
    ,get_char_count,
    sort_char_count)
import sys
def main():
        if len(sys.argv) != 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
        else:
            book_path = sys.argv[1]
            text = get_book_text(book_path)
            word_count = get_word_count(text)
            char_count = get_char_count(text)
            sorted_char_count = sort_char_count(char_count)
            print_report(book_path, word_count, sorted_char_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()
 
def print_report(book_path,word_count,sorted_char_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_char_count:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["count"]}")
    
    print("============= END ===============")

main()