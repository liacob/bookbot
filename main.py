"""My main function."""
import sys
from stats import character_count, count_words


def get_book_text(filepath):
    """Extract book text."""
    with open(filepath, encoding="UTF-8") as f:
        file_contents = f.read()
    return file_contents


def main():
    """Main."""
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    word_ocurrences = count_words(book_text)
    character_ocurrences = character_count(book_text)
    print(f"Found {word_ocurrences} total words")
    for key, value in character_ocurrences.items():
        print(f"{key}: {value}")


main()
