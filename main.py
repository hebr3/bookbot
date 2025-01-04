def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    lookup = {}
    for c in text.lower():
        if c in "abcdefghijklmnopqrstuvwxyz":
            if c in lookup:
                lookup[c] += 1
            else:
                lookup[c] = 1

    print(f"--- Begin report of {book_path} ---")
    print(f"{len(text.split())} words found in the document")
    print("")
    for ch in sorted(lookup, key=lookup.get, reverse=True):
        print(f"The '{ch}' character was found {lookup[ch]} times")
    print("--- End report ---")



def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
