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

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    # print(word_count(file_contents))
    characters = character_count(file_contents)
    print(characters)

main()