"""Text manipulation functions."""


def count_words(book_contents):
    """Count words in text."""
    return len(book_contents.split())


def character_count(book_contents, ordered=True):
    """Count characters in text.
    """
    character_ocurrences = {}
    for char in book_contents.lower():
        if char.isalpha():
            if char in character_ocurrences:
                character_ocurrences[char] += 1
            else:
                character_ocurrences[char] = 1
    if ordered:
        return dict(sorted(
            character_ocurrences.items(),
            key=lambda character: character[1],
            reverse=True
            ))
    else:
        return character_ocurrences
