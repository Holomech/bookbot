def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    characters = {}

    for ch in text:
        character = ch.lower()
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] +=1
    
    return characters

def sort_on(dict):
    return dict["count"]

def report_results(text):
    book = "books/frankenstein.txt"
    characters = character_count(text)
    list_of_characters = []
    for item in characters:
        if item.isalpha():
            list_of_characters.append({"character": item, "count": characters[item]})
    list_of_characters.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book} ---")
    print(f"{word_count(text)} words found in the document\n")
    for dict in list_of_characters:
        print(f"The '{dict['character']}' character was found {dict['count']} times")
    print("--- End report ---")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    # print(word_count(file_contents))
    # characters = character_count(file_contents)
    # print(characters)
    report_results(file_contents)

main()