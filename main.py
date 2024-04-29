def main():
    book_path = "books/frankenstein.txt"

    text = get_book_text(book_path)
    words = get_word_count(text)
    
    characters = get_character_count(text)
    letters = get_letter_counts(characters)
    letters.sort(reverse=True, key=sort_count)
    
    print_report(book_path, words, letters)


def get_word_count(book_text):
    words = book_text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_character_count(book_text):
    character_counts = {}
    for char in book_text.lower():
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts


def get_letter_counts(character_counts):
    letter_counts = [
        {"letter": key, "count": value}
        for key, value in character_counts.items()
        if key.isalpha()
    ]

    return letter_counts


def sort_count(dict):
    return dict["count"]


def print_report(book, words, letters):
    print(f"--- Begin report of {book} ---")
    print(f"{words} words found in the document")
    print()
    for item in letters:
        print(f"The '{item['letter']}' character was found {item['count']} times")
    print()
    print("--- End report ---")


main()