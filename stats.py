"""Text manipulation functions."""


def count_words(book_contents):
    """Count words in text."""
    return len(book_contents.split())


def character_count(book_contents):
    """Count characters in text"""
    ordered_ocurrences = []
    characters_ocurrences = {}
    final_ocurrences = {}
    for character in book_contents.lower():
        if character.isalpha():
            if character in characters_ocurrences:
                characters_ocurrences[character] += 1
            else:
                characters_ocurrences[character] = 1
    for key, value in characters_ocurrences.items():
        ordered_ocurrences.append(
            {"char": key, "num": int(value)}
            )
    # print(type(ordered_ocurrences))
    ordered_ocurrences.sort(reverse=True, key=sort_on)
    for character_counted in ordered_ocurrences:
        final_ocurrences[character_counted["char"]] = character_counted["num"]

    return final_ocurrences


def sort_on(items):
    """Sort by num key."""
    return items["num"]
