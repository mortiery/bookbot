def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    word_count = get_word_count(file_contents)
    character_count_dict = get_character_count_dict(file_contents)
    print_report(book_path, word_count, character_count_dict)

def get_book_text(filename):
    with open(filename) as f:
        return f.read()
    
def get_word_count(text):
    return len(text.split())

def get_character_count_dict(text):
    character_count_dict = {}
    for character in text:
        character_lower = character.lower()
        if character_lower not in character_count_dict:
            character_count_dict[character_lower] = 1
        else:
            character_count_dict[character_lower] += 1
    return character_count_dict

def make_sorted_filtered_character_count_list(character_count_dict):
    character_count_list = []
    for character in character_count_dict:
        if (character.isalpha()):
            character_count_list.append({"character": character, "count": character_count_dict[character]})

    def get_count(character_entry):
        return character_entry["count"]
    
    character_count_list.sort(reverse=True, key=get_count)
    return character_count_list
    
def print_report(book_path, word_count, character_count_dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    character_count_list = make_sorted_filtered_character_count_list(character_count_dict)
    for entry in character_count_list:
        print(f"The '{entry["character"]}' character was found {entry["count"]} times")
    print("--- End report ---")

main()