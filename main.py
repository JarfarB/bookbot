from stats import get_num_words, get_chars_dict, sort_dict_list
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    text = get_book_text(book_path)
    print("----------- Word Count ----------")
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    list_chars_dict = sort_dict_list(chars_dict)
    for item in list_chars_dict:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    #print(list_chars_dict)
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()

