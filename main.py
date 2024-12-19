def main():
    book = "./books/frankenstein.txt"
    text = get_book_contents(book)
    print(f"--- Begin report of {book} ---")
    print(f"{word_count(text)} words found in the document")
    characters = character_count(text)
    character_list = []
    for character in characters:
        if character.isalpha():
            character_list.append({"character": character, "count": characters[character]})
    character_list.sort(reverse=True, key=sort_on)
    for character in character_list:
        print(f"The '{character['character']}' character was found {character['count']} times")
    
def sort_on(dict):
    return dict["count"]

def get_book_contents(book):
    with open(book) as f:
        return f.read()

def word_count(book):
    count = book.split()
    return len(count)
    
def character_count(book):
    characters = {}
    for character in book:
        character = character.lower()
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
            
    return characters
    
main()